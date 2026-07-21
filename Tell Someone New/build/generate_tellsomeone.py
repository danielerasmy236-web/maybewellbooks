"""Generate Tell Someone New (letter PDF). For Every Chapter line.

Template B/E hybrid: one question per page, two labeled answer areas
(YOU / YOUR NEW FRIEND), questions ordered lighter to more personal, and a
closing page that turns the pairing into an actual plan to talk again.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "For Every Chapter", "build"))

import fec_lib as F
import content_tellsomeone as C

OUT_PATH = os.path.join(HERE, "..", "tell-someone-new_v1.0_letter.pdf")


def icon_chairs(c, cx=None, y_top=500, scale=1.0):
    """Cover icon: two chairs angled toward each other, ochre cushion on
    one — the two-seats-pulled-together motif."""
    cx = cx if cx is not None else F.PAGE_W / 2
    w = 34 * scale
    h = 58 * scale
    gap = 30 * scale
    base = F.ty(y_top + 90 * scale)

    for i, dx in enumerate((-gap - w, gap)):
        x0 = cx + dx
        c.setStrokeColorRGB(*F.rgb(F.INK))
        c.setLineWidth(2.6 * scale)
        # seat
        c.line(x0, base + 22 * scale, x0 + w, base + 22 * scale)
        # legs
        c.line(x0 + 3 * scale, base + 22 * scale, x0 + 3 * scale, base)
        c.line(x0 + w - 3 * scale, base + 22 * scale, x0 + w - 3 * scale, base)
        # back (inner side, so the chairs face each other)
        bx = x0 + (w - 3 * scale if i == 0 else 3 * scale)
        c.line(bx, base + 22 * scale, bx, base + h)
        c.line(bx, base + h,
               bx + (-14 * scale if i == 0 else 14 * scale), base + h)
        # cushion on one chair
        if i == 1:
            c.setFillColorRGB(*F.rgb(F.OCHRE))
            c.rect(x0 + 4 * scale, base + 24 * scale, w - 8 * scale,
                   7 * scale, fill=1, stroke=0)


def question_page(c, q_no, question, page_num):
    F.tracked_text(c, F.M, F.ty(62), "TELL SOMEONE NEW", "Nunito-Bold", 11, 2.0)
    F.plain_text(c, F.PAGE_W - F.M, F.ty(62), f"No. {q_no:02d} of 30",
                 "Fraunces-SemiBold", 13, F.INK, right=True)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    F.tracked_text(c, F.M, F.ty(112), "ASK EACH OTHER", "Nunito-Bold", 11, 2.4)
    y = 146
    for ln in F.wrap(question, "Fraunces-SemiBold", 21, F.CW):
        F.plain_text(c, F.M, F.ty(y), ln, "Fraunces-SemiBold", 21)
        y += 29

    top = max(y + 24, 260)
    F.tracked_text(c, F.M, F.ty(top), "YOU", "Nunito-Bold", 11, 2.4)
    F.ruled_lines(c, top + 30, top + 150)

    mid = top + 196
    F.tracked_text(c, F.M, F.ty(mid), "YOUR NEW FRIEND", "Nunito-Bold", 11, 2.4)
    F.ruled_lines(c, mid + 30, min(mid + 150, 706))

    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def closing_page(c, page_num):
    F.tracked_text(c, F.M, F.ty(66), "BEFORE YOU PUT THIS DOWN",
                   "Nunito-Bold", 11, 2.4)
    F.plain_text(c, F.M, F.ty(104), C.CLOSING_TITLE, "Fraunces-Black", 26, F.INK)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(122), F.PAGE_W - F.M, F.ty(122))

    y = 156
    for para in C.CLOSING_PARAS:
        for ln in F.wrap(para, "Nunito-Reg", 13.5, F.CW):
            F.plain_text(c, F.M, F.ty(y), ln, "Nunito-Reg", 13.5)
            y += 20
        y += 12

    # two columns of keep-in-touch fields, one per person
    col_gap = 30
    col_w = (F.CW - col_gap) / 2
    for i, col_title in enumerate(("YOU", "YOUR NEW FRIEND")):
        x0 = F.M + i * (col_w + col_gap)
        F.tracked_text(c, x0, F.ty(y + 10), col_title, "Nunito-Bold", 11, 2.4)
        yy = y + 52
        for field in C.CLOSING_FIELDS:
            F.plain_text(c, x0, F.ty(yy), field, "Nunito-XLI", 12, F.INK)
            c.setStrokeColorRGB(*F.rgb(F.INK))
            c.setLineWidth(F.RULE_W)
            c.line(x0, F.ty(yy + 30), x0 + col_w, F.ty(yy + 30))
            yy += 64

    F.plain_text(c, F.PAGE_W / 2, F.ty(640), C.CLOSING_STATS, "Nunito-Bold",
                 13, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(668), "M A Y B E W E L L   B O O K S",
                 "Nunito-Bold", 11, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(688), C.CFG["TAGLINE"], "Nunito-XL",
                 11, F.INK, center=True)
    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def main():
    F.register_fonts()
    out = os.path.abspath(OUT_PATH)
    cfg = dict(C.CFG)
    cfg["icon_fn"] = lambda c: icon_chairs(c, y_top=486)
    cfg["icon_fn_small"] = lambda c: icon_chairs(c, y_top=476, scale=0.62)

    c = F.start_canvas(out, "Tell Someone New — Thirty Questions for the "
                            "Newest Person in the Room",
                       "A large-print icebreaker book for new residents in a "
                       "care community: 30 paired questions ordered from "
                       "light to personal, both people answer every page.")
    F.cover_page(c, cfg)
    F.title_page(c, cfg)
    F.intro_page(c, cfg, C.INTRO_KICKER, C.INTRO_TITLE, C.INTRO_PARAS, 3)

    page = 4
    for i, q in enumerate(C.QUESTIONS, start=1):
        question_page(c, i, q, page)
        page += 1

    closing_page(c, page)
    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
