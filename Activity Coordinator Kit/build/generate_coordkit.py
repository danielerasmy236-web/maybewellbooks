"""Generate the Activity Coordinator Kit (letter PDF). For Every Chapter
line. Template G: facilitator guide — five activities x (overview page +
adaptations page), photocopiable weekly planning grids, closing.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "For Every Chapter", "build"))

import fec_lib as F
import content_coordkit as C

OUT_PATH = os.path.join(HERE, "..", "activity-coordinator-kit_v1.0_letter.pdf")


def icon_clipboard(c, cx=None, y_top=500, scale=1.0):
    """Cover icon: a clipboard with an ochre clip and ticked lines."""
    cx = cx if cx is not None else F.PAGE_W / 2
    w, h = 86 * scale, 110 * scale
    x0 = cx - w / 2
    y1 = F.ty(y_top)
    y0 = y1 - h

    c.setFillColorRGB(*F.rgb(F.PUTTY))
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(2.6 * scale)
    c.roundRect(x0, y0, w, h, 6 * scale, fill=1, stroke=1)

    c.setFillColorRGB(*F.rgb(F.OCHRE))
    c.roundRect(cx - 16 * scale, y0 + h - 8 * scale, 32 * scale, 14 * scale,
                4 * scale, fill=1, stroke=0)

    c.setLineWidth(2.0 * scale)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    for i in range(4):
        yy = y0 + h * 0.68 - i * 18 * scale
        # tick
        c.line(x0 + 12 * scale, yy, x0 + 17 * scale, yy - 5 * scale)
        c.line(x0 + 17 * scale, yy - 5 * scale, x0 + 25 * scale, yy + 6 * scale)
        # item line
        c.line(x0 + 33 * scale, yy, x0 + w - 12 * scale, yy)


def overview_page(c, act, page_num):
    (name, kicker, overview, size, time, materials, steps, _adapt, _var) = act
    F.tracked_text(c, F.M, F.ty(62), kicker, "Nunito-Bold", 11, 2.0)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    y = 112
    for ln in F.wrap(name, "Fraunces-Black", 24, F.CW):
        F.plain_text(c, F.M, F.ty(y), ln, "Fraunces-Black", 24)
        y += 30
    y += 4
    for ln in F.wrap(overview, "Nunito-Reg", 13, F.CW):
        F.plain_text(c, F.M, F.ty(y), ln, "Nunito-Reg", 13)
        y += 19
    y += 10

    # facts row
    facts = [("GROUP", size), ("TIME", time)]
    x = F.M
    for label, val in facts:
        F.tracked_text(c, x, F.ty(y), label, "Nunito-Bold", 10, 2.0)
        F.plain_text(c, x, F.ty(y + 19), val, "Nunito-Reg", 12.5)
        x += 168
    y += 46
    F.tracked_text(c, F.M, F.ty(y), "MATERIALS", "Nunito-Bold", 10, 2.0)
    yy = y + 19
    for ln in F.wrap(materials, "Nunito-Reg", 12.5, F.CW):
        F.plain_text(c, F.M, F.ty(yy), ln, "Nunito-Reg", 12.5)
        yy += 18
    y = yy + 14

    F.tracked_text(c, F.M, F.ty(y), "HOW TO RUN IT", "Nunito-Bold", 11, 2.4)
    y += 28
    for i, step in enumerate(steps, start=1):
        F.plain_text(c, F.M, F.ty(y), f"{i}.", "Fraunces-SemiBold", 14, F.INK)
        for ln in F.wrap(step, "Nunito-Reg", 13, F.CW - 30):
            F.plain_text(c, F.M + 30, F.ty(y), ln, "Nunito-Reg", 13)
            y += 19
        y += 7

    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def adaptations_page(c, act, page_num):
    (name, kicker, _o, _s, _t, _m, _steps, adapt, variation) = act
    F.tracked_text(c, F.M, F.ty(62), kicker + " · ADAPTATIONS",
                   "Nunito-Bold", 11, 2.0)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    F.plain_text(c, F.M, F.ty(112), "Everyone plays.", "Fraunces-Black", 24)
    F.plain_text(c, F.M, F.ty(140),
                 "Adjustments so the whole room can join — not just the "
                 "healthiest half.", "Nunito-XLI", 12.5)

    y = 180
    for label, text in adapt:
        F.tracked_text(c, F.M, F.ty(y), label, "Nunito-Bold", 11, 2.4)
        c.setFillColorRGB(*F.rgb(F.OCHRE))
        c.circle(F.M - 10, F.ty(y - 4), 3, fill=1, stroke=0)
        yy = y + 24
        for ln in F.wrap(text, "Nunito-Reg", 13, F.CW):
            F.plain_text(c, F.M, F.ty(yy), ln, "Nunito-Reg", 13)
            yy += 19
        y = yy + 18

    y += 6
    c.setStrokeColorRGB(*F.rgb(F.OCHRE))
    c.setLineWidth(1.4)
    c.line(F.M, F.ty(y), F.M + 130, F.ty(y))
    y += 26
    for ln in F.wrap(variation, "Nunito-XLI", 12.5, F.CW):
        F.plain_text(c, F.M, F.ty(y), ln, "Nunito-XLI", 12.5)
        y += 18

    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def planner_page(c, page_num):
    F.tracked_text(c, F.M, F.ty(62), "WEEKLY PLANNER · PHOTOCOPY FREELY",
                   "Nunito-Bold", 11, 2.0)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    F.plain_text(c, F.M, F.ty(112), C.PLANNER_TITLE, "Fraunces-Black", 24)
    y = 140
    for ln in F.wrap(C.PLANNER_NOTE, "Nunito-XLI", 12, F.CW):
        F.plain_text(c, F.M, F.ty(y), ln, "Nunito-XLI", 12)
        y += 17

    # grid: rows = days, columns = ACTIVITY / TIME / ROOM
    top = y + 20
    row_h = 66.0
    col_x = [F.M, F.M + 118, F.M + 328, F.M + 424, F.PAGE_W - F.M]

    # header row
    hdr_y = top + 20
    for i, col in enumerate(["", *C.PLANNER_COLS]):
        if col:
            F.tracked_text(c, col_x[i] + 8, F.ty(top + 16), col,
                           "Nunito-Bold", 10, 2.0)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(1.8)
    c.line(F.M, F.ty(top + 26), F.PAGE_W - F.M, F.ty(top + 26))

    yy = top + 26
    for day in C.PLANNER_DAYS:
        F.plain_text(c, F.M + 8, F.ty(yy + 38), day, "Fraunces-SemiBold",
                     13, F.INK)
        c.setLineWidth(F.RULE_W)
        c.line(F.M, F.ty(yy + row_h), F.PAGE_W - F.M, F.ty(yy + row_h))
        yy += row_h
    # verticals
    c.setLineWidth(F.RULE_W)
    for x in col_x[1:-1]:
        c.line(x, F.ty(top + 26), x, F.ty(yy))
    c.setLineWidth(1.8)
    c.rect(F.M, F.ty(yy), F.CW, yy - top - 26 + row_h * 0, fill=0, stroke=0)

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
    icon_clipboard(c, y_top=470, scale=0.62)
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
    cfg["icon_fn"] = lambda c: icon_clipboard(c, y_top=498)
    cfg["icon_fn_small"] = lambda c: icon_clipboard(c, y_top=486, scale=0.62)

    c = F.start_canvas(out, "Activity Coordinator Kit — Five Group "
                            "Activities, One Kit, a Whole Calendar",
                       "The institutional facilitator guide for the For "
                       "Every Chapter line: five senior-center group "
                       "activities with adaptation notes and a "
                       "photocopiable weekly planner.")
    F.cover_page(c, cfg)
    F.title_page(c, cfg)
    F.intro_page(c, cfg, C.INTRO_KICKER, C.INTRO_TITLE, C.INTRO_PARAS, 3)

    page = 4
    for act in C.ACTIVITIES:
        overview_page(c, act, page)
        page += 1
        adaptations_page(c, act, page)
        page += 1

    planner_page(c, page)
    page += 1
    planner_page(c, page)
    page += 1

    closing_page(c, page)
    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
