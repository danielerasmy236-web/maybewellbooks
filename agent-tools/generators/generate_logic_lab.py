import sys
import os
import textwrap

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mw_lib import brand, logic_grid
from content import logic_lab_content as ct
from reportlab.lib.units import inch


def _page_bg(c):
    c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
    c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)


def _header(c, label, title, accent):
    c.setFillColorRGB(*brand._hex_rgb(accent))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, label.upper())
    c.setFillColorRGB(*brand._hex_rgb(brand.INK))
    c.setFont("Helvetica-Bold", 16)
    c.drawString(brand.MARGIN, brand.PAGE_H - 1.2 * inch, title)


def draw_solution_grid(c, x0, y0, cols_labels, rows_labels, ink_hex, cellw=0.42 * inch, cellh=0.32 * inch):
    r, g, b = brand._hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setFillColorRGB(r, g, b)
    n_rows = len(rows_labels)
    n_cols = len(cols_labels)
    c.setFont("Helvetica", 6)
    for j, lab in enumerate(cols_labels):
        cx = x0 + (j + 1) * cellw + cellw / 2
        c.saveState()
        c.translate(cx, y0 + (n_rows + 1) * cellh + 4)
        c.rotate(45)
        c.drawString(0, 0, lab)
        c.restoreState()
    c.setFont("Helvetica-Bold", 7)
    for i, lab in enumerate(rows_labels):
        cy = y0 + (n_rows - i) * cellh
        c.drawRightString(x0 + cellw - 4, cy - cellh / 2 - 3, lab)
    c.setLineWidth(0.7)
    for i in range(n_rows + 1):
        c.line(x0, y0 + i * cellh, x0 + (n_cols + 1) * cellw, y0 + i * cellh)
    for j in range(n_cols + 2):
        c.line(x0 + j * cellw, y0, x0 + j * cellw, y0 + (n_rows + 1) * cellh)
    return (n_rows + 1) * cellh


