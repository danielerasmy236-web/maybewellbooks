"""Generate 15-Minute Micro-Adventures — Missions Built to Finish Before the
Moment Passes (letter PDF).

Field Notes line, Volume Four. Reuses the DWYI/TWIW/Wander production
pipeline: Fraunces (titles) + Nunito (body) static instances, ReportLab
canvas, vector icons only (no emoji glyphs).

Compact Template B variant: no sections, no dividers — 80 flat missions
tagged by setting icon (indoor / outdoor / anywhere) instead of chapters.
Each page drops the hint paragraph and draw box in favor of a single
one-line log — the point is speed, not depth.

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

import content_micro as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_PATH = os.path.join(HERE, "..", "15-minute-micro-adventures_v1.0_letter.pdf")

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


def draw_star_row(c, x_right, cy, stars):
    for i in range(3):
        draw_star(c, x_right - (2 - i) * 16 - 6, cy, 6, i < stars)


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


def draw_timer(c, cx, y_top, scale=1.0):
    """The cover icon: a kitchen-timer dial — the 15-minute countdown."""
    r = 44 * scale
    top_y = ty(y_top)
    cy = top_y - 20 * scale - r

    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2.4 * scale)
    c.circle(cx, cy, r, fill=0, stroke=1)

    # button on top
    c.setFillColorRGB(*rgb(INK))
    c.rect(cx - 6 * scale, cy + r - 2 * scale, 12 * scale, 10 * scale, fill=1, stroke=0)

    # tick marks
    for ang_deg in range(0, 360, 30):
        rad = math.radians(ang_deg)
        x1 = cx + (r - 6 * scale) * math.cos(rad)
        y1 = cy + (r - 6 * scale) * math.sin(rad)
        x2 = cx + r * math.cos(rad)
        y2 = cy + r * math.sin(rad)
        c.setLineWidth(1 * scale)
        c.line(x1, y1, x2, y2)

    # hand pointing to "15" position (90 degrees, ochre, short — quarter turn)
    hand_len = r * 0.62
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(3 * scale)
    c.line(cx, cy, cx + hand_len * math.cos(math.radians(20)),
           cy + hand_len * math.sin(math.radians(20)))
    c.setFillColorRGB(*rgb(INK))
    c.circle(cx, cy, 2.6 * scale, fill=1, stroke=0)


def draw_tag_icon(c, tag, x, cy, scale=1.0):
    """Small setting icon: house (IN), leaf (OUT), or ring (ANY)."""
    if tag == "IN":
        w, h = 14 * scale, 11 * scale
        base_y = cy - h / 2
        c.setStrokeColorRGB(*rgb(INK))
        c.setLineWidth(1.1)
        c.rect(x, base_y, w, h * 0.62, fill=0, stroke=1)
        p = c.beginPath()
        p.moveTo(x - 2 * scale, base_y + h * 0.62)
        p.lineTo(x + w / 2, base_y + h)
        p.lineTo(x + w + 2 * scale, base_y + h * 0.62)
        c.drawPath(p, fill=0, stroke=1)
    elif tag == "OUT":
        c.setStrokeColorRGB(*rgb(INK))
        c.setFillColorRGB(*rgb(OCHRE))
        c.setLineWidth(1.0)
        r = 6 * scale
        p = c.beginPath()
        p.moveTo(x + r, cy - r)
        p.curveTo(x + r * 2.1, cy - r * 0.3, x + r * 1.6, cy + r * 0.9, x + r, cy + r)
        p.curveTo(x + r * 0.4, cy + r * 0.9, x - r * 0.1, cy - r * 0.3, x + r, cy - r)
        p.close()
        c.drawPath(p, fill=1, stroke=0)
        c.setStrokeColorRGB(*rgb(INK))
        c.setLineWidth(0.8)
        c.line(x + r, cy - r * 0.2, x + r, cy + r)
    else:  # ANY
        c.setStrokeColorRGB(*rgb(INK))
        c.setLineWidth(1.1)
        r = 6.5 * scale
        c.circle(x + r, cy, r, fill=0, stroke=1)
        c.ellipse(x + r - r * 0.95, cy - r * 0.45, x + r + r * 0.95, cy + r * 0.45,
                   fill=0, stroke=1)


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
    c.setFont("Fraunces-Black", 46)
    c.drawCentredString(PAGE_W / 2, ty(300), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(354), C.TITLE_LINES[1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(394), 96, 3, fill=1, stroke=0)

    plain_text(c, PAGE_W / 2, ty(428), C.SUBTITLE, "Nunito-XLI", 15, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(450), C.SPANISH_NOTE, "Nunito-XLI", 12, INK, center=True)

    draw_timer(c, PAGE_W / 2, 500)

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
    c.setFont("Fraunces-Black", 30)
    c.drawCentredString(PAGE_W / 2, ty(328), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(366), C.TITLE_LINES[1])
    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 40, ty(392), 80, 2.5, fill=1, stroke=0)
    plain_text(c, PAGE_W / 2, ty(420), C.SUBTITLE, "Nunito-XLI", 13, INK, center=True)
    draw_timer(c, PAGE_W / 2, 484, scale=0.62)
    plain_text(c, PAGE_W / 2, ty(660), "dead time isn't dead.", "Nunito-XL", 12, INK, center=True)
    c.showPage()


def intro_page(c, page_num):
    tracked_text(c, M, ty(60), C.INTRO_KICKER, "Nunito-Bold", 10, 2.4, OCHRE)
    plain_text(c, M, ty(96), C.INTRO_TITLE, "Fraunces-Black", 23, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(114), PAGE_W - M, ty(114))

    y = 144
    for item in C.INTRO_PARAS:
        if isinstance(item, tuple):
            label, body = item
            if label == "TAGS":
                for tag, desc in C.TAG_LEGEND:
                    draw_tag_icon(c, tag, M + 2, ty(y - 3))
                    plain_text(c, M + 30, ty(y), tag, "Nunito-Bold", 10, INK)
                    plain_text(c, M + 62, ty(y), desc, "Nunito-XLI", 10.5, INK)
                    y += 18
                y += 6
            elif label == "STARS":
                for stars, desc in C.STAR_LEGEND:
                    for i in range(3):
                        draw_star(c, M + 8 + i * 15, ty(y - 4), 5.5, i < stars)
                    plain_text(c, M + 56, ty(y), desc, "Nunito-XLI", 10.5, INK)
                    y += 18
                y += 6
            else:
                tracked_text(c, M, ty(y), label, "Nunito-Bold", 10, 2.4, OCHRE)
                lines = wrap(body, "Nunito-Reg", 11, CW - 64)
                yy = y
                for ln in lines:
                    plain_text(c, M + 64, ty(yy), ln, "Nunito-Reg", 11, INK)
                    yy += 16
                y = yy + 9
        else:
            for ln in wrap(item, "Nunito-Reg", 11, CW):
                plain_text(c, M, ty(y), ln, "Nunito-Reg", 11, INK)
                y += 16
            y += 9

    footer(c, page_num)
    c.showPage()


def mission_page(c, mission_no, tag, stars, prompt, page_num):
    tracked_text(c, M, ty(64), "MISSION", "Nunito-Bold", 10, 2.4, OCHRE)
    draw_tag_icon(c, tag, M + 74, ty(60))
    plain_text(c, M + 96, ty(64), tag, "Nunito-Bold", 9, INK)

    draw_star_row(c, PAGE_W - M - 62, ty(60), stars)
    plain_text(c, PAGE_W - M, ty(64), f"No. {mission_no:02d}", "Fraunces-SemiBold",
               12, INK, right=True)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(80), PAGE_W - M, ty(80))

    # big compact prompt, set a comfortable distance below the header
    lines = wrap(prompt, "Fraunces-SemiBold", 24, CW)
    y = 190
    for ln in lines:
        plain_text(c, M, ty(y), ln, "Fraunces-SemiBold", 24, INK)
        y += 33

    # single compact log line, close below the prompt — the rest of the
    # page is deliberate white space (this is a 15-minute book, not a diary)
    log_y = max(y + 50, 330)
    tracked_text(c, M, ty(log_y), "LOG", "Nunito-Bold", 10, 2.4, OCHRE)
    done_w = pdfmetrics.stringWidth("done", "Nunito-XLI", 10)
    plain_text(c, PAGE_W - M, ty(log_y), "done", "Nunito-XLI", 10, INK, right=True)
    box_s = 10
    box_gap = 6
    box_x = PAGE_W - M - done_w - box_gap - box_s
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.rect(box_x, ty(log_y) - 1, box_s, box_s, fill=0, stroke=1)

    c.setLineWidth(0.7)
    c.line(M, ty(log_y + 22), PAGE_W - M - 40, ty(log_y + 22))

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

    draw_timer(c, PAGE_W / 2, 500, scale=0.5)

    plain_text(c, PAGE_W / 2, ty(660), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 10, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(682), "dead time isn't dead.", "Nunito-XL", 10, INK,
               center=True)
    footer(c, page_num)
    c.showPage()


def main():
    register_fonts()
    out = os.path.abspath(OUT_PATH)
    c = _canvas.Canvas(out, pagesize=letter)
    c.setTitle("15-Minute Micro-Adventures — Missions Built to Finish Before the Moment Passes")
    c.setAuthor("Maybewell Books")
    c.setSubject("80 zero-setup missions sized for real dead time — a bus stop, a work break — tagged indoor/outdoor/anywhere.")
    c.setCreator("anonymous")

    cover(c)
    title_page(c)
    intro_page(c, 3)
    page = 4
    for i, (tag, stars, prompt) in enumerate(C.MISSIONS, start=1):
        mission_page(c, i, tag, stars, prompt, page)
        page += 1
    closing_page(c, page)

    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
