"""Generate Memory Bingo (letter PDF). For Every Chapter line.

Template H: facilitator rules page, two caller-list pages with check
boxes, then 10 unique 4x4 bingo cards (deterministic layouts seeded from
content). High-contrast thick card borders, large-print squares — designed
to be read from a slight distance in a group room.
"""

import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "For Every Chapter", "build"))

import fec_lib as F
import content_memorybingo as C

OUT_PATH = os.path.join(HERE, "..", "memory-bingo_v1.0_letter.pdf")


def icon_bingo(c, cx=None, y_top=500, scale=1.0):
    """Cover icon: a 4x4 mini card with an ochre winning row."""
    cx = cx if cx is not None else F.PAGE_W / 2
    side = 96 * scale
    x0 = cx - side / 2
    y1 = F.ty(y_top)
    y0 = y1 - side
    cell = side / 4

    c.setFillColorRGB(*F.rgb(F.OCHRE))
    c.rect(x0, y0 + 2 * cell, side, cell, fill=1, stroke=0)

    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(2.4 * scale)
    c.rect(x0, y0, side, side, fill=0, stroke=1)
    c.setLineWidth(1.6 * scale)
    for i in range(1, 4):
        c.line(x0 + i * cell, y0, x0 + i * cell, y0 + side)
        c.line(x0, y0 + i * cell, x0 + side, y0 + i * cell)


def caller_page(c, phrases, start_no, page_num):
    F.tracked_text(c, F.M, F.ty(62), "CALLER LIST", "Nunito-Bold", 11, 2.0)
    F.plain_text(c, F.PAGE_W - F.M, F.ty(62),
                 f"Phrases {start_no:02d}-{start_no + len(phrases) - 1:02d}",
                 "Fraunces-SemiBold", 13, F.INK, right=True)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    F.plain_text(c, F.M, F.ty(100),
                 "Call in any order. Read each twice. Check off as you go.",
                 "Nunito-XLI", 12, F.INK)

    y = 136
    for i, ph in enumerate(phrases):
        c.setStrokeColorRGB(*F.rgb(F.INK))
        c.setLineWidth(1.6)
        c.rect(F.M, F.ty(y + 4), 14, 14, fill=0, stroke=1)
        F.plain_text(c, F.M + 26, F.ty(y), f"{start_no + i:02d}", "Nunito-Bold",
                     13, F.INK)
        F.plain_text(c, F.M + 60, F.ty(y), ph, "Nunito-Reg", 14, F.INK)
        y += 29

    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def card_page(c, card_no, phrases, page_num):
    F.tracked_text(c, F.M, F.ty(62), "MEMORY BINGO", "Nunito-Bold", 11, 2.0)
    F.plain_text(c, F.PAGE_W - F.M, F.ty(62), f"Card No. {card_no:02d}",
                 "Fraunces-SemiBold", 13, F.INK, right=True)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    F.plain_text(c, F.M, F.ty(100),
                 "Mark a square if it's true of you. Four in a row wins.",
                 "Nunito-XLI", 12, F.INK)

    # 4x4 grid, high-contrast borders
    grid_top = 124.0
    side = F.CW
    cell_w = side / 4
    cell_h = 136.0
    x0 = F.M

    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(2.6)
    c.rect(x0, F.ty(grid_top + 4 * cell_h), side, 4 * cell_h, fill=0, stroke=1)
    c.setLineWidth(1.8)
    for i in range(1, 4):
        c.line(x0 + i * cell_w, F.ty(grid_top), x0 + i * cell_w,
               F.ty(grid_top + 4 * cell_h))
        c.line(x0, F.ty(grid_top + i * cell_h), x0 + side,
               F.ty(grid_top + i * cell_h))

    for idx, ph in enumerate(phrases):
        row, col = divmod(idx, 4)
        cx = x0 + col * cell_w + cell_w / 2
        lines = F.wrap(ph, "Nunito-Bold", 11.5, cell_w - 16)
        block_h = len(lines) * 16
        yy = grid_top + row * cell_h + (cell_h - block_h) / 2 + 12
        for ln in lines:
            F.plain_text(c, cx, F.ty(yy), ln, "Nunito-Bold", 11.5, F.INK,
                         center=True)
            yy += 16

    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def closing_page(c, page_num):
    F.putty_bg(c)
    F.plain_text(c, F.PAGE_W / 2, F.ty(300), C.CLOSING_TITLE,
                 "Fraunces-Black", 28, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(346), C.CLOSING_BODY, "Nunito-Reg",
                 14.5, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(412), C.CLOSING_STATS, "Nunito-Bold",
                 13, F.INK, center=True)
    icon_bingo(c, y_top=470, scale=0.62)
    F.plain_text(c, F.PAGE_W / 2, F.ty(660), "M A Y B E W E L L   B O O K S",
                 "Nunito-Bold", 11, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(682), C.CFG["TAGLINE"], "Nunito-XL",
                 11, F.INK, center=True)
    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def build_cards():
    """Deterministic unique layouts: 16 phrases sampled from the 40 per
    card, seeded so the shipped book is reproducible."""
    rng = random.Random(C.CARD_SEED)
    cards = []
    seen = set()
    while len(cards) < C.CARD_COUNT:
        pick = tuple(rng.sample(C.PHRASES, 16))
        if pick not in seen:
            seen.add(pick)
            cards.append(list(pick))
    return cards


def main():
    F.register_fonts()
    out = os.path.abspath(OUT_PATH)
    cfg = dict(C.CFG)
    cfg["icon_fn"] = lambda c: icon_bingo(c, y_top=496)
    cfg["icon_fn_small"] = lambda c: icon_bingo(c, y_top=484, scale=0.62)

    c = F.start_canvas(out, "Memory Bingo — Bingo Where Every Square Is a "
                            "Life Actually Lived",
                       "A large-print group game for senior centers: bingo "
                       "with life-experience phrases instead of numbers, a "
                       "40-phrase caller list, and ten unique cards.")
    F.cover_page(c, cfg)
    F.title_page(c, cfg)
    F.intro_page(c, cfg, C.INTRO_KICKER, C.INTRO_TITLE, C.INTRO_PARAS, 3)

    page = 4
    caller_page(c, C.PHRASES[:20], 1, page)
    page += 1
    caller_page(c, C.PHRASES[20:], 21, page)
    page += 1

    for i, card in enumerate(build_cards(), start=1):
        card_page(c, i, card, page)
        page += 1

    closing_page(c, page)
    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
