"""QA scanner for The World Is Watching (PyMuPDF).

Three checks, exit code 1 if any fails:

1. Word-boundary overflow: every extracted word bbox must sit inside the page
   margins (54pt sides, with 3pt tolerance; footer/header rows get their own
   band). Catches wrapped-text math errors and any letterspacing bloat.

2. Zone integrity: on field-log pages the DRAW sketch box (the big dashed
   rect) must contain no words at all — prompt/hint/log text bleeding into
   the sketch zone is the three-zone layout's failure mode.

3. Tc-operator audit: in every page content stream, each nonzero `Tc`
   (character spacing) must be followed by a `0 Tc` before the stream ends,
   and the running Tc value at end-of-page must be 0. This is the DWYI
   "Tc leak" bug: Tc is page-level text state that survives past ET, so an
   unreset tracked label letterspaces everything drawn after it.
"""

import re
import sys

import fitz

PDF = "../the-world-is-watching_v1.0_letter.pdf"
PAGE_W, PAGE_H = 612, 792
M = 54
TOL = 3.0

doc = fitz.open(PDF)
problems = []

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

    # --- 2. DRAW box must be empty (field pages only) ---
    is_field_page = any(w[4] == "DRAW" for w in words) and \
        any(w[4] == "LOG" for w in words)
    if is_field_page:
        # the sketch box is the tallest rect-ish drawing on the page
        boxes = [d["rect"] for d in page.get_drawings()
                 if d["rect"].width > 400 and d["rect"].height > 200]
        if not boxes:
            problems.append(f"p{pno+1}: field page has no DRAW box drawing")
        else:
            box = max(boxes, key=lambda r: r.height)
            inner = fitz.Rect(box.x0 + 2, box.y0 + 2, box.x1 - 2, box.y1 - 2)
            for x0, y0, x1, y1, w, *_ in words:
                if fitz.Rect(x0, y0, x1, y1).intersects(inner):
                    problems.append(f"p{pno+1}: word {w!r} inside DRAW box")

    # --- 3. Tc audit ---
    stream = page.read_contents().decode("latin-1")
    tc_values = [float(v) for v in re.findall(r"(-?[\d.]+)\s+Tc\b", stream)]
    running = 0.0
    for v in tc_values:
        running = v
    if running != 0.0:
        problems.append(f"p{pno+1}: page ends with Tc={running} (leaks into "
                        f"nothing here, but violates the reset discipline)")
    # every nonzero Tc must be followed by a zero Tc later in the stream
    for i, v in enumerate(tc_values):
        if v != 0.0 and not any(x == 0.0 for x in tc_values[i + 1:]):
            problems.append(f"p{pno+1}: nonzero Tc={v} never reset to 0")
            break

print(f"scanned {doc.page_count} pages, "
      f"{sum(len(doc[p].get_text('words')) for p in range(doc.page_count))} words")
if problems:
    print(f"\n{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("QA clean: no overflow, no words in DRAW boxes, Tc always reset.")
