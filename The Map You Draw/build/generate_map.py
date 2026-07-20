"""Generate The Map You Draw — A Personal Atlas of Everywhere You Actually Go
(letter PDF).

Field Notes line, Volume Three. Reuses the DWYI/TWIW/Wander production
pipeline: Fraunces (titles) + Nunito (body) static instances, ReportLab
canvas, vector icons only (no emoji glyphs).

Structural departure from Template B: no sections, no divider pages — one
continuous 36-page personal atlas. Each atlas page carries a single
marginalia prompt ("MARK") above a large blank map canvas.

Tc discipline: every tracked (letterspaced) string goes through
tracked_text(), which sets charSpace and always resets it to 0 inside the
same text object.
"""

import math
import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as _canvas

import content_map as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_PATH = os.path.join(HERE, "..", "the-map-you-draw_v1.0_letter.pdf")

PAGE_W, PAGE_H = letter  # 612 x 792
M = 54.0
CW = PAGE_W - 2 * M

INK = "#20303A"
PUTTY = "#F3EEE6"
OCHRE = "#D99A2B"

FONTS = {
    "Fraunces-Black": "Fraunces-9ptBlack.ttf",
    "Fraunces-SemiBold": "Fraunces-SemiBold.ttf",
    "Nunito-XL": "Nunito-ExtraLight.ttf",
    "Nunito-XLI": "Nunito-ExtraLightItalic.ttf",
    "Nunito-Reg": "Nunito-Regular.ttf",
    "Nunito-Bold": "Nunito-Bold.ttf",
}


def rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def ty(y_top):
    return PAGE_H - y_top


def register_fonts():
    for name, fn in FONTS.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))


def tracked_width(text, font, size, track):
    return pdfmetrics.stringWidth(text, font, size) + track * max(len(text) - 1, 0)


def tracked_text(c, x, y, text, font, size, track, color, center=False):
    if center:
        x = x - tracked_width(text, font, size, track) / 2
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColorRGB(*rgb(color))
    t.setCharSpace(track)
    t.textOut(text)
    t.setCharSpace(0)
    c.drawText(t)


def plain_text(c, x, y, text, font, size, color, right=False, center=False):
    c.setFont(font, size)
    c.setFillColorRGB(*rgb(color))
    if right:
        c.drawRightString(x, y, text)
    elif center:
        c.drawCentredString(x, y, text)
    else:
        c.drawString(x, y, text)


def wrap(text, font, size, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(trial, font, size) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- vector bits

def draw_star(c, cx, cy, r, filled):
    pts = []
    for i in range(10):
        ang = math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    p = c.beginPath()
    p.moveTo(*pts[0])
    for pt in pts[1:]:
        p.lineTo(*pt)
    p.close()
    if filled:
        c.setFillColorRGB(*rgb(OCHRE))
        c.drawPath(p, fill=1, stroke=0)
    else:
        c.setStrokeColorRGB(*rgb(INK))
        c.setLineWidth(0.9)
        c.drawPath(p, fill=0, stroke=1)


def draw_infinity(c, cx, cy, r=5.5):
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.4)
    c.circle(cx - r + 1, cy, r, fill=0, stroke=1)
    c.circle(cx + r - 1, cy, r, fill=0, stroke=1)


def footer(c, page_num):
    c.setFillColorRGB(*rgb(OCHRE))
    c.circle(M + 2, ty(745), 2, fill=1, stroke=0)
    plain_text(c, M + 10, ty(747), C.TAGLINE, "Nunito-XL", 8, INK)
    plain_text(c, PAGE_W - M, ty(747), str(page_num), "Nunito-Reg", 8, INK, right=True)


