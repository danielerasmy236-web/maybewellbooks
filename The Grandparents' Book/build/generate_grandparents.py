"""Generate The Grandparents' Book — A Large-Print Interview Book for the
Stories Worth Keeping (letter PDF).

Field Notes line, Volume Seven. Reuses the DWYI/TWIW/Wander production
pipeline: Fraunces (titles) + Nunito (body) static instances, ReportLab
canvas, vector icons only (no emoji glyphs).

Template E, interview Q&A variant, LARGE PRINT: every font size steps up
from the standard Field Notes scale (question 22pt vs 18-19pt, body 13.5pt
vs 11.5pt, generous 30pt-spaced ruled answer lines) — matching the
accessibility approach of the Word Search Safari line.

Grayscale discipline: unlike TWIW/Wander/etc., every text run in this book
uses INK, never the OCHRE accent — ochre is reserved for decorative shapes
(rules, dots, icon fills) only, never for anything a reader has to read.
This keeps every span under the 0.45 luminance ceiling a photocopier needs.

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

import content_grandparents as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_PATH = os.path.join(HERE, "..", "the-grandparents-book_v1.0_letter.pdf")

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


def tracked_text(c, x, y, text, font, size, track, color=INK, center=False):
    """Draw letterspaced text and ALWAYS emit a trailing `0 Tc` (Tc leak
    guard). Defaults to INK — this book never uses ochre for text, to stay
    under the 0.45 grayscale luminance ceiling."""
    if center:
        x = x - tracked_width(text, font, size, track) / 2
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColorRGB(*rgb(color))
    t.setCharSpace(track)
    t.textOut(text)
    t.setCharSpace(0)
    c.drawText(t)


def plain_text(c, x, y, text, font, size, color=INK, right=False, center=False):
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
    plain_text(c, M + 10, ty(747), C.TAGLINE, "Nunito-XL", 9, INK)
    plain_text(c, PAGE_W - M, ty(747), str(page_num), "Nunito-Reg", 9, INK, right=True)


def putty_bg(c):
    c.setFillColorRGB(*rgb(PUTTY))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_portrait_frame(c, cx, y_top, scale=1.0):
    """The recurring icon: a framed portrait with a simple figure inside and
    an ochre nameplate — the keepsake, interview-subject motif."""
    w, h = 96 * scale, 116 * scale
    x0 = cx - w / 2
    y1 = ty(y_top)
    y0 = y1 - h

    c.setFillColorRGB(*rgb(PUTTY))
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2.6 * scale)
    c.roundRect(x0, y0, w, h, 8 * scale, fill=1, stroke=1)

    cx_fig = x0 + w / 2
    c.setFillColorRGB(*rgb(INK))
    c.circle(cx_fig, y0 + h * 0.66, 14 * scale, fill=1, stroke=0)
    p = c.beginPath()
    p.moveTo(x0 + w * 0.22, y0 + h * 0.18)
    p.curveTo(x0 + w * 0.22, y0 + h * 0.40, x0 + w * 0.78, y0 + h * 0.40,
              x0 + w * 0.78, y0 + h * 0.18)
    p.lineTo(x0 + w * 0.78, y0 + h * 0.08)
    p.lineTo(x0 + w * 0.22, y0 + h * 0.08)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(x0 + w * 0.2, y0 - 4 * scale, w * 0.6, 5 * scale, fill=1, stroke=0)


# --------------------------------------------------------------------- pages

def cover(c):
    putty_bg(c)
    wm = "M A Y B E W E L L   B O O K S"
    plain_text(c, PAGE_W / 2, ty(74), wm, "Nunito-Bold", 13, INK, center=True)
    wm_w = pdfmetrics.stringWidth(wm, "Nunito-Bold", 13)
    draw_star(c, PAGE_W / 2 + wm_w / 2 + 15, ty(70), 5.5, True)

    tracked_text(c, PAGE_W / 2, ty(227), C.EYEBROW, "Nunito-Bold", 11, 2.4,
                 INK, center=True)

    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", 40)
    c.drawCentredString(PAGE_W / 2, ty(298), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(346), C.TITLE_LINES[1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(386), 96, 3, fill=1, stroke=0)

    plain_text(c, PAGE_W / 2, ty(420), C.SUBTITLE, "Nunito-XLI", 15, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(444), C.SPANISH_NOTE, "Nunito-XLI", 12, INK, center=True)

    draw_portrait_frame(c, PAGE_W / 2, 500)

    badge_w = tracked_width(C.BADGE, "Nunito-Bold", 10, 1.2) + 36
    c.setFillColorRGB(*rgb(OCHRE))
    c.roundRect(PAGE_W / 2 - badge_w / 2, ty(686), badge_w, 22, 11, fill=1, stroke=0)
    tracked_text(c, PAGE_W / 2, ty(679), C.BADGE, "Nunito-Bold", 10, 1.2,
                 INK, center=True)

    plain_text(c, PAGE_W / 2, ty(720), C.TAGLINE, "Nunito-XL", 12, INK, center=True)
    tracked_text(c, PAGE_W / 2, ty(755), "maybewellbooks.com", "Nunito-XL", 10,
                 0.54, INK, center=True)
    c.showPage()


def title_page(c):
    putty_bg(c)
    plain_text(c, PAGE_W / 2, ty(120), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 11, INK, center=True)
    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", 28)
    c.drawCentredString(PAGE_W / 2, ty(328), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(364), C.TITLE_LINES[1])
    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 40, ty(392), 80, 2.5, fill=1, stroke=0)
    plain_text(c, PAGE_W / 2, ty(422), C.SUBTITLE, "Nunito-XLI", 13.5, INK, center=True)
    draw_portrait_frame(c, PAGE_W / 2, 488, scale=0.62)
    plain_text(c, PAGE_W / 2, ty(660), "some stories only get told once.",
               "Nunito-XL", 13, INK, center=True)
    c.showPage()


