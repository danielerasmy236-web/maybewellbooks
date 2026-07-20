"""QA scanner for Letter to the Future (PyMuPDF).

Two checks, exit code 1 if any fails:

1. Word-boundary overflow: every extracted word bbox must sit inside the
   page margins (54pt sides, with 3pt tolerance).

2. Tc-operator audit: every nonzero `Tc` must be followed by a `0 Tc` before
   the stream ends, and the running Tc value at end-of-page must be 0.
"""

import re
import sys

import fitz

PDF = "../letter-to-the-future_v1.0_letter.pdf"
PAGE_W, PAGE_H = 612, 792
M = 54
TOL = 3.0

doc = fitz.open(PDF)
problems = []

for pno in range(doc.page_count):
    page = doc[pno]

    words = page.get_text("words")
    for x0, y0, x1, y1, w, *_ in words:
        if x0 < M - TOL or x1 > PAGE_W - M + TOL:
            problems.append(f"p{pno+1}: word {w!r} outside side margins "
                            f"(x0={x0:.1f}, x1={x1:.1f})")
        if y0 < 40 - TOL or y1 > 760 + TOL:
            problems.append(f"p{pno+1}: word {w!r} outside vertical bounds "
                            f"(y0={y0:.1f}, y1={y1:.1f})")

    stream = page.read_contents().decode("latin-1")
    tc_values = [float(v) for v in re.findall(r"(-?[\d.]+)\s+Tc\b", stream)]
    running = 0.0
    for v in tc_values:
        running = v
    if running != 0.0:
        problems.append(f"p{pno+1}: page ends with Tc={running}")
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
print("QA clean: no overflow, Tc always reset.")
