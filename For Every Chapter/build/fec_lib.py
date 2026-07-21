"""Shared library for the "For Every Chapter" senior line.

Every product in this line imports from here so the cross-cutting brand
elements stay identical everywhere:

- The ribbon badge (ochre #C98A3E rosette + "FOR EVERY CHAPTER" small caps)
  drawn at the same size and position on every cover, so customers can
  visually scan the catalog for this line.
- The line-wide accessibility standard, non-negotiable: large-print type as
  the default (body >= 13.5pt, questions 20-22pt), thicker rules (1.0pt vs
  the standard catalog's 0.7pt) for tremor / reduced fine motor control,
  high ink contrast (text is always INK, never ochre — ochre decorates
  shapes only), and generous answer boxes.

Same production stack as the rest of the catalog: ReportLab, Fraunces +
Nunito static instances (shared from The World Is Watching's build), Tc
discipline via tracked_text() (always resets charSpace to 0 inside the
same text object).
"""

import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

PAGE_W, PAGE_H = letter
M = 54.0
CW = PAGE_W - 2 * M

INK = "#20303A"
PUTTY = "#F3EEE6"
OCHRE = "#D99A2B"       # catalog decorative ochre
FEC_OCHRE = "#C98A3E"   # the line's ribbon-badge ochre (brief-specified)

RULE_W = 1.0            # line-wide rule weight (thicker than catalog 0.7)

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")

FONTS = {
    "Fraunces-Black": "Fraunces-9ptBlack.ttf",
    "Fraunces-SemiBold": "Fraunces-SemiBold.ttf",
    "Nunito-XL": "Nunito-ExtraLight.ttf",
    "Nunito-XLI": "Nunito-ExtraLightItalic.ttf",
    "Nunito-Reg": "Nunito-Regular.ttf",
    "Nunito-Bold": "Nunito-Bold.ttf",
}

NUM_WORDS = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT"]


def register_fonts():
    for name, fn in FONTS.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))


def rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def ty(y_top):
    return PAGE_H - y_top


def tracked_width(text, font, size, track):
    return pdfmetrics.stringWidth(text, font, size) + track * max(len(text) - 1, 0)


def tracked_text(c, x, y, text, font, size, track, color=INK, center=False):
    """Letterspaced text with the Tc leak guard: always emits a trailing
    `0 Tc` inside the same text object."""
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


def putty_bg(c):
    c.setFillColorRGB(*rgb(PUTTY))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def footer(c, page_num, tagline):
    c.setFillColorRGB(*rgb(OCHRE))
    c.circle(M + 2, ty(745), 2, fill=1, stroke=0)
    plain_text(c, M + 10, ty(747), tagline, "Nunito-XL", 9, INK)
    plain_text(c, PAGE_W - M, ty(747), str(page_num), "Nunito-Reg", 9, INK, right=True)


def ruled_lines(c, y_start, y_end, step=30, x0=M, x1=PAGE_W - M, lw=RULE_W):
    """Large-print answer lines: 30pt spacing, thick rules."""
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(lw)
    yy = y_start
    while yy <= y_end:
        c.line(x0, ty(yy), x1, ty(yy))
        yy += step
    return yy


# ------------------------------------------------------- the line's ribbon

def draw_fec_ribbon(c):
    """The "For Every Chapter" cover badge: an ochre ribbon rosette with two
    notched tails, top-right corner, with FOR EVERY CHAPTER in small caps
    beneath. Same size and position on every cover in the line. The caption
    is INK (never ochre) so it passes the grayscale photocopy check."""
    cx = 498.0
    t = 84.0          # rosette center, distance from top
    r = 15.0

    # tails first (behind the disc)
    c.setFillColorRGB(*rgb(FEC_OCHRE))
    for sign in (-1, 1):
        x_in = cx + sign * 2
        x_out = cx + sign * 13
        top = t + r - 5
        bot = 127.0
        notch_x = cx + sign * 7.5
        p = c.beginPath()
        p.moveTo(min(x_in, x_out), ty(top))
        p.lineTo(max(x_in, x_out), ty(top))
        p.lineTo(max(x_in, x_out), ty(bot))
        p.lineTo(notch_x, ty(bot - 7))
        p.lineTo(min(x_in, x_out), ty(bot))
        p.close()
        c.drawPath(p, fill=1, stroke=0)

    # rosette disc + inner ring
    c.setFillColorRGB(*rgb(FEC_OCHRE))
    c.circle(cx, ty(t), r, fill=1, stroke=0)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.4)
    c.circle(cx, ty(t), 9.0, fill=0, stroke=1)

    # caption, small caps, INK for grayscale legibility
    tracked_text(c, cx, ty(142), "FOR EVERY CHAPTER", "Nunito-Bold", 7.5, 1.4,
                 INK, center=True)


# ------------------------------------------------------------ shared pages