def intro_page(c, page_num):
    tracked_text(c, M, ty(66), C.INTRO_KICKER, "Nunito-Bold", 11, 2.4, INK)
    plain_text(c, M, ty(104), C.INTRO_TITLE, "Fraunces-Black", 26, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(122), PAGE_W - M, ty(122))

    y = 156
    for item in C.INTRO_PARAS:
        if isinstance(item, tuple):
            label, body = item
            tracked_text(c, M, ty(y), label, "Nunito-Bold", 11, 2.4, INK)
            lines = wrap(body, "Nunito-Reg", 13.5, CW - 74)
            yy = y
            for ln in lines:
                plain_text(c, M + 74, ty(yy), ln, "Nunito-Reg", 13.5, INK)
                yy += 20
            y = yy + 11
        else:
            for ln in wrap(item, "Nunito-Reg", 13.5, CW):
                plain_text(c, M, ty(y), ln, "Nunito-Reg", 13.5, INK)
                y += 20
            y += 11

    footer(c, page_num)
    c.showPage()


def divider_page(c, idx, title, note, count):
    putty_bg(c)
    label = f"SECTION {C.NUM_WORDS[idx]}  ·  {count} QUESTIONS"
    tracked_text(c, PAGE_W / 2, PAGE_H / 2 + 52, label, "Nunito-Bold", 12, 2.4,
                 INK, center=True)
    plain_text(c, PAGE_W / 2, PAGE_H / 2 + 6, title, "Fraunces-Black", 32, INK,
               center=True)
    plain_text(c, PAGE_W / 2, PAGE_H / 2 - 26, note, "Nunito-XLI", 13.5, INK,
               center=True)
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.4)
    c.line(PAGE_W / 2 - 65, PAGE_H / 2 - 52, PAGE_W / 2 + 65, PAGE_H / 2 - 52)
    c.showPage()


def question_page(c, section_title, q_no, question, page_num):
    tracked_text(c, M, ty(62), section_title.upper(), "Nunito-Bold", 11, 2.0, INK)
    plain_text(c, PAGE_W - M, ty(62), f"No. {q_no:02d}", "Fraunces-SemiBold",
               13, INK, right=True)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(76), PAGE_W - M, ty(76))

    tracked_text(c, M, ty(112), "ASK", "Nunito-Bold", 11, 2.4, INK)
    y = 144
    for ln in wrap(question, "Fraunces-SemiBold", 22, CW):
        plain_text(c, M, ty(y), ln, "Fraunces-SemiBold", 22, INK)
        y += 30

    ans_top = max(y + 20, 226)
    tracked_text(c, M, ty(ans_top), "ANSWER", "Nunito-Bold", 11, 2.4, INK)

    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.7)
    line_top = ans_top + 30
    yy = line_top
    while yy <= 706:
        c.line(M, ty(yy), PAGE_W - M, ty(yy))
        yy += 30

    footer(c, page_num)
    c.showPage()


def closing_page(c, page_num):
    putty_bg(c)
    plain_text(c, PAGE_W / 2, ty(300), C.CLOSING_TITLE, "Fraunces-Black", 28,
               INK, center=True)
    plain_text(c, PAGE_W / 2, ty(346), C.CLOSING_BODY, "Nunito-Reg", 14.5, INK,
               center=True)

    stats_w = pdfmetrics.stringWidth(C.CLOSING_STATS, "Nunito-Bold", 13)
    plain_text(c, PAGE_W / 2 - 10, ty(412), C.CLOSING_STATS, "Nunito-Bold", 13,
               INK, center=True)
    draw_infinity(c, PAGE_W / 2 - 10 + stats_w / 2 + 16, ty(408))

    plain_text(c, PAGE_W / 2, ty(458), C.CLOSING_SHARE, "Nunito-XLI", 13, INK,
               center=True)

    draw_portrait_frame(c, PAGE_W / 2, 502, scale=0.5)

    plain_text(c, PAGE_W / 2, ty(660), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 11, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(682), "some stories only get told once.",
               "Nunito-XL", 11, INK, center=True)
    footer(c, page_num)
    c.showPage()


def main():
    register_fonts()
    out = os.path.abspath(OUT_PATH)
    c = _canvas.Canvas(out, pagesize=letter)
    c.setTitle("The Grandparents' Book — A Large-Print Interview Book for the Stories Worth Keeping")
    c.setAuthor("Maybewell Books")
    c.setSubject("A large-print interview activity book: 42 questions across 6 sections for a younger person to hand-transcribe an older relative's answers.")
    c.setCreator("anonymous")

    cover(c)
    title_page(c)
    intro_page(c, 3)
    page = 4
    q_no = 0
    for idx, (title, note, questions) in enumerate(C.SECTIONS):
        divider_page(c, idx, title, note, len(questions))
        page += 1
        for question in questions:
            q_no += 1
            question_page(c, title, q_no, question, page)
            page += 1
    closing_page(c, page)

    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
