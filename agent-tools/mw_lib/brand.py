"""Shared MAYBEWELL BOOKS brand kit for reportlab-generated activity books.

Colors and layout conventions are reverse-engineered from the live site
(Website - Repos/maybewell-site-dist-v2) and the two existing published
books, so new products look like they belong on the same shelf.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas as _canvas

# --- palette (matches the Q color object in the site bundle) ---
OCHRE = "#D99A2B"
TEAL = "#2A9D8F"
CORAL = "#E8604C"
VIOLET = "#7C6FD0"
PLUM = "#B5537F"
SAGE = "#6A994E"
SLATE = "#47609C"
INK = "#20303A"
CREAM = "#F3EEE6"

PAGE_W, PAGE_H = letter
MARGIN = 0.75 * inch

AUTHOR = "Maybewell Books"
CREATOR = "anonymous"
SITE_URL = "maybewellbooks.com"


def new_canvas(path, title, subject):
    c = _canvas.Canvas(path, pagesize=letter)
    c.setTitle(title)
    c.setAuthor(AUTHOR)
    c.setSubject(subject)
    c.setCreator(CREATOR)
    return c


def _hex_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) / 255 for i in (0, 2, 4))


def draw_cover(c, title, subtitle, tagline, accent_hex, badge="A CREATIVITY BOOK"):
    c.setFillColorRGB(*_hex_rgb(CREAM))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    r, g, b = _hex_rgb(INK)
    c.setFillColorRGB(r, g, b)
    c.setFont("Helvetica-Bold", 13)
    wordmark = " ".join("MAYBEWELL BOOKS")
    c.drawCentredString(PAGE_W / 2, PAGE_H - 1.6 * inch, wordmark)

    r, g, b = _hex_rgb(accent_hex)
    c.setFillColorRGB(r, g, b)
    star_cx, star_y = PAGE_W / 2 + 1.55 * inch, PAGE_H - 1.66 * inch
    _draw_star(c, star_cx, star_y, 5)

    r, g, b = _hex_rgb(INK)
    c.setFillColorRGB(r, g, b)
    c.setFont("Helvetica-Bold", 34)
    lines = title.split("\n")
    y = PAGE_H - 2.7 * inch
    for line in lines:
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 0.5 * inch

    c.setFont("Helvetica-Oblique", 15)
    c.setFillColorRGB(*_hex_rgb(INK))
    c.drawCentredString(PAGE_W / 2, y - 0.15 * inch, subtitle)

    badge_w = c.stringWidth(badge, "Helvetica-Bold", 10) + 28
    badge_y = 2.2 * inch
    c.setFillColorRGB(*_hex_rgb(accent_hex))
    c.roundRect(PAGE_W / 2 - badge_w / 2, badge_y, badge_w, 22, 11, fill=1, stroke=0)
    c.setFillColorRGB(*_hex_rgb(CREAM))
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(PAGE_W / 2, badge_y + 7, badge)

    c.setFillColorRGB(*_hex_rgb(INK))
    c.setFont("Helvetica", 10)
    c.drawCentredString(PAGE_W / 2, 1.7 * inch, tagline)

    c.setFont("Helvetica", 9)
    c.setFillColorRGB(*_hex_rgb(INK))
    c.drawCentredString(PAGE_W / 2, 1.0 * inch, SITE_URL)

    c.showPage()


def _draw_star(c, cx, cy, r):
    import math
    points = []
    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.42
        points.append((cx + rad * math.cos(angle), cy + rad * math.sin(angle)))
    p = c.beginPath()
    p.moveTo(*points[0])
    for pt in points[1:]:
        p.lineTo(*pt)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def draw_section_divider(c, count_label, title, accent_hex, note=None):
    c.setFillColorRGB(*_hex_rgb(CREAM))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    c.setFillColorRGB(*_hex_rgb(accent_hex))
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 0.6 * inch, count_label.upper())

    c.setFillColorRGB(*_hex_rgb(INK))
    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2, title.upper())

    if note:
        c.setFont("Helvetica-Oblique", 11)
        c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 0.4 * inch, note)

    c.setStrokeColorRGB(*_hex_rgb(accent_hex))
    c.setLineWidth(1.2)
    c.line(PAGE_W / 2 - 0.9 * inch, PAGE_H / 2 - 0.7 * inch, PAGE_W / 2 + 0.9 * inch, PAGE_H / 2 - 0.7 * inch)

    c.showPage()


def draw_footer(c, page_num, accent_hex, label=None):
    c.setFillColorRGB(*_hex_rgb(accent_hex))
    c.circle(MARGIN, 0.55 * inch, 2, fill=1, stroke=0)
    c.setFillColorRGB(*_hex_rgb(INK))
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 8, 0.5 * inch, label or SITE_URL)
    c.drawRightString(PAGE_W - MARGIN, 0.5 * inch, str(page_num))


def draw_ruled_lines(c, x0, y0_top, width, num_lines, gap, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(0.6)
    y = y0_top
    for _ in range(num_lines):
        c.line(x0, y, x0 + width, y)
        y -= gap
    return y


def draw_blank_box(c, x0, y0, width, height, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1)
    c.setDash(3, 3)
    c.rect(x0, y0, width, height, fill=0, stroke=1)
    c.setDash()


def draw_intro_page(c, title, body_lines, accent_hex):
    c.setFillColorRGB(*_hex_rgb(CREAM))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    c.setFillColorRGB(*_hex_rgb(accent_hex))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN, PAGE_H - 1.4 * inch, "HOW TO USE THIS BOOK")

    c.setFillColorRGB(*_hex_rgb(INK))
    c.setFont("Helvetica-Bold", 22)
    c.drawString(MARGIN, PAGE_H - 1.8 * inch, title)

    c.setFont("Helvetica", 11)
    y = PAGE_H - 2.4 * inch
    for line in body_lines:
        c.drawString(MARGIN, y, line)
        y -= 0.28 * inch

    draw_footer(c, 2, accent_hex)
    c.showPage()
