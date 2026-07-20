"""Generate Letter to the Future — A Correspondence Book for Sealing,
Storing, and Opening Later (letter PDF).

Field Notes line, Volume Six. Reuses the DWYI/TWIW/Wander production
pipeline: Fraunces (titles) + Nunito (body) static instances, ReportLab
canvas, vector icons only (no emoji glyphs).

Template D, correspondence variant: three time-horizon sections, each a
reflection-prompt page (with a sealed "open on ___" date field and an
envelope-flap graphic) followed by several blank ruled letter pages, plus a
closing "Instructions for Storage" page instead of the usual DWYI closing.

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

import content_letter as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_PATH = os.path.join(HERE, "..", "letter-to-the-future_v1.0_letter.pdf")

PAGE_W, PAGE_H = letter
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


def draw_envelope(c, cx, y_top, scale=1.0, sealed=True):
    """The recurring icon: an envelope with a triangular flap and an ochre
    wax-seal dot — the correspondence motif."""
    w, h = 112 * scale, 76 * scale
    x0 = cx - w / 2
    y1 = ty(y_top)
    y0 = y1 - h

    c.setFillColorRGB(*rgb(PUTTY))
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2.2 * scale)
    c.rect(x0, y0, w, h, fill=1, stroke=1)

    c.setLineWidth(1.4 * scale)
    p = c.beginPath()
    p.moveTo(x0, y1)
    p.lineTo(x0 + w / 2, y0 + h * 0.42)
    p.lineTo(x0 + w, y1)
    c.drawPath(p, fill=0, stroke=1)

    if sealed:
        c.setFillColorRGB(*rgb(OCHRE))
        c.circle(x0 + w / 2, y0 + h * 0.42, 9 * scale, fill=1, stroke=0)
        c.setStrokeColorRGB(*rgb(PUTTY))
        c.setLineWidth(1 * scale)
        c.circle(x0 + w / 2, y0 + h * 0.42, 4 * scale, fill=0, stroke=1)


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
    c.setFont("Fraunces-Black", 54)
    c.drawCentredString(PAGE_W / 2, ty(304), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(363), C.TITLE_LINES[1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(403), 96, 3, fill=1, stroke=0)

    plain_text(c, PAGE_W / 2, ty(436), C.SUBTITLE, "Nunito-XLI", 14, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(458), C.SPANISH_NOTE, "Nunito-XLI", 12, INK, center=True)

    draw_envelope(c, PAGE_W / 2, 508)

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
    plain_text(c, PAGE_W / 2, ty(426), C.SUBTITLE, "Nunito-XLI", 12.5, INK, center=True)
    draw_envelope(c, PAGE_W / 2, 488, scale=0.62)
    plain_text(c, PAGE_W / 2, ty(660), "some things are worth waiting for.",
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
            lines = wrap(body, "Nunito-Reg", 11.5, CW - 80)
            yy = y
            for ln in lines:
                plain_text(c, M + 80, ty(yy), ln, "Nunito-Reg", 11.5, INK)
                yy += 17
            y = yy + 9
        else:
            for ln in wrap(item, "Nunito-Reg", 11.5, CW):
                plain_text(c, M, ty(y), ln, "Nunito-Reg", 11.5, INK)
                y += 17
            y += 9

    footer(c, page_num)
    c.showPage()


def horizon_page(c, label, prompts, page_num):
    putty_bg(c)
    tracked_text(c, PAGE_W / 2, ty(150), "OPEN IN", "Nunito-Bold", 11, 2.4,
                 OCHRE, center=True)
    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", 44)
    c.drawCentredString(PAGE_W / 2, ty(212), label)

    y = 268
    tracked_text(c, M, ty(y), "BEFORE YOU WRITE", "Nunito-Bold", 10, 2.4, OCHRE)
    y += 28
    for prompt in prompts:
        c.setFillColorRGB(*rgb(OCHRE))
        c.circle(M + 3, ty(y - 4), 2, fill=1, stroke=0)
        lines = wrap(prompt, "Nunito-XLI", 12.5, CW - 22)
        for ln in lines:
            plain_text(c, M + 16, ty(y), ln, "Nunito-XLI", 12.5, INK)
            y += 19
        y += 8

    draw_envelope(c, PAGE_W / 2, 620, scale=0.72, sealed=False)

    label_w = pdfmetrics.stringWidth("Open on:", "Nunito-Bold", 10.5)
    ox = PAGE_W / 2 - 90
    plain_text(c, ox, ty(700), "Open on:", "Nunito-Bold", 10.5, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.8)
    c.line(ox + label_w + 8, ty(703), ox + label_w + 8 + 110, ty(703))

    footer(c, page_num)
    c.showPage()


def letter_page(c, horizon_label, letter_no, page_num):
    tracked_text(c, M, ty(60), f"LETTER · OPEN IN {horizon_label.upper()}",
                 "Nunito-Bold", 9, 2.0, OCHRE)
    plain_text(c, PAGE_W - M, ty(60), f"Page {letter_no}", "Fraunces-SemiBold",
               11, INK, right=True)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(72), PAGE_W - M, ty(72))

    if letter_no == 1:
        plain_text(c, M, ty(112), "Dear Future Me,", "Fraunces-SemiBold", 20, INK)
        line_top = 148
    else:
        line_top = 100

    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.6)
    y = line_top
    while y <= 706:
        c.line(M, ty(y), PAGE_W - M, ty(y))
        y += 26

    footer(c, page_num)
    c.showPage()


def closing_page(c, page_num):
    putty_bg(c)
    plain_text(c, PAGE_W / 2, ty(90), C.CLOSING_TITLE, "Fraunces-Black", 25,
               INK, center=True)
    plain_text(c, PAGE_W / 2, ty(122), C.CLOSING_INTRO, "Nunito-Reg", 12, INK,
               center=True)

    y = 168
    for label, body in C.CLOSING_POINTS:
        tracked_text(c, M, ty(y), label, "Nunito-Bold", 10, 2.4, OCHRE)
        lines = wrap(body, "Nunito-Reg", 11.5, CW - 80)
        yy = y
        for ln in lines:
            plain_text(c, M + 80, ty(yy), ln, "Nunito-Reg", 11.5, INK)
            yy += 17
        y = yy + 16

    y += 6
    plain_text(c, M, ty(y), C.CLOSING_WHO_LABEL, "Nunito-Bold", 11, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.7)
    c.line(M, ty(y + 30), PAGE_W - M, ty(y + 30))

    draw_envelope(c, PAGE_W / 2, 552, scale=0.5)

    plain_text(c, PAGE_W / 2, ty(628), C.CLOSING_BODY, "Nunito-XLI", 12, INK,
               center=True)

    stats_w = pdfmetrics.stringWidth(C.CLOSING_STATS, "Nunito-Bold", 12)
    plain_text(c, PAGE_W / 2 - 10, ty(665), C.CLOSING_STATS, "Nunito-Bold", 12,
               INK, center=True)
    draw_infinity(c, PAGE_W / 2 - 10 + stats_w / 2 + 16, ty(661))
    plain_text(c, PAGE_W / 2, ty(688), C.CLOSING_SHARE, "Nunito-XLI", 10.5, INK,
               center=True)

    footer(c, page_num)
    c.showPage()


def main():
    register_fonts()
    out = os.path.abspath(OUT_PATH)
    c = _canvas.Canvas(out, pagesize=letter)
    c.setTitle("Letter to the Future — A Correspondence Book for Sealing, Storing, and Opening Later")
    c.setAuthor("Maybewell Books")
    c.setSubject("A correspondence activity book: three sealed letters to your future self, opened in 1, 5, and 10 years, with reflection prompts and storage instructions.")
    c.setCreator("anonymous")

    cover(c)
    title_page(c)
    intro_page(c, 3)
    page = 4
    for label, years_word, prompts, n_pages in C.HORIZONS:
        horizon_page(c, label, prompts, page)
        page += 1
        for i in range(1, n_pages + 1):
            letter_page(c, label, i, page)
            page += 1
    closing_page(c, page)

    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
