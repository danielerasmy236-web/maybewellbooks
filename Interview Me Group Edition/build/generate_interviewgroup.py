"""Generate Interview Me — Group Edition (letter PDF). For Every Chapter line.

Template E adapted for group use: facilitator strip at the top of every
question page (suggested phrasing + the comparison prompt), the question in
large print, then three side-by-side answer columns.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "For Every Chapter", "build"))

import fec_lib as F
import content_interviewgroup as C

OUT_PATH = os.path.join(HERE, "..", "interview-me-group-edition_v1.0_letter.pdf")


def icon_group(c, cx=None, y_top=500, scale=1.0):
    """Cover icon: three heads in a row with one shared speech bubble."""
    cx = cx if cx is not None else F.PAGE_W / 2
    r = 13 * scale
    gap = 40 * scale
    base = F.ty(y_top + 84 * scale)

    for i, dx in enumerate((-gap, 0, gap)):
        c.setFillColorRGB(*F.rgb(F.INK))
        c.circle(cx + dx, base + 34 * scale, r, fill=1, stroke=0)
        p = c.beginPath()
        p.moveTo(cx + dx - 17 * scale, base)
        p.curveTo(cx + dx - 17 * scale, base + 22 * scale,
                  cx + dx + 17 * scale, base + 22 * scale,
                  cx + dx + 17 * scale, base)
        p.close()
        c.drawPath(p, fill=1, stroke=0)

    # shared speech bubble above, ochre
    bw, bh = 74 * scale, 30 * scale
    bx, by = cx - bw / 2, base + 56 * scale
    c.setFillColorRGB(*F.rgb(F.OCHRE))
    c.roundRect(bx, by, bw, bh, 10 * scale, fill=1, stroke=0)
    p = c.beginPath()
    p.moveTo(cx - 8 * scale, by)
    p.lineTo(cx, by - 12 * scale)
    p.lineTo(cx + 8 * scale, by)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def question_page(c, section_title, facilitator_hint, q_no, question, page_num):
    # facilitator strip
    F.tracked_text(c, F.M, F.ty(62), "FACILITATOR", "Nunito-Bold", 11, 2.0)
    F.plain_text(c, F.PAGE_W - F.M, F.ty(62), f"No. {q_no:02d}",
                 "Fraunces-SemiBold", 13, F.INK, right=True)
    y = 84
    for ln in F.wrap(facilitator_hint + "  " + C.COMPARE_PROMPT,
                     "Nunito-XLI", 12, F.CW):
        F.plain_text(c, F.M, F.ty(y), ln, "Nunito-XLI", 12)
        y += 17
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(y + 4), F.PAGE_W - F.M, F.ty(y + 4))

    # the question, read-aloud large
    F.tracked_text(c, F.M, F.ty(y + 34), section_title.upper(),
                   "Nunito-Bold", 11, 2.0)
    yy = y + 66
    for ln in F.wrap(question, "Fraunces-SemiBold", 21, F.CW):
        F.plain_text(c, F.M, F.ty(yy), ln, "Fraunces-SemiBold", 21)
        yy += 29

    # three answer columns
    col_gap = 18
    col_w = (F.CW - 2 * col_gap) / 3
    top = max(yy + 26, 268)
    for i in range(3):
        x0 = F.M + i * (col_w + col_gap)
        F.tracked_text(c, x0, F.ty(top), "NAME", "Nunito-Bold", 10, 2.0)
        c.setStrokeColorRGB(*F.rgb(F.INK))
        c.setLineWidth(F.RULE_W)
        c.line(x0 + 44, F.ty(top + 2), x0 + col_w, F.ty(top + 2))
        F.ruled_lines(c, top + 40, 700, x0=x0, x1=x0 + col_w)

    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def closing_page(c, page_num):
    F.putty_bg(c)
    F.plain_text(c, F.PAGE_W / 2, F.ty(300), C.CLOSING_TITLE,
                 "Fraunces-Black", 26, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(346), C.CLOSING_BODY, "Nunito-Reg",
                 14.5, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(412), C.CLOSING_STATS, "Nunito-Bold",
                 13, F.INK, center=True)
    icon_group(c, y_top=470, scale=0.62)
    F.plain_text(c, F.PAGE_W / 2, F.ty(660), "M A Y B E W E L L   B O O K S",
                 "Nunito-Bold", 11, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(682), C.CFG["TAGLINE"], "Nunito-XL",
                 11, F.INK, center=True)
    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def main():
    F.register_fonts()
    out = os.path.abspath(OUT_PATH)
    cfg = dict(C.CFG)
    cfg["icon_fn"] = lambda c: icon_group(c, y_top=488)
    cfg["icon_fn_small"] = lambda c: icon_group(c, y_top=478, scale=0.62)

    c = F.start_canvas(out, "Interview Me — Group Edition — One Question, a "
                            "Room Full of Answers",
                       "A large-print, facilitator-led group interview book: "
                       "40 questions with three side-by-side answer columns "
                       "per page so a group can compare answers aloud.")
    F.cover_page(c, cfg)
    F.title_page(c, cfg)
    F.intro_page(c, cfg, C.INTRO_KICKER, C.INTRO_TITLE, C.INTRO_PARAS, 3)

    page = 4
    q_no = 0
    for idx, (title, note, hint, questions) in enumerate(C.SECTIONS):
        F.divider_page(c, f"SECTION {F.NUM_WORDS[idx]}  ·  "
                          f"{len(questions)} QUESTIONS", title, note)
        page += 1
        for q in questions:
            q_no += 1
            question_page(c, title, hint, q_no, q, page)
            page += 1

    closing_page(c, page)
    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
