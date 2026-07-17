"""QA scanner for the For Teachers and Educators line (PyMuPDF).

Checks, per PDF, exit 1 on any failure:

1. Word-boundary overflow — words inside side margins (54pt ± 3) and the
   vertical band (40..762).
2. Tc audit — every nonzero charSpace is reset to 0 and pages end at Tc=0
   (the DWYI Tc-leak bug guard).
3. Grayscale legibility (NEW, line requirement) — every text span's fill
   color must photocopy dark: relative luminance <= 0.45. Color may only
   decorate shapes, never carry text a teacher or student must read.
"""

import glob
import re
import sys

import fitz

PAGE_W = 612
M, TOL = 54, 3.0
LUM_MAX = 0.45

pdfs = sorted(glob.glob("../*.pdf"))
assert len(pdfs) == 6, f"expected 6 PDFs, found {len(pdfs)}"

problems = []
total_pages = total_words = 0

for path in pdfs:
    doc = fitz.open(path)
    name = path.split("/")[-1]
    total_pages += doc.page_count
    for pno in range(doc.page_count):
        page = doc[pno]
        words = page.get_text("words")
        total_words += len(words)

        for x0, y0, x1, y1, w, *_ in words:
            if x0 < M - TOL or x1 > PAGE_W - M + TOL:
                problems.append(f"{name} p{pno+1}: word {w!r} outside side margins (x0={x0:.1f}, x1={x1:.1f})")
            if y0 < 40 - TOL or y1 > 762 + TOL:
                problems.append(f"{name} p{pno+1}: word {w!r} outside vertical bounds (y0={y0:.1f}, y1={y1:.1f})")

        stream = page.read_contents().decode("latin-1")
        tcs = [float(v) for v in re.findall(r"(-?[\d.]+)\s+Tc\b", stream)]
        if tcs and tcs[-1] != 0.0:
            problems.append(f"{name} p{pno+1}: page ends with Tc={tcs[-1]}")
        for i, v in enumerate(tcs):
            if v != 0.0 and not any(x == 0.0 for x in tcs[i + 1:]):
                problems.append(f"{name} p{pno+1}: nonzero Tc={v} never reset")
                break

        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    col = span["color"]
                    r, g, b = (col >> 16) & 255, (col >> 8) & 255, col & 255
                    lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
                    if lum > LUM_MAX:
                        problems.append(
                            f"{name} p{pno+1}: text {span['text'][:40]!r} too light for "
                            f"grayscale (lum={lum:.2f}, color=#{col:06x})")

print(f"scanned {len(pdfs)} PDFs, {total_pages} pages, {total_words} words")
if problems:
    print(f"\n{len(problems)} problem(s):")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("QA clean: margins ok, Tc always reset, all text photocopy-dark.")
