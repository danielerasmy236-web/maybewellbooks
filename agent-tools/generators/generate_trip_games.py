import sys
import os
import textwrap

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mw_lib import brand, game_boards as gb
from content import trip_games_content as ct
from reportlab.lib.units import inch


def _header(c, page_num, index, total, title, rules, accent):
    c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
    c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)
    c.setFillColorRGB(*brand._hex_rgb(accent))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, f"GAME #{index} OF {total}")
    c.setFillColorRGB(*brand._hex_rgb(brand.INK))
    c.setFont("Helvetica-Bold", 20)
    c.drawString(brand.MARGIN, brand.PAGE_H - 1.25 * inch, title)
    c.setFont("Helvetica", 10)
    y = brand.PAGE_H - 1.6 * inch
    for line in textwrap.wrap(rules, 78):
        c.drawString(brand.MARGIN, y, line)
        y -= 0.2 * inch
    return y - 0.2 * inch


def build(output_path):
    c = brand.new_canvas(output_path, "Road Trip Games", "18 two-player paper-and-pencil games")
    accent = getattr(brand, ct.ACCENT)

    brand.draw_cover(c, ct.TITLE, ct.SUBTITLE, ct.TAGLINE, accent)
    brand.draw_intro_page(c, "Buckle Up", ct.INTRO_BODY, accent)

    page_num = 3
    total = len(ct.GAMES)
    ink = brand.INK

    for idx, game in enumerate(ct.GAMES, start=1):
        top = _header(c, page_num, idx, total, game["title"], game["rules"], accent)
        board_type, p1, p2 = game["board"]
        area_w = brand.PAGE_W - 2 * brand.MARGIN
        bottom = 1.0 * inch

        if board_type == "dots":
            gb.draw_dots(c, brand.MARGIN + 0.5 * inch, bottom + 0.3 * inch, area_w - 1 * inch, top - bottom - 0.6 * inch, p1, p2, ink)
        elif board_type == "multigrid":
            gb.draw_multigrid(c, brand.MARGIN, bottom + 1.5 * inch, area_w, 1.6 * inch, p2, ink)
        elif board_type == "grid":
            size_w = area_w
            size_h = top - bottom
            cols = p1
            rows = p2 or p1
            side = min(size_w, size_h)
            gb.draw_grid(c, brand.MARGIN + (area_w - side) / 2, bottom, side, side, cols, rows, ink)
        elif board_type == "coordgrid":
            side = min(area_w, top - bottom) - 0.3 * inch
            gb.draw_coordgrid(c, brand.MARGIN + 0.4 * inch, bottom + 0.2 * inch, side, p1, ink)
        elif board_type == "bingo":
            side = min(area_w, top - bottom)
            gb.draw_bingo(c, brand.MARGIN + (area_w - side) / 2, bottom, side, ct.BINGO_ITEMS, ink, accent)
        elif board_type == "hangman":
            gb.draw_hangman(c, brand.MARGIN + 1 * inch, bottom + 0.5 * inch, ink, blanks=p1)
        elif board_type == "bracket":
            gb.draw_bracket(c, brand.MARGIN, bottom, area_w, top - bottom - 0.2 * inch, p1, ink)
        elif board_type == "mash":
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.setFont("Helvetica-Bold", 14)
            c.drawString(brand.MARGIN, top, "M   A   S   H")
            y = top - 0.4 * inch
            for cat, opts in ct.MASH_CATEGORIES.items():
                c.setFont("Helvetica-Bold", 10)
                c.drawString(brand.MARGIN, y, cat + ":")
                c.setFont("Helvetica", 10)
                c.drawString(brand.MARGIN + 1.8 * inch, y, "  /  ".join(o or "____" for o in opts))
                y -= 0.35 * inch
        elif board_type == "categories":
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.setFont("Helvetica-Bold", 9)
            c.drawString(brand.MARGIN, top, "Letter: ______")
            gb.draw_categories_table(c, brand.MARGIN, top - 0.4 * inch, area_w, ct.CATEGORIES, ink)
        elif board_type == "dottodot":
            side = min(area_w, top - bottom)
            gb.draw_dot_to_dot(c, brand.MARGIN + (area_w - side) / 2, bottom, side, ct.DOT_TO_DOT_STAR, ink)
        elif board_type == "sprouts":
            c.setFillColorRGB(*brand._hex_rgb(ink))
            for px, py in [(0.3, 0.5), (0.5, 0.6), (0.7, 0.5)]:
                c.circle(brand.MARGIN + px * area_w, bottom + py * (top - bottom), 3, fill=1, stroke=0)
        elif board_type == "ladder":
            ladder = ct.WORD_LADDERS[idx % len(ct.WORD_LADDERS)]
            gb.draw_word_ladder(c, brand.MARGIN, top, area_w, ladder["start"], ladder["end"], ladder["rungs"], ink)
        elif board_type == "checklist26":
            gb.draw_checklist26(c, brand.MARGIN, top - 0.5 * inch, area_w, ink)
        elif board_type == "foldtemplate":
            side = min(area_w, top - bottom)
            gb.draw_fold_template(c, brand.MARGIN + (area_w - side) / 2, bottom, side, ink)
        elif board_type == "drawguess":
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.setFont("Helvetica", 11)
            y = top
            for i in range(0, len(ct.DRAW_GUESS_WORDS), 2):
                c.drawString(brand.MARGIN, y, "• " + ct.DRAW_GUESS_WORDS[i])
                if i + 1 < len(ct.DRAW_GUESS_WORDS):
                    c.drawString(brand.MARGIN + area_w / 2, y, "• " + ct.DRAW_GUESS_WORDS[i + 1])
                y -= 0.3 * inch
        elif board_type == "cards":
            c.setFont("Helvetica", 12)
            y = top
            for prompt in ct.WOULD_YOU_RATHER:
                c.setFillColorRGB(*brand._hex_rgb(ink))
                for line in textwrap.wrap(prompt, 60):
                    c.drawString(brand.MARGIN, y, line)
                    y -= 0.22 * inch
                y -= 0.15 * inch

        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    brand.draw_section_divider(c, "SCORE SHEET", "Who's Winning?", accent, ct.SCORE_NOTE)
    page_num += 1
    c.setFillColorRGB(*brand._hex_rgb(ink))
    c.setFont("Helvetica-Bold", 10)
    y = brand.PAGE_H - 1.2 * inch
    c.drawString(brand.MARGIN, y, "GAME")
    c.drawString(brand.MARGIN + 4.2 * inch, y, "PLAYER 1")
    c.drawString(brand.MARGIN + 5.6 * inch, y, "PLAYER 2")
    y -= 0.1 * inch
    c.setLineWidth(1)
    c.line(brand.MARGIN, y, brand.PAGE_W - brand.MARGIN, y)
    y -= 0.3 * inch
    c.setFont("Helvetica", 10)
    for game in ct.GAMES:
        c.drawString(brand.MARGIN, y, game["title"])
        c.setLineWidth(0.6)
        c.line(brand.MARGIN + 4.2 * inch, y - 3, brand.MARGIN + 5.2 * inch, y - 3)
        c.line(brand.MARGIN + 5.6 * inch, y - 3, brand.MARGIN + 6.6 * inch, y - 3)
        y -= 0.32 * inch
    brand.draw_footer(c, page_num, accent)
    c.showPage()
    page_num += 1

    c.save()
    return page_num - 1


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/trip_games.pdf"
    total_pages = build(out)
    print(f"Generated {out} with {total_pages} pages")