def putty_bg(c):
    c.setFillColorRGB(*rgb(PUTTY))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_folded_map(c, cx, y_top, scale=1.0):
    """The cover/closing icon: a folded paper map with a dashed route and an
    ochre X marking the spot — the visual shorthand for personal cartography.
    """
    w, h = 108 * scale, 132 * scale
    x0 = cx - w / 2
    y1 = ty(y_top)
    y0 = y1 - h

    c.setFillColorRGB(*rgb(PUTTY))
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2.2 * scale)
    c.rect(x0, y0, w, h, fill=1, stroke=1)

    # fold lines
    c.setLineWidth(1 * scale)
    c.setDash(3, 3)
    c.line(x0 + w / 3, y0, x0 + w / 3, y1)
    c.line(x0 + 2 * w / 3, y0, x0 + 2 * w / 3, y1)
    c.setDash()

    # dashed route from bottom-left toward the X
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.3 * scale)
    c.setDash(4, 3)
    p = c.beginPath()
    p.moveTo(x0 + 14 * scale, y0 + 20 * scale)
    p.curveTo(x0 + 40 * scale, y0 + 50 * scale,
              x0 + 55 * scale, y0 + 70 * scale,
              x0 + 78 * scale, y0 + 100 * scale)
    c.drawPath(p, fill=0, stroke=1)
    c.setDash()

    # start pin
    c.setFillColorRGB(*rgb(INK))
    c.circle(x0 + 14 * scale, y0 + 20 * scale, 3 * scale, fill=1, stroke=0)

    # ochre X marks the spot
    xs, ys = x0 + 78 * scale, y0 + 100 * scale
    r = 7 * scale
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(2.6 * scale)
    c.line(xs - r, ys - r, xs + r, ys + r)
    c.line(xs - r, ys + r, xs + r, ys - r)


# --------------------------------------------------------------------- pages

def cover(c):
    putty_bg(c)
    wm = "M A Y B E W E L L   B O O K S"
    plain_text(c, PAGE_W / 2, ty(74), wm, "Nunito-Bold", 13, INK, center=True)
    wm_w = pdfmetrics.stringWidth(wm, "Nunito-Bold", 13)
    draw_star(c, PAGE_W / 2 + wm_w / 2 + 15, ty(70), 5.5, True)

    tracked_text(c, PAGE_W / 2, ty(227), C.EYEBROW, "Nunito-Bold", 11, 2.4,
                 OCHRE, center=True)

    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", 56)
    c.drawCentredString(PAGE_W / 2, ty(304), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(365), C.TITLE_LINES[1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(405), 96, 3, fill=1, stroke=0)

    plain_text(c, PAGE_W / 2, ty(438), C.SUBTITLE, "Nunito-XLI", 15, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(460), C.SPANISH_NOTE, "Nunito-XLI", 12, INK, center=True)

    draw_folded_map(c, PAGE_W / 2, 500)

    badge_w = tracked_width(C.BADGE, "Nunito-Bold", 10, 1.2) + 36
    c.setFillColorRGB(*rgb(OCHRE))
    c.roundRect(PAGE_W / 2 - badge_w / 2, ty(686), badge_w, 22, 11, fill=1, stroke=0)
    tracked_text(c, PAGE_W / 2, ty(679), C.BADGE, "Nunito-Bold", 10, 1.2,
                 PUTTY, center=True)

    plain_text(c, PAGE_W / 2, ty(720), C.TAGLINE, "Nunito-XL", 11, INK, center=True)
    tracked_text(c, PAGE_W / 2, ty(755), "maybewellbooks.com", "Nunito-XL", 9,
                 0.54, INK, center=True)
    c.showPage()


def title_page(c):
    putty_bg(c)
    plain_text(c, PAGE_W / 2, ty(120), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 11, INK, center=True)
    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", 36)
    c.drawCentredString(PAGE_W / 2, ty(328), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(370), C.TITLE_LINES[1])
    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 40, ty(398), 80, 2.5, fill=1, stroke=0)
    plain_text(c, PAGE_W / 2, ty(426), C.SUBTITLE, "Nunito-XLI", 13, INK, center=True)
    draw_folded_map(c, PAGE_W / 2, 488, scale=0.62)
    plain_text(c, PAGE_W / 2, ty(660), "it only has to make sense to you.",
               "Nunito-XL", 12, INK, center=True)
    c.showPage()


