"""Generate Questions They Never Ask You — A Conversation Manual for Dinners,
Car Rides, and Waiting Rooms (letter PDF).

Field Notes line, Volume Five. Reuses the DWYI/TWIW/Wander production
pipeline: Fraunces (titles) + Nunito (body) static instances, ReportLab
canvas, vector icons only (no emoji glyphs).

Template B, two-answer variant: each question page carries two independent
ruled-line answer zones (ANSWER ONE / ANSWER TWO) instead of a single
LOG+DRAW/NOTICE pairing — this book is a shared conversation, not a solo log.

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

import content_questions as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_PATH = os.path.join(HERE, "..", "questions-they-never-ask-you_v1.0_letter.pdf")

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


def draw_speech_bubbles(c, cx, y_top, scale=1.0):
    """The cover icon: two overlapping speech bubbles — one asking, one
    answering."""
    top_y = ty(y_top)
    w1, h1 = 74 * scale, 52 * scale
    x1, y1 = cx - 46 * scale, top_y - 14 * scale - h1
    c.setFillColorRGB(*rgb(PUTTY))
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2.2 * scale)
    c.roundRect(x1, y1, w1, h1, 12 * scale, fill=1, stroke=1)
    p = c.beginPath()
    p.moveTo(x1 + 16 * scale, y1)
    p.lineTo(x1 + 6 * scale, y1 - 12 * scale)
    p.lineTo(x1 + 28 * scale, y1)
    p.close()
    c.setFillColorRGB(*rgb(PUTTY))
    c.drawPath(p, fill=1, stroke=0)
    c.setStrokeColorRGB(*rgb(INK))
    c.line(x1 + 16 * scale, y1, x1 + 6 * scale, y1 - 12 * scale)
    c.line(x1 + 6 * scale, y1 - 12 * scale, x1 + 28 * scale, y1)

    w2, h2 = 62 * scale, 44 * scale
    x2, y2 = cx - 6 * scale, y1 + h1 - 20 * scale
    c.setFillColorRGB(*rgb(OCHRE))
    c.roundRect(x2, y2, w2, h2, 10 * scale, fill=1, stroke=0)
    p2 = c.beginPath()
    p2.moveTo(x2 + w2 - 18 * scale, y2)
    p2.lineTo(x2 + w2 - 6 * scale, y2 - 11 * scale)
    p2.lineTo(x2 + w2 - 30 * scale, y2)
    p2.close()
    c.drawPath(p2, fill=1, stroke=0)

    # question mark dot + dash inside bubble one (ink), answer lines inside two
    c.setFillColorRGB(*rgb(INK))
    c.circle(x1 + w1 / 2, y1 + 12 * scale, 1.8 * scale, fill=1, stroke=0)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2 * scale)
    c.arc(x1 + w1 / 2 - 6 * scale, y1 + 20 * scale, x1 + w1 / 2 + 6 * scale,
          y1 + 32 * scale, 200, 160)

    c.setStrokeColorRGB(*rgb(PUTTY))
    c.setLineWidth(1.6 * scale)
    for i in range(2):
        yy = y2 + h2 / 2 + 6 * scale - i * 10 * scale
        c.line(x2 + 12 * scale, yy, x2 + w2 - 12 * scale, yy)


def ruled_block(c, top_y, n_lines, spacing=22):
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.6)
    y = top_y
    for _ in range(n_lines):
        c.line(M, ty(y), PAGE_W - M, ty(y))
        y += spacing
    return y


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
    c.setFont("Fraunces-Black", 42)
    c.drawCentredString(PAGE_W / 2, ty(300), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(350), C.TITLE_LINES[1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(390), 96, 3, fill=1, stroke=0)

    plain_text(c, PAGE_W / 2, ty(424), C.SUBTITLE, "Nunito-XLI", 14, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(446), C.SPANISH_NOTE, "Nunito-XLI", 12, INK, center=True)

    draw_speech_bubbles(c, PAGE_W / 2, 502)

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
    c.setFont("Fraunces-Black", 28)
    c.drawCentredString(PAGE_W / 2, ty(328), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(364), C.TITLE_LINES[1])
    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 40, ty(390), 80, 2.5, fill=1, stroke=0)
    plain_text(c, PAGE_W / 2, ty(418), C.SUBTITLE, "Nunito-XLI", 12.5, INK, center=True)
    draw_speech_bubbles(c, PAGE_W / 2, 486, scale=0.62)
    plain_text(c, PAGE_W / 2, ty(660), "these are the ones worth asking.",
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


def divider_page(c, idx, title, note, count):
    putty_bg(c)
    label = f"SECTION {C.NUM_WORDS[idx]}  ·  {count} QUESTIONS"
    tracked_text(c, PAGE_W / 2, PAGE_H / 2 + 52, label, "Nunito-Bold", 11, 2.4,
                 OCHRE, center=True)
    plain_text(c, PAGE_W / 2, PAGE_H / 2 + 6, title, "Fraunces-Black", 28, INK,
               center=True)
    plain_text(c, PAGE_W / 2, PAGE_H / 2 - 26, note, "Nunito-XLI", 12, INK,
               center=True)
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.2)
    c.line(PAGE_W / 2 - 65, PAGE_H / 2 - 52, PAGE_W / 2 + 65, PAGE_H / 2 - 52)
    c.showPage()


def question_page(c, section_title, q_no, question, page_num):
    tracked_text(c, M, ty(60), section_title.upper(), "Nunito-Bold", 10, 2.0, OCHRE)
    plain_text(c, PAGE_W - M, ty(60), f"No. {q_no:02d}", "Fraunces-SemiBold",
               12, INK, right=True)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(72), PAGE_W - M, ty(72))

    tracked_text(c, M, ty(104), "ASK", "Nunito-Bold", 10, 2.4, OCHRE)
    y = 132
    for ln in wrap(question, "Fraunces-SemiBold", 19, CW):
        plain_text(c, M, ty(y), ln, "Fraunces-SemiBold", 19, INK)
        y += 26

    block_top = max(y + 22, 232)
    half = (706 - block_top - 20) / 2
    spacing = 24
    n_lines = max(3, int((half - 30) // spacing))

    for i, label in enumerate(("ANSWER ONE", "ANSWER TWO")):
        top = block_top + i * (half + 20)
        tracked_text(c, M, ty(top), label, "Nunito-Bold", 10, 2.4, OCHRE)
        name_w = 150
        c.setStrokeColorRGB(*rgb(INK))
        c.setLineWidth(0.7)
        c.line(M + 90, ty(top + 3), M + 90 + name_w, ty(top + 3))
        plain_text(c, M + 90 + name_w + 10, ty(top), "name", "Nunito-XLI", 9, INK)
        ruled_block(c, top + 28, n_lines, spacing=spacing)

    footer(c, page_num)
    c.showPage()


def closing_page(c, page_num):
    putty_bg(c)
    plain_text(c, PAGE_W / 2, ty(300), C.CLOSING_TITLE, "Fraunces-Black", 26,
               INK, center=True)
    plain_text(c, PAGE_W / 2, ty(345), C.CLOSING_BODY, "Nunito-Reg", 13, INK,
               center=True)

    stats_w = pdfmetrics.stringWidth(C.CLOSING_STATS, "Nunito-Bold", 12)
    plain_text(c, PAGE_W / 2 - 10, ty(410), C.CLOSING_STATS, "Nunito-Bold", 12,
               INK, center=True)
    draw_infinity(c, PAGE_W / 2 - 10 + stats_w / 2 + 16, ty(406))

    plain_text(c, PAGE_W / 2, ty(455), C.CLOSING_SHARE, "Nunito-XLI", 12, INK,
               center=True)

    draw_speech_bubbles(c, PAGE_W / 2, 500, scale=0.5)

    plain_text(c, PAGE_W / 2, ty(660), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 10, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(682), "these are the ones worth asking.",
               "Nunito-XL", 10, INK, center=True)
    footer(c, page_num)
    c.showPage()


def main():
    register_fonts()
    out = os.path.abspath(OUT_PATH)
    c = _canvas.Canvas(out, pagesize=letter)
    c.setTitle("Questions They Never Ask You — A Conversation Manual for Dinners, Car Rides, and Waiting Rooms")
    c.setAuthor("Maybewell Books")
    c.setSubject("A two-answer conversation manual: 48 specific, non-cliche questions across 6 sections, with room for two people to write their own answers side by side.")
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
