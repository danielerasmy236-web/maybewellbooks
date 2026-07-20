import sys
import os
import textwrap

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mw_lib import brand, mazes, game_boards as gb, autumn_shapes as sh
from content import autumn_book_content as ct
from reportlab.lib.units import inch


def _page_bg(c):
    c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
    c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)


def _title(c, label, title):
    c.setFillColorRGB(*brand._hex_rgb(brand.INK))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, label.upper())
    c.setFont("Helvetica-Bold", 20)
    c.drawString(brand.MARGIN, brand.PAGE_H - 1.25 * inch, title)


def render_activity(c, section_name, act, page_num, accent, seed):
    _page_bg(c)
    _title(c, section_name, act["title"])
    ink = brand.INK
    area_w = brand.PAGE_W - 2 * brand.MARGIN
    top = brand.PAGE_H - 1.7 * inch
    bottom = 1.0 * inch
    cx = brand.PAGE_W / 2
    t = act["type"]

    if t == "rubbing":
        c.setFont("Helvetica-Oblique", 10)
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawCentredString(cx, top, "Place a real leaf or object underneath and rub gently with a crayon.")
        sh.draw_leaf(c, cx, (top + bottom) / 2 - 0.3 * inch, 3.6 * inch, act["shape"], ink) if act["shape"] not in ("acorn", "pinecone") else None
        if act["shape"] == "acorn":
            sh.draw_acorn(c, cx, (top + bottom) / 2, 3.2 * inch, ink)
        elif act["shape"] == "pinecone":
            sh.draw_pinecone(c, cx, (top + bottom) / 2, 3.2 * inch, ink)

    elif t == "counting":
        c.setFont("Helvetica", 11)
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawCentredString(cx, top, "Count them one at a time, then write the number below.")
        fn = sh.SHAPE_FN[act["icon"]]
        n = act["count"]
        cols = 5
        icon_size = 0.55 * inch
        gap = area_w / cols
        y = top - 1.0 * inch
        for i in range(n):
            col = i % cols
            row = i // cols
            fn(c, brand.MARGIN + col * gap + gap / 2, y - row * 1.0 * inch, icon_size, ink)
        box_y = bottom + 0.6 * inch
        c.setFont("Helvetica-Bold", 12)
        c.drawString(cx - 1.3 * inch, box_y, "There are")
        brand.draw_blank_box(c, cx + 0.1 * inch, box_y - 0.1 * inch, 0.6 * inch, 0.45 * inch, ink)
        c.drawString(cx + 0.85 * inch, box_y, f"{act['icon']}s.")

    elif t == "addition":
        c.setFont("Helvetica-Bold", 28)
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawCentredString(cx, (top + bottom) / 2 + 0.5 * inch, f"{act['a']} leaves + {act['b']} leaves = ___")
        for i in range(act["a"] + act["b"]):
            sh.draw_leaf(c, brand.MARGIN + 0.4 * inch + (i % 6) * 1.1 * inch, (top + bottom) / 2 - 0.6 * inch - (i // 6) * 1.1 * inch, 0.7 * inch, "oak", ink)

    elif t == "estimate":
        sh.draw_pumpkin(c, cx, (top + bottom) / 2 + 0.4 * inch, 3 * inch, ink)
        c.setFont("Helvetica", 11)
        c.drawCentredString(cx, bottom + 0.5 * inch, "My guess: _______   Grown-up's guess: _______   Actual count: _______")

    elif t == "maze":
        cols, rows = act["grid"]
        walls = mazes.generate_maze(cols, rows, seed=seed)
        size = min(area_w, top - bottom)
        mazes.render_maze(c, walls, cols, rows, brand.MARGIN + (area_w - size) / 2, bottom, size, ink)

    elif t == "dots":
        pts = sh.DOT_TO_DOT_PUMPKIN if act["shape"] == "pumpkin" else sh.DOT_TO_DOT_LEAF
        size = min(area_w, top - bottom, 4.5 * inch)
        x0 = brand.MARGIN + (area_w - size) / 2
        y0 = bottom + (top - bottom - size) / 2
        gb.draw_dot_to_dot(c, x0, y0, size, pts, ink)
        c.setFont("Helvetica-Oblique", 9)
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawCentredString(cx, y0 - 0.3 * inch, "Connect the dots in order, then connect the last one back to #1.")

    elif t == "choices":
        c.setFont("Helvetica", 13)
        y = top - 0.3 * inch
        for opt in act["options"]:
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.circle(brand.MARGIN + 8, y - 4, 8, fill=0, stroke=1)
            c.drawString(brand.MARGIN + 0.4 * inch, y - 8, opt)
            y -= 0.55 * inch

    elif t == "draw_blank":
        brand.draw_blank_box(c, brand.MARGIN, bottom, area_w, top - bottom, ink)

    elif t == "colorbynumber":
        _draw_tree(c, cx, (top + bottom) / 2, 4 * inch, ink)
        c.setFont("Helvetica-Bold", 10)
        y = bottom + 0.3 * inch
        for num, colorname in ct.COLOR_KEY:
            c.setFillColorRGB(*brand._hex_rgb(getattr(brand, colorname)))
            c.rect(brand.MARGIN + 0 * inch, y, 14, 14, fill=1, stroke=0)
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.drawString(brand.MARGIN + 20, y + 3, num)
            y -= 0

    elif t == "wordmatch":
        c.setFont("Helvetica", 12)
        y = top
        for word, definition in ct.WORD_MATCH_PAIRS:
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.drawString(brand.MARGIN, y, word)
            c.drawRightString(brand.PAGE_W - brand.MARGIN, y, definition)
            y -= 0.5 * inch

    elif t == "weather":
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        cellw = area_w / 7
        c.setFont("Helvetica-Bold", 9)
        for i, day in enumerate(days):
            x = brand.MARGIN + i * cellw + cellw / 2
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.drawCentredString(x, top, day)
            for j, label in enumerate(["Sunny", "Cloudy", "Rainy", "Windy"]):
                yy = top - 0.5 * inch - j * 0.4 * inch
                c.circle(x, yy, 5, fill=0, stroke=1)
                c.setFont("Helvetica", 7)
                c.drawCentredString(x, yy - 18, label)
                c.setFont("Helvetica-Bold", 9)

    elif t == "gratitude":
        for i in range(5):
            y = top - i * 1.2 * inch
            sh.draw_leaf(c, brand.MARGIN + 0.4 * inch, y, 0.8 * inch, "birch", ink)
            c.setStrokeColorRGB(*brand._hex_rgb(ink))
            c.setLineWidth(0.6)
            c.line(brand.MARGIN + 1 * inch, y - 0.35 * inch, brand.PAGE_W - brand.MARGIN, y - 0.35 * inch)

    elif t == "pie":
        r = 1.8 * inch
        import math
        c.setStrokeColorRGB(*brand._hex_rgb(ink))
        c.setLineWidth(1.4)
        c.circle(cx, (top + bottom) / 2 + 0.4 * inch, r, fill=0, stroke=1)
        cy0 = (top + bottom) / 2 + 0.4 * inch
        for i in range(6):
            ang = i * math.pi / 3
            c.line(cx, cy0, cx + r * math.cos(ang), cy0 + r * math.sin(ang))
        c.setFont("Helvetica", 9)
        c.drawCentredString(cx, bottom + 0.3 * inch, "Label each slice with your favorite pie topping.")

    elif t == "tictactoe":
        gb.draw_multigrid(c, brand.MARGIN + area_w / 2 - 1.2 * inch, (top + bottom) / 2 - 0.6 * inch, 2.4 * inch, 2.4 * inch, 1, ink)
        c.setFont("Helvetica", 10)
        c.drawCentredString(cx, bottom + 0.4 * inch, "Use leaves and acorns as markers instead of X and O.")

    elif t == "bingo":
        size = min(area_w, top - bottom)
        gb.draw_bingo(c, brand.MARGIN + (area_w - size) / 2, bottom, size, ct.BINGO_ITEMS, ink, accent)

    elif t == "ispy":
        c.setFont("Helvetica", 13)
        y = top
        for item in ct.ISPY_ITEMS:
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.rect(brand.MARGIN, y - 10, 12, 12, fill=0, stroke=1)
            c.drawString(brand.MARGIN + 0.3 * inch, y - 9, item)
            y -= 0.4 * inch

    elif t == "charades":
        c.setFont("Helvetica", 12)
        y = top
        for i, item in enumerate(ct.CHARADES_ITEMS, start=1):
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.drawString(brand.MARGIN, y, f"{i}. {item}")
            y -= 0.35 * inch
        c.setFont("Helvetica-Oblique", 9)
        c.drawString(brand.MARGIN, y - 0.1 * inch, "Cut apart, fold, and pick one from a hat.")

    brand.draw_footer(c, page_num, accent)


def _draw_tree(c, cx, cy, size, ink_hex):
    c.setStrokeColorRGB(*brand._hex_rgb(ink_hex))
    c.setLineWidth(1.4)
    trunk_w = size * 0.12
    c.rect(cx - trunk_w / 2, cy - size * 0.5, trunk_w, size * 0.35, fill=0, stroke=1)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(*brand._hex_rgb(ink_hex))
    c.drawCentredString(cx, cy - size * 0.32, "4")
    for i, frac in enumerate([0.05, -0.15, -0.32]):
        w = size * (0.9 - i * 0.22)
        y = cy - size * 0.15 + i * size * 0.28
        c.ellipse(cx - w / 2, y - size * 0.12, cx + w / 2, y + size * 0.12, fill=0, stroke=1)
        c.drawCentredString(cx, y - 4, str(i + 1))


def build(output_path, seed=20260805):
    c = brand.new_canvas(output_path, "The Autumn Book", "28 autumn activities for ages 5-8")
    accent = getattr(brand, ct.ACCENT)

    brand.draw_cover(c, ct.TITLE, ct.SUBTITLE, ct.TAGLINE, accent)
    brand.draw_intro_page(c, "One Cozy Season", ct.INTRO_BODY, accent)

    page_num = 3
    total = sum(len(s["activities"]) for s in ct.SECTIONS)
    act_counter = 0

    for section in ct.SECTIONS:
        label = f"{len(section['activities'])} ACTIVITIES · #{act_counter + 1}-{act_counter + len(section['activities'])}"
        brand.draw_section_divider(c, label, section["name"], accent, section["note"])
        page_num += 1
        for act in section["activities"]:
            act_counter += 1
            render_activity(c, section["name"], act, page_num, accent, seed + act_counter)
            c.showPage()
            page_num += 1

    c.save()
    return page_num - 1


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/autumn_book.pdf"
    total_pages = build(out)
    print(f"Generated {out} with {total_pages} pages")