def build(output_path, seed=20260812):
    c = brand.new_canvas(output_path, "Little Logic Lab", "30 logic puzzles and 5 detective cases")
    accent = getattr(brand, ct.ACCENT)
    ink = brand.INK

    brand.draw_cover(c, ct.TITLE, ct.SUBTITLE, "maybewellbooks.com", accent)
    brand.draw_intro_page(c, "Think It Through", ct.INTRO_BODY, accent)

    page_num = 3
    grid_puzzles = []

    label = f"{len(ct.GRID_THEMES)} PUZZLES · #1-{len(ct.GRID_THEMES)}"
    brand.draw_section_divider(c, label, "Logic Grids", accent, "Use the grid to mark what's impossible")
    page_num += 1

    for i, theme in enumerate(ct.GRID_THEMES, start=1):
        names = [ct.NAME_POOL[(i * 3 + k) % len(ct.NAME_POOL)] for k in range(3)]
        puzzle = logic_grid.generate_puzzle(names, theme["b_values"], theme["c_values"], seed + i)
        grid_puzzles.append((i, puzzle))

        _page_bg(c)
        _header(c, f"Logic Grid #{i} of {len(ct.GRID_THEMES)}", f"Who has what?", accent)
        c.setFont("Helvetica", 11)
        y = brand.PAGE_H - 1.7 * inch
        c.setFillColorRGB(*brand._hex_rgb(ink))
        for j, clue in enumerate(puzzle["clues"], start=1):
            for line in textwrap.wrap(f"{j}. {clue}", 78):
                c.drawString(brand.MARGIN, y, line)
                y -= 0.24 * inch
            y -= 0.04 * inch

        cols_labels = theme["b_values"] + theme["c_values"]
        draw_solution_grid(c, brand.MARGIN, 1.3 * inch, cols_labels, puzzle["names"], ink,
                            cellw=0.55 * inch, cellh=0.4 * inch)

        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    brand.draw_section_divider(c, "15 PUZZLES · #16-30", "Pattern Riddles", accent, "Find the rule, then continue it")
    page_num += 1

    for i, riddle in enumerate(ct.PATTERN_RIDDLES, start=1):
        _page_bg(c)
        _header(c, f"Pattern Riddle #{i + 15} of 30", riddle["title"], accent)
        c.setFont("Helvetica-Bold", 26)
        c.setFillColorRGB(*brand._hex_rgb(ink))
        seq_text = "   ".join(riddle["seq"])
        c.drawCentredString(brand.PAGE_W / 2, brand.PAGE_H - 3 * inch, seq_text)
        c.setFont("Helvetica", 11)
        c.drawCentredString(brand.PAGE_W / 2, brand.PAGE_H - 4 * inch, "What comes next? Write your answer below.")
        brand.draw_blank_box(c, brand.PAGE_W / 2 - 0.8 * inch, brand.PAGE_H - 5.3 * inch, 1.6 * inch, 0.8 * inch, ink)
        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    brand.draw_section_divider(c, "5 CASES", "Detective Cases", accent, "Read every clue. One alibi always breaks.")
    page_num += 1

    for i, case in enumerate(ct.DETECTIVE_CASES, start=1):
        _page_bg(c)
        _header(c, f"Case #{i} of 5", case["title"], accent)
        c.setFont("Helvetica", 11)
        y = brand.PAGE_H - 1.7 * inch
        for line in textwrap.wrap(case["setup"], 78):
            c.drawString(brand.MARGIN, y, line)
            y -= 0.24 * inch
        y -= 0.2 * inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(brand.MARGIN, y, "SUSPECTS")
        y -= 0.28 * inch
        c.setFont("Helvetica", 10)
        for s in case["suspects"]:
            for line in textwrap.wrap("• " + s, 80):
                c.drawString(brand.MARGIN, y, line)
                y -= 0.22 * inch
            y -= 0.06 * inch
        y -= 0.15 * inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(brand.MARGIN, y, "CLUES")
        y -= 0.28 * inch
        c.setFont("Helvetica", 10)
        for cl in case["clues"]:
            for line in textwrap.wrap("• " + cl, 80):
                c.drawString(brand.MARGIN, y, line)
                y -= 0.22 * inch
            y -= 0.06 * inch
        y -= 0.15 * inch
        c.setFont("Helvetica-BoldOblique", 10)
        c.drawString(brand.MARGIN, y, "Who did it? ________________________")
        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    # --- solutions ---
    brand.draw_section_divider(c, "SOLUTIONS", "Answers", accent)
    page_num += 1

    _page_bg(c)
    _header(c, "Solutions", "Logic Grids", accent)
    c.setFont("Helvetica", 9)
    y = brand.PAGE_H - 1.6 * inch
    for i, puzzle in grid_puzzles:
        parts = []
        for n in puzzle["names"]:
            sol = puzzle["solution"][n]
            vals = " / ".join(sol.values())
            parts.append(f"{n} = {vals}")
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawString(brand.MARGIN, y, f"#{i}: " + "; ".join(parts))
        y -= 0.24 * inch
        if y < 1 * inch:
            brand.draw_footer(c, page_num, accent)
            c.showPage()
            page_num += 1
            _page_bg(c)
            _header(c, "Solutions", "Logic Grids (continued)", accent)
            y = brand.PAGE_H - 1.6 * inch
    brand.draw_footer(c, page_num, accent)
    c.showPage()
    page_num += 1

    _page_bg(c)
    _header(c, "Solutions", "Pattern Riddles", accent)
    c.setFont("Helvetica", 10)
    y = brand.PAGE_H - 1.6 * inch
    for i, riddle in enumerate(ct.PATTERN_RIDDLES, start=1):
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawString(brand.MARGIN, y, f"#{i + 15}: {riddle['answer']}  —  rule: {riddle['rule']}")
        y -= 0.26 * inch
    brand.draw_footer(c, page_num, accent)
    c.showPage()
    page_num += 1

    for case in ct.DETECTIVE_CASES:
        _page_bg(c)
        _header(c, "Solution", case["title"], accent)
        c.setFont("Helvetica", 11)
        y = brand.PAGE_H - 1.7 * inch
        for line in textwrap.wrap(case["solution"], 78):
            c.drawString(brand.MARGIN, y, line)
            y -= 0.24 * inch
        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    c.save()
    return page_num - 1


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/logic_lab.pdf"
    total_pages = build(out)
    print(f"Generated {out} with {total_pages} pages")
