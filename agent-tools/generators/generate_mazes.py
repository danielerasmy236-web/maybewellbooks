import sys
import os
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mw_lib import brand, mazes
from content import mazes_content as ct
from reportlab.lib.units import inch


def build(output_path, seed=20260715):
    c = brand.new_canvas(output_path, "Mazes of the Lost City", "42 hand-drawn mazes, jungle-city themed puzzle book")
    accent = getattr(brand, ct.ACCENT)

    brand.draw_cover(c, ct.TITLE, ct.SUBTITLE, ct.TAGLINE, accent)

    brand.draw_intro_page(c, "Welcome to the Lost City", ct.INTRO_BODY, accent)

    page_num = 3
    maze_records = []  # (tier, index, walls, cols, rows, path, caption)
    maze_counter = 0

    for tier in ct.TIERS:
        cols, rows = tier["grid"]
        count = len(tier["captions"])
        label = f"{count} MAZES · #{maze_counter + 1}–{maze_counter + count}"
        brand.draw_section_divider(c, label, tier["name"], accent, tier["note"])
        page_num += 1

        for i, caption in enumerate(tier["captions"]):
            maze_counter += 1
            seed_i = seed + maze_counter
            walls = mazes.generate_maze(cols, rows, seed=seed_i)
            path = mazes.solve_maze(walls, cols, rows)
            maze_records.append((tier["key"], maze_counter, walls, cols, rows, path, caption))

            c.setFillColorRGB(*brand._hex_rgb(brand.INK))
            c.setFont("Helvetica-Bold", 10)
            c.drawString(brand.MARGIN, brand.PAGE_H - 1.35 * inch, f"MAZE #{maze_counter}")
            c.setFont("Helvetica-Oblique", 10)
            c.drawRightString(brand.PAGE_W - brand.MARGIN, brand.PAGE_H - 1.35 * inch, caption)

            size = brand.PAGE_W - 2 * brand.MARGIN
            x0 = brand.MARGIN
            y0 = 1.0 * inch
            mazes.render_maze(c, walls, cols, rows, x0, y0, size, brand.INK)

            brand.draw_footer(c, page_num, accent)
            c.showPage()
            page_num += 1

    # solutions section
    sol_label = f"{len(maze_records)} SOLUTIONS · IN CASE THE JUNGLE WINS"
    brand.draw_section_divider(c, sol_label, "Solutions", accent)
    page_num += 1

    per_page = 4
    for start in range(0, len(maze_records), per_page):
        chunk = maze_records[start:start + per_page]
        c.setFillColorRGB(*brand._hex_rgb(brand.INK))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(brand.MARGIN, brand.PAGE_H - 0.7 * inch, "SOLUTIONS")

        cell_w = (brand.PAGE_W - 2 * brand.MARGIN) / 2
        cell_h = 3.6 * inch
        top = brand.PAGE_H - 1.1 * inch
        for idx, (tier_key, mnum, walls, cols, rows, path, caption) in enumerate(chunk):
            col = idx % 2
            row = idx // 2
            x0 = brand.MARGIN + col * cell_w
            y0 = top - (row + 1) * cell_h
            c.setFont("Helvetica-Bold", 8)
            c.setFillColorRGB(*brand._hex_rgb(brand.INK))
            c.drawString(x0 + 4, y0 + cell_h - 12, f"#{mnum} · {caption}")
            size = min(cell_w, cell_h) - 0.5 * inch
            mazes.render_maze(c, walls, cols, rows, x0 + 8, y0 + 8, size, brand.INK, path=path, path_hex=accent)

        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    # bonus map page
    brand.draw_section_divider(c, "BONUS", ct.BONUS_MAP_TITLE, accent)
    page_num += 1
    _draw_bonus_map(c, maze_records, accent)
    brand.draw_footer(c, page_num, accent)
    c.showPage()
    page_num += 1

    c.save()
    return page_num - 1


def _draw_bonus_map(c, maze_records, accent_hex):
    c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
    c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)

    c.setFillColorRGB(*brand._hex_rgb(brand.INK))
    c.setFont("Helvetica", 10)
    y = brand.PAGE_H - 1.3 * inch
    for line in ct.BONUS_MAP_BODY:
        c.drawCentredString(brand.PAGE_W / 2, y, line)
        y -= 0.22 * inch

    rng = random.Random(7)
    tier_colors = {"easy": brand.TEAL, "medium": brand.OCHRE, "hard": brand.CORAL}
    cols_n, rows_n = 6, 6
    area_w = brand.PAGE_W - 2 * brand.MARGIN
    area_h = 4.6 * inch
    x0 = brand.MARGIN
    y0 = 1.3 * inch
    cell_w = area_w / cols_n
    cell_h = area_h / rows_n

    nodes = []
    used = set()
    for rec in maze_records[::4]:
        while True:
            gx, gy = rng.randrange(cols_n), rng.randrange(rows_n)
            if (gx, gy) not in used:
                used.add((gx, gy))
                break
        cx = x0 + (gx + 0.5) * cell_w
        cy = y0 + (gy + 0.5) * cell_h
        nodes.append((cx, cy, rec[0]))

    c.setLineWidth(1.4)
    for i in range(len(nodes) - 1):
        x1, y1, _ = nodes[i]
        x2, y2, _ = nodes[i + 1]
        c.setStrokeColorRGB(*brand._hex_rgb(brand.INK))
        mx = (x1 + x2) / 2
        c.line(x1, y1, mx, y1)
        c.line(mx, y1, mx, y2)
        c.line(mx, y2, x2, y2)

    for cx, cy, tier_key in nodes:
        color = tier_colors.get(tier_key, brand.INK)
        c.setFillColorRGB(*brand._hex_rgb(color))
        c.roundRect(cx - 14, cy - 10, 28, 20, 4, fill=1, stroke=0)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/mazes_of_the_lost_city.pdf"
    total_pages = build(out)
    print(f"Generated {out} with {total_pages} pages")
