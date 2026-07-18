"""Generate Wander Without a Destination — An Instruction-Led Guide to Getting
Pleasantly Lost (letter PDF).

Field Notes line, Volume Two. Reuses the DWYI/TWIW production pipeline:
Fraunces (titles) + Nunito (body) static instances, ReportLab canvas, vector
icons only (no emoji glyphs).

Template B differs from TWIW's Template A: two working zones per page
(WALK, then LOG+NOTICE) instead of three (FIND/LOG/DRAW) — this book is about
walking, not sketching, so the third zone is ruled writing lines instead of a
blank sketch box.

Tc discipline: every tracked (letterspaced) string goes through tracked_text(),
which sets charSpace and always resets it to 0 inside the same text object —
the DWYI "Tc leak" bug came from character spacing leaking across text blocks
because Tc is page-level state that survives past ET.
"""

import math
import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as _canvas

import content_wander as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_PATH = os.path.join(HERE, "..", "wander-without-a-destination_v1.0_letter.pdf")

PAGE_W, PAGE_H = letter  # 612 x 792
M = 54.0                 # margin, matches the Figma frames
CW = PAGE_W - 2 * M      # content width 504

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
    """Convert a from-the-top y (as used in the Figma frames) to PDF coords."""
    return PAGE_H - y_top


def register_fonts():
    for name, fn in FONTS.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))


def tracked_width(text, font, size, track):
    return pdfmetrics.stringWidth(text, font, size) + track * max(len(text) - 1, 0)


def tracked_text(c, x, y, text, font, size, track, color, center=False):
    """Draw letterspaced text and ALWAYS emit a trailing `0 Tc` (Tc leak guard).

    Tc is page-level text state in PDF: it survives past ET, so a tracked
    label would silently letterspace every later string on the page unless
    we reset it inside the same text object.
    """
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
    """Three stars ending at x_right, `stars` of them filled."""
    for i in range(3):
        draw_star(c, x_right - (2 - i) * 16 - 6, cy, 6, i < stars)


def draw_pin(c, x, cy):
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.1)
    c.circle(x + 5.5, cy, 5.5, fill=0, stroke=1)
    c.setFillColorRGB(*rgb(OCHRE))
    c.circle(x + 5.5, cy, 2, fill=1, stroke=0)


def draw_calendar(c, x, cy):
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.1)
    c.roundRect(x, cy - 5, 11, 10, 2, fill=0, stroke=1)
    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(x + 2.5, cy + 3, 1.5, 4, fill=1, stroke=0)
    c.rect(x + 7, cy + 3, 1.5, 4, fill=1, stroke=0)


def draw_compass(c, cx, y_top, scale=1.0):
    """The cover icon: a compass whose needle points off in a wayward,
    non-cardinal direction — the visual shorthand for 'no fixed destination'.
    """
    r = 46 * scale
    pad = 16 * scale
    top_y = ty(y_top)
    cy = top_y - pad - r

    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2.4 * scale)
    c.circle(cx, cy, r, fill=0, stroke=1)

    tick = 7 * scale
    for ang_deg in (90, 0, 270, 180):
        rad = math.radians(ang_deg)
        x1 = cx + (r - tick) * math.cos(rad)
        y1 = cy + (r - tick) * math.sin(rad)
        x2 = cx + r * math.cos(rad)
        y2 = cy + r * math.sin(rad)
        c.setLineWidth(1.5 * scale)
        c.line(x1, y1, x2, y2)

    ang = math.radians(124)  # off-kilter: not north, not any cardinal point
    needle_len = r * 0.8
    tip = (cx + needle_len * math.cos(ang), cy + needle_len * math.sin(ang))
    tail = (cx - needle_len * 0.55 * math.cos(ang), cy - needle_len * 0.55 * math.sin(ang))
    perp = ang + math.pi / 2
    w = 6.5 * scale
    side_a = (cx + w * math.cos(perp), cy + w * math.sin(perp))
    side_b = (cx - w * math.cos(perp), cy - w * math.sin(perp))

    p = c.beginPath()
    p.moveTo(*tip)
    p.lineTo(*side_a)
    p.lineTo(*side_b)
    p.close()
    c.setFillColorRGB(*rgb(OCHRE))
    c.drawPath(p, fill=1, stroke=0)

    p2 = c.beginPath()
    p2.moveTo(*tail)
    p2.lineTo(*side_a)
    p2.lineTo(*side_b)
    p2.close()
    c.setFillColorRGB(*rgb(INK))
    c.drawPath(p2, fill=1, stroke=0)

    c.setFillColorRGB(*rgb(PUTTY))
    c.circle(cx, cy, 3.4 * scale, fill=1, stroke=0)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1 * scale)
    c.circle(cx, cy, 3.4 * scale, fill=0, stroke=1)


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


