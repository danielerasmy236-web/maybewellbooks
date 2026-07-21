"""Generate One Photo, One Story (letter PDF). For Every Chapter line.

Template F adapted for photo-anchoring: each card page has a dashed
photo-mounting box with classic album corner guides, four anchor prompt
fields, a rotating deeper prompt, and large-print ruled writing lines.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "For Every Chapter", "build"))

import fec_lib as F
import content_photostory as C

OUT_PATH = os.path.join(HERE, "..", "one-photo-one-story_v1.0_letter.pdf")


def icon_photo(c, cx=None, y_top=500, scale=1.0):
    """Cover icon: a mounted photograph (dashed corners echo) with a sun
    and hill inside — putty fill, ink stroke, ochre nameplate."""
    cx = cx if cx is not None else F.PAGE_W / 2
    w, h = 120 * scale, 96 * scale
    x0 = cx - w / 2
    y1 = F.ty(y_top)
    y0 = y1 - h

    c.setFillColorRGB(*F.rgb(F.PUTTY))
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(2.6 * scale)
    c.rect(x0, y0, w, h, fill=1, stroke=1)

    # sun + hills inside
    c.setFillColorRGB(*F.rgb(F.OCHRE))
    c.circle(x0 + w * 0.72, y0 + h * 0.68, 11 * scale, fill=1, stroke=0)
    c.setFillColorRGB(*F.rgb(F.INK))
    p = c.beginPath()
    p.moveTo(x0 + 3, y0 + 3)
    p.lineTo(x0 + w * 0.38, y0 + h * 0.52)
    p.lineTo(x0 + w * 0.62, y0 + h * 0.24)
    p.lineTo(x0 + w * 0.9, y0 + h * 0.5)
    p.lineTo(x0 + w - 3, y0 + 3)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # album corner mounts
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(2.2 * scale)
    g = 10 * scale
    for corner_x, sx in ((x0 - 5, 1), (x0 + w + 5, -1)):
        for corner_y, sy in ((y0 - 5, 1), (y0 + h + 5, -1)):
            c.line(corner_x, corner_y, corner_x + sx * g, corner_y)
            c.line(corner_x, corner_y, corner_x, corner_y + sy * g)


def card_page(c, no, deep_prompt, page_num):
    F.tracked_text(c, F.M, F.ty(62), "ONE PHOTO, ONE STORY", "Nunito-Bold", 11, 2.0)
    F.plain_text(c, F.PAGE_W - F.M, F.ty(62), f"Photo No. {no:02d}",
                 "Fraunces-SemiBold", 13, F.INK, right=True)
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(F.RULE_W)
    c.line(F.M, F.ty(76), F.PAGE_W - F.M, F.ty(76))

    # ---- photo mounting area: dashed box + corner guides
    box_top, box_bot = 96.0, 306.0
    x0, x1 = F.M, F.PAGE_W - F.M
    c.setStrokeColorRGB(*F.rgb(F.INK))
    c.setLineWidth(1.2)
    c.setDash(6, 4)
    c.rect(x0, F.ty(box_bot), x1 - x0, box_bot - box_top, fill=0, stroke=1)
    c.setDash()

    # classic album corner-mount guides (solid L brackets, thick for tremor)
    c.setLineWidth(2.4)
    g = 20
    inset = 10
    for cx_, sx in ((x0 + inset, 1), (x1 - inset, -1)):
        for cy_, sy in ((F.ty(box_top + inset), -1), (F.ty(box_bot - inset), 1)):
            c.line(cx_, cy_, cx_ + sx * g, cy_)
            c.line(cx_, cy_, cx_, cy_ + sy * g)

    F.plain_text(c, F.PAGE_W / 2, F.ty((box_top + box_bot) / 2),
                 "Tape or glue a photo here.", "Nunito-XLI", 12.5, F.INK,
                 center=True)

    # ---- anchor prompt fields
    y = 342
    F.tracked_text(c, F.M, F.ty(y), "WHO'S IN THIS PHOTO?", "Nunito-Bold", 11, 2.0)
    F.ruled_lines(c, y + 26, y + 26)
    y += 66
    F.tracked_text(c, F.M, F.ty(y), "GUESS THE YEAR.", "Nunito-Bold", 11, 2.0)
    F.ruled_lines(c, y + 26, y + 26, x0=F.M, x1=F.M + 150)
    F.tracked_text(c, F.M + 186, F.ty(y), "WHERE WAS THIS TAKEN?",
                   "Nunito-Bold", 11, 2.0)
    F.ruled_lines(c, y + 26, y + 26, x0=F.M + 186, x1=F.PAGE_W - F.M)
    y += 66
    F.tracked_text(c, F.M, F.ty(y),
                   "WHAT WAS HAPPENING JUST BEFORE OR AFTER THIS WAS TAKEN?",
                   "Nunito-Bold", 11, 2.0)
    F.ruled_lines(c, y + 26, y + 56)
    y += 96

    # ---- rotating deeper prompt + writing area
    F.tracked_text(c, F.M, F.ty(y), "AND THE STORY —", "Nunito-Bold", 11, 2.4)
    yy = y + 26
    for ln in F.wrap(deep_prompt, "Fraunces-SemiBold", 15, F.CW):
        F.plain_text(c, F.M, F.ty(yy), ln, "Fraunces-SemiBold", 15)
        yy += 21
    F.ruled_lines(c, yy + 16, 706)

    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def closing_page(c, page_num):
    F.putty_bg(c)
    F.plain_text(c, F.PAGE_W / 2, F.ty(280), C.CLOSING_TITLE,
                 "Fraunces-Black", 28, F.INK, center=True)
    y = 330
    for para in C.CLOSING_PARAS:
        for ln in F.wrap(para, "Nunito-Reg", 14.5, F.CW - 80):
            F.plain_text(c, F.PAGE_W / 2, F.ty(y), ln, "Nunito-Reg", 14.5,
                         F.INK, center=True)
            y += 22
        y += 10
    F.plain_text(c, F.PAGE_W / 2, F.ty(y + 16), C.CLOSING_STATS,
                 "Nunito-Bold", 13, F.INK, center=True)
    icon_photo(c, y_top=y + 60, scale=0.62)
    F.plain_text(c, F.PAGE_W / 2, F.ty(660), "M A Y B E W E L L   B O O K S",
                 "Nunito-Bold", 11, F.INK, center=True)
    F.plain_text(c, F.PAGE_W / 2, F.ty(682), C.CFG["TAGLINE"],
                 "Nunito-XL", 11, F.INK, center=True)
    F.footer(c, page_num, C.CFG["TAGLINE"])
    c.showPage()


def main():
    F.register_fonts()
    out = os.path.abspath(OUT_PATH)
    cfg = dict(C.CFG)
    cfg["icon_fn"] = lambda c: icon_photo(c, y_top=500)
    cfg["icon_fn_small"] = lambda c: icon_photo(c, y_top=488, scale=0.62)

    c = F.start_canvas(out, "One Photo, One Story — The Stories Behind the "
                            "Photographs You Already Have",
                       "A large-print photo keepsake book: mount 30 photos "
                       "and write the story behind each one.")
    F.cover_page(c, cfg)
    F.title_page(c, cfg)
    F.intro_page(c, cfg, C.INTRO_KICKER, C.INTRO_TITLE, C.INTRO_PARAS, 3)
    page = 4
    for i in range(C.CARD_COUNT):
        card_page(c, i + 1, C.DEEP_PROMPTS[i % len(C.DEEP_PROMPTS)], page)
        page += 1
    closing_page(c, page)
    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
