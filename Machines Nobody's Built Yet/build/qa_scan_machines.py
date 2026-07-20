"""QA scanner for Machines Nobody's Built Yet (PyMuPDF).

Four checks, exit code 1 if any fails:

1. Word-boundary overflow: every extracted word bbox must sit inside the page
   margins (54pt sides, with 3pt tolerance; footer/header rows get their own
   band). Catches wrapped-text math errors and any letterspacing bloat.

2. Draw-box zone integrity: on prompt pages, the dashed blank drawing box
   (from its adaptive top edge down to y=706) must contain no text — this
   template's failure mode is prompt/hint text bleeding down into the space
   meant for the reader's drawing. The box top is adaptive (it depends on
   how many lines the prompt/hint wrap to), so this reuses
   compute_prompt_layout() from the generator itself as the single source of
   truth, rather than re-deriving the math and risking drift.
   Detection happens at the SPAN level (get_text("dict")), not the word
   level (get_text("words")): tracked/letterspaced labels get split into
   individual single-letter "words" by the word tokenizer because charSpace
   pushes glyphs past its join threshold, which silently no-ops a word-level
   containment check on that text. This was discovered and fixed in the
   Wander Without a Destination build's qa_scan_wander.py and is reused here
   defensively even though this template's own tracked labels (the section
   eyebrow, the "No. XX" folio) sit outside the box on every page.

3. Tc-operator audit: in every page content stream, each nonzero `Tc`
   (character spacing) must be followed by a `0 Tc` before the stream ends,
   and the running Tc value at end-of-page must be 0. This is the DWYI
   "Tc leak" bug: Tc is page-level text state that survives past ET, so an
   unreset tracked label letterspaces everything drawn after it.

4. Prompt-count sanity: confirms the book has exactly 60 prompt pages (one
   per prompt across content_machines.SECTIONS) and 72 pages total.
"""

import re
import sys

import fitz

import content_machines as C
from generate_machines import CW, M, compute_prompt_layout, register_fonts

PDF = "../machines-nobodys-built-yet_v1.0_letter.pdf"
PAGE_W, PAGE_H = 612, 792
TOL = 3.0

register_fonts()  # compute_prompt_layout() calls pdfmetrics.stringWidth(), which needs fonts registered

# Rebuild the (page_num -> (prompt, hint)) map exactly as main() does, so the
# draw-box zone check knows which page is which prompt.
page = 5
prompt_counter = 0
prompt_pages = {}  # page_num (1-indexed) -> (prompt, hint)
for title, note, prompts in C.SECTIONS:
    divider_page_num = page
    start_p = prompt_counter + 1
    for prompt, hint in prompts:
        prompt_counter += 1
        pg = divider_page_num + prompt_counter - start_p + 1
        prompt_pages[pg] = (prompt, hint)
    page += 1 + len(prompts)
closing_page_num = page
colophon_page_num = page + 1

doc = fitz.open(PDF)
problems = []

for pno in range(doc.page_count):
    page_1 = pno + 1
    pg = doc[pno]

    # --- 1. word-boundary overflow ---
    words = pg.get_text("words")
    for x0, y0, x1, y1, w, *_ in words:
        if x0 < M - TOL or x1 > PAGE_W - M + TOL:
            problems.append(f"p{page_1}: word {w!r} outside side margins "
                            f"(x0={x0:.1f}, x1={x1:.1f})")
        if y0 < 40 - TOL or y1 > 760 + TOL:
            problems.append(f"p{page_1}: word {w!r} outside vertical bounds "
                            f"(y0={y0:.1f}, y1={y1:.1f})")

    # --- 2. draw-box zone must be empty (prompt pages only) ---
    # Span-level, not word-level: get_text("words") tokenizes on whitespace
    # gaps, so a letterspaced (charSpace-tracked) label can get chopped into
    # single-letter "words" whose individual bboxes may not actually
    # intersect a tight zone rect even though the label as a whole does —
    # a silent no-op. get_text("dict") returns each label as one span
    # (tracking shows up as extra spaces within the span's own text), which
    # is the reliable unit to test for zone containment.
    if page_1 in prompt_pages:
        prompt, hint = prompt_pages[page_1]
        _, _, box_top = compute_prompt_layout(prompt, hint)
        zone = fitz.Rect(M + 2, box_top + 2, PAGE_W - M - 2, 706 - 2)
        spans = []
        for block in pg.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    spans.append((span["text"], span["bbox"]))
        for text, bbox in spans:
            if not text.strip():
                continue
            if fitz.Rect(*bbox).intersects(zone):
                problems.append(f"p{page_1}: span {text!r} inside blank drawing box")

    # --- 3. Tc audit ---
    stream = pg.read_contents().decode("latin-1")
    tc_values = [float(v) for v in re.findall(r"(-?[\d.]+)\s+Tc\b", stream)]
    running = 0.0
    for v in tc_values:
        running = v
    if running != 0.0:
        problems.append(f"p{page_1}: page ends with Tc={running}")
    for i, v in enumerate(tc_values):
        if v != 0.0 and not any(x == 0.0 for x in tc_values[i + 1:]):
            problems.append(f"p{page_1}: nonzero Tc={v} never reset to 0")
            break

print(f"scanned {doc.page_count} pages, "
      f"{sum(len(doc[p].get_text('words')) for p in range(doc.page_count))} words")
print(f"prompt pages found: {len(prompt_pages)} (expected 60)")
print(f"total pages: {doc.page_count} (expected {colophon_page_num})")

if len(prompt_pages) != 60:
    problems.append(f"expected 60 prompt pages, found {len(prompt_pages)}")
if doc.page_count != colophon_page_num:
    problems.append(f"expected {colophon_page_num} total pages, found {doc.page_count}")

if problems:
    print(f"\n{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("QA clean: no overflow, no words in the blank drawing box, Tc always reset.")
