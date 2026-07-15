import sys
import os
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mw_lib import brand, word_search as ws
from content import word_search_content as ct
from reportlab.lib.units import inch


def build(output_path, seed=20260722):
    c = brand.new_canvas(output_path, "Word Search Safari", "35 themed word-search puzzles across savanna, reef, and rainforest")
    accent = getattr(brand, ct.ACCENT)
    rng = random.Random(seed)

    brand.draw_cover(c, ct.TITLE, ct.SUBTITLE, "maybewellbooks.com", accent)
    brand.draw_intro_page(c, "Welcome to the Safari", ct.INTRO_BODY, accent)

    page_num = 3
    puzzle_num = 0
    solved_records = []

    for theme in ct.THEMES:
        label = f"{theme['count']} HUNTS · #{puzzle_num + 1}–{puzzle_num + theme['count']}"
        brand.draw_section_divider(c, label, theme["name"], accent, theme["note"])
        page_num += 1

        for i in range(theme["count"]):
            puzzle_num += 1
            words = rng.sample(theme["pool"], ct.WORDS_PER_PUZZLE)
            bonus = rng.choice(theme["bonus_pool"])
            grid, placements = ws.generate_grid(words + [bonus], ct.GRID_SIZE, seed=seed + puzzle_num)
            solved_records.append((theme["name"], puzzle_num, grid, placements, words, bonus))

            c.setFillColorRGB(*brand._hex_rgb(brand.INK))
            c.setFont("Helvetica-Bold", 10)
            c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, f"HUNT #{puzzle_num} · {theme['name'].upper()}")

            area = 5.6 * inch
            x0 = (brand.PAGE_W - area) / 2
            y0 = 2.3 * inch
            ws.render_grid(c, grid, ct.GRID_SIZE, x0, y0, area, brand.INK)

            c.setFont("Helvetica", 10)
            words_line = "   ".join(sorted(words))
            c.drawCentredString(brand.PAGE_W / 2, y0 - 0.35 * inch, words_line)
            c.setFont("Helvetica-Oblique", 9)
            c.drawCentredString(brand.PAGE_W / 2, y0 - 0.6 * inch, "+ one more hiding animal not on the list")

            brand.draw_footer(c, page_num, accent)
            c.showPage()
            page_num += 1

    sol_label = f"{len(solved_records)} SOLUTIONS · WORDS + BONUS ANIMALS"
    brand.draw_section_divider(c, sol_label, "Solutions", accent)
    page_num += 1

    per_page = 6
    for start in range(0, len(solved_records), per_page):
        chunk = solved_records[start:start + per_page]
        c.setFillColorRGB(*brand._hex_rgb(brand.INK))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(brand.MARGIN, brand.PAGE_H - 0.7 * inch, "SOLUTIONS")

        cols_n = 2
        rows_n = 3
        cell_w = (brand.PAGE_W - 2 * brand.MARGIN) / cols_n
        top = brand.PAGE_H - 1.1 * inch
        bottom_limit = 0.8 * inch
        cell_h = (top - bottom_limit) / rows_n
        for idx, (theme_name, pnum, grid, placements, words, bonus) in enumerate(chunk):
            col = idx % cols_n
            row = idx // cols_n
            x0 = brand.MARGIN + col * cell_w
            y0 = top - (row + 1) * cell_h
            c.setFont("Helvetica-Bold", 8)
            c.setFillColorRGB(*brand._hex_rgb(brand.INK))
            c.drawString(x0 + 4, y0 + cell_h - 12, f"#{pnum} · bonus: {bonus.title()}")
            area = min(cell_w, cell_h) - 0.5 * inch
            ws.render_grid(c, grid, ct.GRID_SIZE, x0 + 8, y0 + 8, area, brand.INK, cell_font=6)
            ws.render_solution_overlay(c, placements, ct.GRID_SIZE, x0 + 8, y0 + 8, area, accent)

        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    c.save()
    return page_num - 1


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/word_search_safari.pdf"
    total_pages = build(out)
    print(f"Generated {out} with {total_pages} pages")