def cover_page(c, cfg):
    """Line-standard cover. cfg keys: EYEBROW, TITLE_LINES, SUBTITLE,
    SPANISH_NOTE (optional), BADGE, TAGLINE, icon_fn (optional callable)."""
    putty_bg(c)

    wm = "M A Y B E W E L L   B O O K S"
    plain_text(c, PAGE_W / 2, ty(74), wm, "Nunito-Bold", 13, INK, center=True)
    wm_w = pdfmetrics.stringWidth(wm, "Nunito-Bold", 13)
    _star(c, PAGE_W / 2 + wm_w / 2 + 15, ty(70), 5.5)

    draw_fec_ribbon(c)

    tracked_text(c, PAGE_W / 2, ty(227), cfg["EYEBROW"], "Nunito-Bold", 11,
                 2.4, INK, center=True)

    size = 40
    while any(pdfmetrics.stringWidth(ln, "Fraunces-Black", size) > CW
              for ln in cfg["TITLE_LINES"]):
        size -= 2
    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", size)
    c.drawCentredString(PAGE_W / 2, ty(298), cfg["TITLE_LINES"][0])
    c.drawCentredString(PAGE_W / 2, ty(346), cfg["TITLE_LINES"][1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(386), 96, 3, fill=1, stroke=0)

    plain_text(c, PAGE_W / 2, ty(420), cfg["SUBTITLE"], "Nunito-XLI", 15, INK,
               center=True)
    if cfg.get("SPANISH_NOTE"):
        plain_text(c, PAGE_W / 2, ty(444), cfg["SPANISH_NOTE"], "Nunito-XLI",
                   12, INK, center=True)

    if cfg.get("icon_fn"):
        cfg["icon_fn"](c)

    badge_w = tracked_width(cfg["BADGE"], "Nunito-Bold", 10, 1.2) + 36
    c.setFillColorRGB(*rgb(OCHRE))
    c.roundRect(PAGE_W / 2 - badge_w / 2, ty(686), badge_w, 22, 11, fill=1, stroke=0)
    tracked_text(c, PAGE_W / 2, ty(679), cfg["BADGE"], "Nunito-Bold", 10, 1.2,
                 INK, center=True)

    plain_text(c, PAGE_W / 2, ty(720), cfg["TAGLINE"], "Nunito-XL", 12, INK,
               center=True)
    tracked_text(c, PAGE_W / 2, ty(755), "maybewellbooks.com", "Nunito-XL", 10,
                 0.54, INK, center=True)
    c.showPage()


def title_page(c, cfg):
    putty_bg(c)
    plain_text(c, PAGE_W / 2, ty(120), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 11, INK, center=True)
    size = 28
    while any(pdfmetrics.stringWidth(ln, "Fraunces-Black", size) > CW
              for ln in cfg["TITLE_LINES"]):
        size -= 2
    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", size)
    c.drawCentredString(PAGE_W / 2, ty(328), cfg["TITLE_LINES"][0])
    c.drawCentredString(PAGE_W / 2, ty(364), cfg["TITLE_LINES"][1])
    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 40, ty(392), 80, 2.5, fill=1, stroke=0)
    plain_text(c, PAGE_W / 2, ty(422), cfg["SUBTITLE"], "Nunito-XLI", 13.5,
               INK, center=True)
    if cfg.get("icon_fn_small"):
        cfg["icon_fn_small"](c)
    plain_text(c, PAGE_W / 2, ty(660), cfg["TAGLINE"], "Nunito-XL", 13, INK,
               center=True)
    c.showPage()


def intro_page(c, cfg, kicker, title, paras, page_num):
    """Large-print intro: 13.5pt body, 20pt leading, labeled two-move rows
    supported via (label, body) tuples."""
    tracked_text(c, M, ty(66), kicker, "Nunito-Bold", 11, 2.4, INK)
    plain_text(c, M, ty(104), title, "Fraunces-Black", 26, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(RULE_W)
    c.line(M, ty(122), PAGE_W - M, ty(122))

    y = 156
    for item in paras:
        if isinstance(item, tuple):
            label, body = item
            tracked_text(c, M, ty(y), label, "Nunito-Bold", 11, 2.4, INK)
            lines = wrap(body, "Nunito-Reg", 13.5, CW - 96)
            yy = y
            for ln in lines:
                plain_text(c, M + 96, ty(yy), ln, "Nunito-Reg", 13.5, INK)
                yy += 20
            y = yy + 11
        else:
            for ln in wrap(item, "Nunito-Reg", 13.5, CW):
                plain_text(c, M, ty(y), ln, "Nunito-Reg", 13.5, INK)
                y += 20
            y += 11

    footer(c, page_num, cfg["TAGLINE"])
    c.showPage()


def divider_page(c, label, title, note):
    putty_bg(c)
    tracked_text(c, PAGE_W / 2, PAGE_H / 2 + 52, label, "Nunito-Bold", 12,
                 2.4, INK, center=True)
    plain_text(c, PAGE_W / 2, PAGE_H / 2 + 6, title, "Fraunces-Black", 32,
               INK, center=True)
    for i, ln in enumerate(wrap(note, "Nunito-XLI", 13.5, CW - 60)):
        plain_text(c, PAGE_W / 2, PAGE_H / 2 - 26 - i * 19, ln, "Nunito-XLI",
                   13.5, INK, center=True)
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.4)
    c.line(PAGE_W / 2 - 65, PAGE_H / 2 - 72, PAGE_W / 2 + 65, PAGE_H / 2 - 72)
    c.showPage()


def _star(c, cx, cy, r):
    import math
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
    c.setFillColorRGB(*rgb(OCHRE))
    c.drawPath(p, fill=1, stroke=0)


def start_canvas(out_path, title, subject):
    from reportlab.pdfgen import canvas as _canvas
    c = _canvas.Canvas(out_path, pagesize=letter)
    c.setTitle(title)
    c.setAuthor("Maybewell Books")
    c.setSubject(subject)
    c.setCreator("anonymous")
    return c