def ruled_lines(c, notice_y, bottom_top=706, spacing=26):
    """Draw ruled writing lines from just below the NOTICE label down to the
    bottom margin. Returns the topmost line's top-coordinate y (for QA)."""
    line_top = notice_y + 24
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.6)
    y = line_top
    while y <= bottom_top:
        c.line(M, ty(y), PAGE_W - M, ty(y))
        y += spacing
    return line_top


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
    c.setFont("Fraunces-Black", 52)
    c.drawCentredString(PAGE_W / 2, ty(304), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(361), C.TITLE_LINES[1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(405), 96, 3, fill=1, stroke=0)

    plain_text(c, PAGE_W / 2, ty(440), C.SUBTITLE, "Nunito-XLI", 15, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(462), C.SPANISH_NOTE, "Nunito-XLI", 12, INK, center=True)

    draw_compass(c, PAGE_W / 2, 500)

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
    c.setFont("Fraunces-Black", 34)
    c.drawCentredString(PAGE_W / 2, ty(328), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(368), C.TITLE_LINES[1])
    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 40, ty(396), 80, 2.5, fill=1, stroke=0)
    plain_text(c, PAGE_W / 2, ty(424), C.SUBTITLE, "Nunito-XLI", 13, INK, center=True)
    draw_compass(c, PAGE_W / 2, 490, scale=0.62)
    plain_text(c, PAGE_W / 2, ty(660), "get a little lost.", "Nunito-XL", 12, INK, center=True)
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
            if label == "STARS":
                for stars, desc in C.STAR_LEGEND:
                    for i in range(3):
                        draw_star(c, M + 8 + i * 15, ty(y - 4), 5.5, i < stars)
                    plain_text(c, M + 56, ty(y), desc, "Nunito-XLI", 11, INK)
                    y += 20
                y += 6
            else:
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


NUM_WORDS = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN"]


def divider_page(c, idx, title, note, count):
    putty_bg(c)
    label = f"SECTION {NUM_WORDS[idx]}  ·  {count} WALKS"
    tracked_text(c, PAGE_W / 2, PAGE_H / 2 + 52, label, "Nunito-Bold", 11, 2.4,
                 OCHRE, center=True)
    plain_text(c, PAGE_W / 2, PAGE_H / 2 + 6, title, "Fraunces-Black", 30, INK,
               center=True)
    plain_text(c, PAGE_W / 2, PAGE_H / 2 - 26, note, "Nunito-XLI", 12, INK,
               center=True)
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.2)
    c.line(PAGE_W / 2 - 65, PAGE_H / 2 - 52, PAGE_W / 2 + 65, PAGE_H / 2 - 52)
    c.showPage()


def field_page(c, section_title, walk_no, stars, prompt, hint, page_num):
    # header
    tracked_text(c, M, ty(60), section_title.upper(), "Nunito-Bold", 10, 2.0, OCHRE)
    plain_text(c, PAGE_W - M, ty(60), f"No. {walk_no:02d}", "Fraunces-SemiBold",
               12, INK, right=True)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(72), PAGE_W - M, ty(72))

    # WALK
    tracked_text(c, M, ty(110), "WALK", "Nunito-Bold", 10, 2.4, OCHRE)
    if stars > 0:
        draw_star_row(c, PAGE_W - M, ty(106), stars)

    y = 140
    for ln in wrap(prompt, "Fraunces-SemiBold", 18, CW):
        plain_text(c, M, ty(y), ln, "Fraunces-SemiBold", 18, INK)
        y += 25
    y += 4
    for ln in wrap(hint, "Nunito-XLI", 12, CW):
        plain_text(c, M, ty(y), ln, "Nunito-XLI", 12, INK)
        y += 16

    # LOG (adaptive: sits below the prompt block, never above y=232)
    log_y = max(y + 18, 232)
    tracked_text(c, M, ty(log_y), "LOG", "Nunito-Bold", 10, 2.4, OCHRE)
    row_y = log_y + 26
    draw_pin(c, M, ty(row_y - 4))
    plain_text(c, M + 18, ty(row_y), "Where I ended up:", "Nunito-Reg", 11, INK)
    where_x = M + 18 + pdfmetrics.stringWidth("Where I ended up:", "Nunito-Reg", 11) + 8
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(0.8)
    c.line(where_x, ty(row_y + 3), where_x + 178, ty(row_y + 3))
    cal_x = where_x + 178 + 24
    draw_calendar(c, cal_x, ty(row_y - 4))
    plain_text(c, cal_x + 18, ty(row_y), "Date:", "Nunito-Reg", 11, INK)
    date_x = cal_x + 18 + pdfmetrics.stringWidth("Date:", "Nunito-Reg", 11) + 8
    c.line(date_x, ty(row_y + 3), PAGE_W - M, ty(row_y + 3))

    # NOTICE — ruled lines instead of a draw box: this book logs the walk,
    # it doesn't ask the reader to sketch it.
    notice_y = log_y + 62
    tracked_text(c, M, ty(notice_y), "NOTICE", "Nunito-Bold", 10, 2.4, OCHRE)
    plain_text(c, PAGE_W - M, ty(notice_y), "one thing along the way",
               "Nunito-XLI", 10, INK, right=True)
    ruled_lines(c, notice_y)

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

    draw_compass(c, PAGE_W / 2, 500, scale=0.5)

    plain_text(c, PAGE_W / 2, ty(660), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 10, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(682), "get a little lost.", "Nunito-XL", 10, INK,
               center=True)
    footer(c, page_num)
    c.showPage()


def main():
    register_fonts()
    out = os.path.abspath(OUT_PATH)
    c = _canvas.Canvas(out, pagesize=letter)
    c.setTitle("Wander Without a Destination — An Instruction-Led Guide to Getting Pleasantly Lost")
    c.setAuthor("Maybewell Books")
    c.setSubject("A destination-less walking guide: 70 semi-random instructions for a dérive, with room to log where you ended up.")
    c.setCreator("anonymous")

    cover(c)                      # p1
    title_page(c)                 # p2
    intro_page(c, 3)              # p3
    page = 4
    walk_no = 0
    for idx, (title, note, prompts) in enumerate(C.SECTIONS):
        divider_page(c, idx, title, note, len(prompts))
        page += 1
        for stars, prompt, hint in prompts:
            walk_no += 1
            field_page(c, title, walk_no, stars, prompt, hint, page)
            page += 1
    closing_page(c, page)         # last

    c.save()
    print(f"wrote {out} ({page} pages)")


if __name__ == "__main__":
    main()
