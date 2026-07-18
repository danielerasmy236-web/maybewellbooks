"""QA scanner for Wander Without a Destination (PyMuPDF).

Four checks, exit code 1 if any fails:

1. Word-boundary overflow: every extracted word bbox must sit inside the page
   margins (54pt sides, with 3pt tolerance; footer/header rows get their own
   band). Catches wrapped-text math errors and any letterspacing bloat.

2. Zone integrity: on WALK/LOG/NOTICE pages, the NOTICE ruled-lines zone
   (from just below the NOTICE label to the bottom margin) must contain no
   words other than the "one thing along the way" caption on its own label
   row — prompt/hint/log text bleeding down into the writing lines is this
   template's failure mode (the equivalent of TWIW's "words in the DRAW box"
   check, adapted for a ruled-lines zone instead of a blank sketch box).

3. Tc-operator audit: in every page content stream, each nonzero `Tc`
   (character spacing) must be followed by a `0 Tc` before the stream ends,
   and the running Tc value at end-of-page must be 0. This is the DWYI
   "Tc leak" bug: Tc is page-level text state that survives past ET, so an
   unreset tracked label letterspaces everything drawn after it.

4. Prompt-count sanity: confirms the book has exactly 70 WALK/LOG/NOTICE
   pages (one per prompt in content_wander.py).
"""

import re
import sys

import fitz

PDF = "../wander-without-a-destination_v1.0_letter.pdf"
PAGE_W, PAGE_H = 612, 792
M = 54
TOL = 3.0

doc = fitz.open(PDF)
problems = []
field_page_count = 0

for pno in range(doc.page_count):
    page = doc[pno]

    # --- 1. word-boundary overflow ---
    words = page.get_text("words")
    for x0, y0, x1, y1, w, *_ in words:
        if x0 < M - TOL or x1 > PAGE_W - M + TOL:
            problems.append(f"p{pno+1}: word {w!r} outside side margins "
                            f"(x0={x0:.1f}, x1={x1:.1f})")
        if y0 < 40 - TOL or y1 > 760 + TOL:
            problems.append(f"p{pno+1}: word {w!r} outside vertical bounds "
                            f"(y0={y0:.1f}, y1={y1:.1f})")

    # --- 2. NOTICE zone must be empty (WALK/LOG/NOTICE pages only) ---
    # Tracked (letterspaced) labels like "WALK" get split into individual
    # single-letter "words" by get_text("words") because charSpace pushes
    # the glyphs past the tokenizer's join threshold — so zone detection has
    # to happen at the span level (get_text("dict")), where the whole label
    # still comes back as one span ("W A L K") with spaces from the tracking.
    spans = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                spans.append((span["text"], span["bbox"]))
    norm = {text.replace(" ", ""): bbox for text, bbox in spans}
    is_field_page = "WALK" in norm and "LOG" in norm and "NOTICE" in norm
    if is_field_page:
        field_page_count += 1
        notice_top = norm["NOTICE"][1]
        # ruled-lines zone: from just below the NOTICE/caption row down to
        # where the ruled lines actually stop (706pt, matching ruled_lines()
        # in generate_wander.py) — NOT all the way to the footer band, since
        # the footer legitimately sits below that.
        zone_top = notice_top + 14
        zone = fitz.Rect(M + 2, zone_top, PAGE_W - M - 2, 706 + 4)
        for x0, y0, x1, y1, w, *_ in words:
            if fitz.Rect(x0, y0, x1, y1).intersects(zone):
                problems.append(f"p{pno+1}: word {w!r} inside NOTICE ruled-lines zone")

    # --- 3. Tc audit ---
    stream = page.read_contents().decode("latin-1")
    tc_values = [float(v) for v in re.findall(r"(-?[\d.]+)\s+Tc\b", stream)]
    running = 0.0
    for v in tc_values:
        running = v
    if running != 0.0:
        problems.append(f"p{pno+1}: page ends with Tc={running} (leaks into "
                        f"nothing here, but violates the reset discipline)")
    for i, v in enumerate(tc_values):
        if v != 0.0 and not any(x == 0.0 for x in tc_values[i + 1:]):
            problems.append(f"p{pno+1}: nonzero Tc={v} never reset to 0")
            break

print(f"scanned {doc.page_count} pages, "
      f"{sum(len(doc[p].get_text('words')) for p in range(doc.page_count))} words")
print(f"WALK/LOG/NOTICE pages found: {field_page_count} (expected 70)")
if field_page_count != 70:
    problems.append(f"expected 70 field pages, found {field_page_count}")

if problems:
    print(f"\n{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("QA clean: no overflow, no words in NOTICE ruled-lines zone, Tc always reset.")
