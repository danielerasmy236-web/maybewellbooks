"""Generate Trivia by Decade (letter PDF). For Every Chapter line.

Template B: 4 decade sections x 15 questions, 3 questions per page with
large-print answer lines, full answer-notes section at the back.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "For Every Chapter", "build"))

import fec_lib as F
import content_trivia as C

OUT_PATH = os.path.join(HERE, "..", "trivia-by-decade_v1.0_letter.pdf")


def icon_radio(c, cx=None, y_top=500, scale=1.0):
    """Cover icon: a tabletop radio — rounded cabinet, ochre dial, speaker
    slats — the object every one of these decades gathered around."""
    cx = cx if cx is not None else F.PAGE_W / 2
    w, h = 118 * scale, 84 * scale
    x0 = cx - w / 2
    y1 = F.ty(y_top)
    y0 = y1 - h

    c.setFillColorRGB(*F.rgb(F.PUTTY))
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(2.6 * scale)
    c.roundRect(x0, y0, w, h, 12 * scale, fill=1, stroke=1)

    # dial
    c.setFillColorRGB(*F.rgb(F.OCHRE))
    c.circle(x0 + w * 0.3, y0 + h * 0.52, 16 * scale, fill=1, stroke=0)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(1.6 * scale)
    c.circle(x0 + w * 0.3, y0 + h * 0.52, 16 * scale, fill=0, stroke=1)
    c.line(x0 + w * 0.3, y0 + h * 0.52,
           x0 + w * 0.3 + 10 * scale, y0 + h * 0.62)

    # speaker slats
    c.setLineWidth(2.2 * scale)
    for i in range(4):
        xx = x0 + w * 0.56 + i * 9 * scale
        c.line(xx, y0 + h * 0.3, xx, y0 + h * 0.74)

    # feet
    c.setFillColorRGB(*F.rgb(F.INK))
    c.rect(x0 + w * 0.14, y0 - 5 * scale, w * 0.12, 5 * scale, fill=1, stroke=0)
    c.rect(x0 + w * 0.74, y0 - 5 * scale, w * 0.12, 5 * scale, fill=1, stroke=0)


def question_block(c, q_no, question, y):
    F.plain_text(c, F.M, F.ty(y), f"{q_no:02d}", "Fraunces-SemiBold", 15, F.INK)
    yy = y
    for ln in F.wrap(question, "Fraunces-SemiBold", 16, F.CW - 40):
        F.plain_text(c, F.M + 40, F.ty(yy), ln, "Fraunces-SemiBold", 16)
        yy += 23
    F.ruled_lines(c, yy + 14, yy + 44, x0=F.M + 40)
    return yy + 78


def notes_page(c, decade_title, notes, start_no, page_num):
    F.tracked_text(c, F.M, F.ty(62), "ANSWER NOTES", "Nunito-Bold", 11, 2.0)
    F.plain_text(c, F.PAGE_W - F.M, F.ty(62), decade_title,
                 "Fraunces-SemiBold", 13, F.INK, right=True)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    y = 106
    for i, note in enumerate(notes):
        F.plain_text(c, F.M, F.ty(y), f"{start_no + i:02d}", "Nunito-Bold",
                     12.5, F.INK)
        for ln in F.wrap(note, "Nunito-Reg", 12.5, F.CW - 40):
            F.plain_text(c, F.M + 40, F.ty(y), ln, "Nunito-Reg", 12.5)
            y += 18
        y += 8

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
    icon_radio(c, y_top=470, scale=0.62)
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
    cfg["icon_fn"] = lambda c: icon_radio(c, y_top=500)
    cfg["icon_fn_small"] = lambda c: icon_radio(c, y_top=488, scale=0.62)

    c = F.start_canvas(out, "Trivia by Decade — Sixty Questions That Reward "
                            "Having Actually Been There",
                       "Large-print trivia organized by decade (1950s-1980s), "
                       "rewarding lived memory over textbook answers, with "
                       "answer notes for discussion.")
    F.cover_page(c, cfg)
    F.title_page(c, cfg)
    F.intro_page(c, cfg, C.INTRO_KICKER, C.INTRO_TITLE, C.INTRO_PARAS, 3)

    page = 4
    q_no = 0
    for idx, (title, note, questions) in enumerate(C.SECTIONS):
        F.divider_page(c, f"SECTION {F.NUM_WORDS[idx]}  ·  15 QUESTIONS",
                       title, note)
        page += 1
        for i in range(0, len(questions), 3):
            F.tracked_text(c, F.M, F.ty(62), title.upper(), "Nunito-Bold", 11, 2.0)
            F.plain_text(c, F.PAGE_W - F.M, F.ty(62),
                         f"Questions {q_no + 1:02d}-{q_no + len(questions[i:i+3]):02d}",
                         "Fraunces-SemiBold", 13, F.INK, right=True)
            c.setStrokeColorRGB(*F.rgb(F.INK))
            c.setLineWidth(F.RULE_W)
            c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))
            y = 116
            for q in questions[i:i + 3]:
                q_no += 1
                y = question_block(c, q_no, q, y)
            F.footer(c, page, C.CFG["TAGLINE"])
            c.showPage()
            page += 1

    F.divider_page(c, "AT THE BACK", "Answer Notes",
                   "What most people say — argue with all of it.")
    page += 1
    start = 1
    for (title, _, questions), notes in zip(C.SECTIONS, C.ANSWER_NOTES):
        mid = 8
        notes_page(c, title, notes[:mid], start, page)
        page += 1
        notes_page(c, title, notes[mid:], start + mid, page)
        page += 1
        start += len(questions)

    closing_page(c, page)
    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
