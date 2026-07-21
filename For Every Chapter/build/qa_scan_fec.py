"""QA scanner for the "For Every Chapter" line (PyMuPDF). Parameterized:

    python3 qa_scan_fec.py <path-to-pdf>

Same three checks as the Grandparents'/Teachers scanners, exit 1 on any
failure. Extra attention (per the line brief) to whether large-print sizing
causes overflow the standard-size catalog never hits — the margins check is
the guard for that.

1. Word-boundary overflow: every extracted word bbox inside 54pt side
   margins (3pt tolerance) and 40..760 vertical bounds.
2. Tc-operator audit: every nonzero `Tc` later reset to 0; page ends at 0.
3. Grayscale legibility: every text span's fill must photocopy dark —
   relative luminance <= 0.45 (large-print/senior line = photocopy bar).
"""

import re
import sys

import fitz

PDF = sys.argv[1]
PAGE_W, PAGE_H = 612, 792
M = 54
TOL = 3.0
LUM_MAX = 0.45

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

    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                col = span["color"]
                r, g, b = (col >> 16) & 255, (col >> 8) & 255, col & 255
                lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
                if lum > LUM_MAX:
                    problems.append(
                        f"p{pno+1}: text {span['text'][:40]!r} too light for "
                        f"grayscale (lum={lum:.2f}, color=#{col:06x})")

print(f"{PDF}: scanned {doc.page_count} pages, "
      f"{sum(len(doc[p].get_text('words')) for p in range(doc.page_count))} words")
if problems:
    print(f"\n{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("QA clean: no overflow, Tc always reset, all text photocopy-dark.")