def intro_page(c, page_num):
    tracked_text(c, M, ty(66), C.INTRO_KICKER, "Nunito-Bold", 10, 2.4, OCHRE)
    plain_text(c, M, ty(102), C.INTRO_TITLE, "Fraunces-Black", 24, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(120), PAGE_W - M, ty(120))

    y = 152
    for item in C.INTRO_PARAS:
        if isinstance(item, tuple):
            label, body = item
            tracked_text(c, M, ty(y), label, "Nunito-Bold", 10, 2.4, OCHRE)
            lines = wrap(body, "Nunito-Reg", 11.5, CW - 64)
            yy = y
            for ln in lines:
                plain_text(c, M + 64, ty(yy), ln, "Nunito-Reg", 11.5, INK)
                yy += 17
            y = yy + 9
        else:
            for ln in wrap(item, "Nunito-Reg", 11.5, CW):
                plain_text(c, M, ty(y), ln, "Nunito-Reg", 11.5, INK)
                y += 17
            y += 9

    footer(c, page_num)
    c.showPage()


def atlas_page(c, mark_no, prompt, page_num):
    # header
    tracked_text(c, M, ty(60), "PERSONAL ATLAS", "Nunito-Bold", 10, 2.0, OCHRE)
    plain_text(c, PAGE_W - M, ty(60), f"No. {mark_no:02d}", "Fraunces-SemiBold",
               12, INK, right=True)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(72), PAGE_W - M, ty(72))

    # MARK
    tracked_text(c, M, ty(108), "MARK", "Nunito-Bold", 10, 2.4, OCHRE)
    y = 138
    for ln in wrap(prompt, "Fraunces-SemiBold", 18, CW - 130):
        plain_text(c, M, ty(y), ln, "Fraunces-SemiBold", 18, INK)
        y += 25

    label_w = pdfmetrics.stringWidth("Visited:", "Nunito-Reg", 10)
    label_x = PAGE_W - M - 100 - label_w
    plain_text(c, label_x, ty(112), "Visited:", "Nunito-Reg", 10, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.7)
    c.line(label_x + label_w + 8, ty(115), PAGE_W - M, ty(115))

    box_top = max(y + 14, 172)
    box_bottom = 706
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.setDash(4, 4)
    c.roundRect(M, ty(box_bottom), CW, box_bottom - box_top, 10, fill=0, stroke=1)
    c.setDash()

    footer(c, page_num)
    c.showPage()


def closing_page(c, page_num):
    putty_bg(c)
    plain_text(c, PAGE_W / 2, ty(300), C.CLOSING_TITLE, "Fraunces-Black", 25,
               INK, center=True)
    plain_text(c, PAGE_W / 2, ty(345), C.CLOSING_BODY, "Nunito-Reg", 13, INK,
               center=True)

    stats_w = pdfmetrics.stringWidth(C.CLOSING_STATS, "Nunito-Bold", 12)
    plain_text(c, PAGE_W / 2 - 10, ty(410), C.CLOSING_STATS, "Nunito-Bold", 12,
               INK, center=True)
    draw_infinity(c, PAGE_W / 2 - 10 + stats_w / 2 + 16, ty(406))

    plain_text(c, PAGE_W / 2, ty(455), C.CLOSING_SHARE, "Nunito-XLI", 12, INK,
               center=True)

    draw_folded_map(c, PAGE_W / 2, 500, scale=0.5)

    plain_text(c, PAGE_W / 2, ty(660), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 10, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(682), "it only has to make sense to you.",
               "Nunito-XL", 10, INK, center=True)
    footer(c, page_num)
    c.showPage()


def main():
    register_fonts()
    out = os.path.abspath(OUT_PATH)
    c = _canvas.Canvas(out, pagesize=letter)
    c.setTitle("The Map You Draw — A Personal Atlas of Everywhere You Actually Go")
    c.setAuthor("Maybewell Books")
    c.setSubject("A continuous personal-atlas activity book: 36 marginalia prompts guiding a hand-drawn map of your own neighborhood, built to be revisited over time.")
    c.setCreator("anonymous")

    cover(c)               # p1
    title_page(c)           # p2
    intro_page(c, 3)         # p3
    page = 4
    for i, prompt in enumerate(C.MARKS, start=1):
        atlas_page(c, i, prompt, page)
        page += 1
    closing_page(c, page)    # last

    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
