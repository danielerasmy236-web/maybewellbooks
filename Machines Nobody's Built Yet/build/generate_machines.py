"""Generate Machines Nobody's Built Yet — Sixty prompts to draw the
inventions that don't exist, yet (letter PDF).

Imagine line, third title. Reuses the DWYI/Impossible Garden pure-drawing-
prompt template: one prompt per page, generous blank space for the drawing,
no difficulty tiers (this is the Imagine line, not the Field Notes ★
system). Production pipeline matches TWIW/Wander: Fraunces (titles) +
Nunito (body) static instances, ReportLab canvas, vector icons only (no
emoji glyphs).

Tc discipline: every tracked (letterspaced) string goes through
tracked_text(), which sets charSpace and always resets it to 0 inside the
same text object — Tc is page-level state in PDF and leaks past ET
otherwise (the known DWYI bug).
"""

import math
import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as _canvas

import content_machines as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_PATH = os.path.join(HERE, "..", "machines-nobodys-built-yet_v1.0_letter.pdf")

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

def draw_star(c, cx, cy, r, filled, color=OCHRE):
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
        c.setFillColorRGB(*rgb(color))
        c.drawPath(p, fill=1, stroke=0)
    else:
        c.setStrokeColorRGB(*rgb(color))
        c.setLineWidth(0.9)
        c.drawPath(p, fill=0, stroke=1)


def draw_infinity(c, cx, cy, r=5.5):
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.4)
    c.circle(cx - r + 1, cy, r, fill=0, stroke=1)
    c.circle(cx + r - 1, cy, r, fill=0, stroke=1)


def draw_gear(c, cx, y_top, scale=1.0):
    """The cover icon: an invented machine's single gear, mid-turn, with a
    small spark of invention catching on its rim — the visual shorthand for
    'built, but not yet real'.
    """
    r = 34 * scale        # tooth-tip radius
    body_r = 25 * scale    # root radius
    pad = 20 * scale
    top_y = ty(y_top)
    cy = top_y - pad - r

    teeth = 8
    tooth_half = (2 * math.pi / teeth) * 0.26
    for i in range(teeth):
        ang = 2 * math.pi * i / teeth
        a0, a1 = ang - tooth_half, ang + tooth_half
        p = c.beginPath()
        p.moveTo(cx + body_r * math.cos(a0), cy + body_r * math.sin(a0))
        p.lineTo(cx + r * math.cos(a0), cy + r * math.sin(a0))
        p.lineTo(cx + r * math.cos(a1), cy + r * math.sin(a1))
        p.lineTo(cx + body_r * math.cos(a1), cy + body_r * math.sin(a1))
        p.close()
        c.setFillColorRGB(*rgb(INK))
        c.drawPath(p, fill=1, stroke=0)

    c.setFillColorRGB(*rgb(PUTTY))
    c.circle(cx, cy, body_r, fill=1, stroke=0)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2.2 * scale)
    c.circle(cx, cy, body_r, fill=0, stroke=1)

    hole_r = body_r * 0.32
    c.setFillColorRGB(*rgb(PUTTY))
    c.circle(cx, cy, hole_r, fill=1, stroke=0)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.2 * scale)
    c.circle(cx, cy, hole_r, fill=0, stroke=1)

    # spark of invention, catching on the rim, upper right
    draw_star(c, cx + r * 0.92, cy + r * 0.68, 7 * scale, True, color=OCHRE)


def footer(c, page_num):
    c.setFillColorRGB(*rgb(OCHRE))
    c.circle(M + 2, ty(745), 2, fill=1, stroke=0)
    plain_text(c, M + 10, ty(747), C.TAGLINE, "Nunito-XL", 8, INK)
    plain_text(c, PAGE_W - M, ty(747), str(page_num), "Nunito-Reg", 8, INK, right=True)


def putty_bg(c):
    c.setFillColorRGB(*rgb(PUTTY))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)


def draw_box(c, top_y, bottom_y):
    """The blank drawing box: dashed ochre rounded rect, with a small star
    ornament (top-left) and a dot (bottom-right) — decoration only, not a
    difficulty indicator (this book has none)."""
    top = ty(top_y)
    bottom = ty(bottom_y)
    c.saveState()
    c.setDash([4, 3])
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.1)
    c.roundRect(M, bottom, CW, top - bottom, 10, fill=0, stroke=1)
    c.restoreState()
    draw_star(c, M + 22, top - 22, 6, False, color=OCHRE)
    c.setFillColorRGB(*rgb(OCHRE))
    c.circle(M + CW - 14, bottom + 14, 2.6, fill=1, stroke=0)


# --------------------------------------------------------------------- pages

def cover(c):
    putty_bg(c)
    wm = "M A Y B E W E L L   B O O K S"
    plain_text(c, PAGE_W / 2, ty(74), wm, "Nunito-Bold", 13, INK, center=True)

    tracked_text(c, PAGE_W / 2, ty(112), C.EYEBROW, "Nunito-Bold", 11, 2.4,
                 OCHRE, center=True)

    c.setFillColorRGB(*rgb(INK))
    c.setFont("Fraunces-Black", 46)
    c.drawCentredString(PAGE_W / 2, ty(190), C.TITLE_LINES[0])
    c.drawCentredString(PAGE_W / 2, ty(242), C.TITLE_LINES[1])

    c.setFillColorRGB(*rgb(OCHRE))
    c.rect(PAGE_W / 2 - 48, ty(280), 96, 3, fill=1, stroke=0)

    for i, ln in enumerate(wrap(C.SUBTITLE, "Nunito-XLI", 15, CW - 40)):
        plain_text(c, PAGE_W / 2, ty(312 + i * 19), ln, "Nunito-XLI", 15, INK,
                   center=True)
    plain_text(c, PAGE_W / 2, ty(360), C.SPANISH_NOTE, "Nunito-XLI", 12, INK,
               center=True)

    draw_gear(c, PAGE_W / 2, 410)

    for i, ln in enumerate(wrap(C.FROM_THE_MAKERS, "Nunito-XLI", 10.5, CW - 120)):
        plain_text(c, PAGE_W / 2, ty(608 + i * 14), ln, "Nunito-XLI", 10.5,
                   INK, center=True)

    badge_w = tracked_width(C.BADGE, "Nunito-Bold", 10, 1.2) + 36
    c.setFillColorRGB(*rgb(OCHRE))
    c.roundRect(PAGE_W / 2 - badge_w / 2, ty(686), badge_w, 22, 11, fill=1, stroke=0)
    tracked_text(c, PAGE_W / 2, ty(679), C.BADGE, "Nunito-Bold", 10, 1.2,
                 PUTTY, center=True)

    plain_text(c, PAGE_W / 2, ty(720), C.TAGLINE, "Nunito-XL", 11, INK, center=True)
    tracked_text(c, PAGE_W / 2, ty(755), "maybewellbooks.com", "Nunito-XL", 9,
                 0.54, INK, center=True)
    c.showPage()


def dedication_page(c, page_num):
    draw_star(c, PAGE_W / 2, ty(78), 6, True)
    plain_text(c, PAGE_W / 2, ty(112), C.DEDICATION, "Nunito-XLI", 12, INK,
               center=True)
    plain_text(c, PAGE_W / 2, ty(158), C.BEFORE_TITLE, "Fraunces-Black", 24,
               INK, center=True)

    y = 200
    for para in C.BEFORE_PARAS:
        for ln in wrap(para, "Nunito-Reg", 11.5, CW):
            plain_text(c, M, ty(y), ln, "Nunito-Reg", 11.5, INK)
            y += 17
        y += 11

    box_w = CW - 80
    box_h = 40
    box_x = M + 40
    box_top = y + 6
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.1)
    c.roundRect(box_x, ty(box_top + box_h), box_w, box_h, box_h / 2, fill=0, stroke=1)
    rule_txt = "Draw what nobody's built, not what already exists."
    plain_text(c, PAGE_W / 2, ty(box_top + box_h / 2 + 4), rule_txt,
               "Nunito-Bold", 12.5, INK, center=True)
    y = box_top + box_h + 34

    plain_text(c, PAGE_W / 2, ty(y), "— With love, Maybewell Books",
               "Nunito-XLI", 11, INK, center=True)

    footer(c, page_num)
    c.showPage()


def how_to_page(c, page_num):
    plain_text(c, M, ty(90), C.HOW_TITLE, "Fraunces-Black", 24, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(106), PAGE_W - M, ty(106))

    y = 138
    for para in C.HOW_PARAS:
        for ln in wrap(para, "Nunito-Reg", 11.5, CW):
            plain_text(c, M, ty(y), ln, "Nunito-Reg", 11.5, INK)
            y += 17
        y += 11

    box_h = 36
    c.setFillColorRGB(*rgb(PUTTY))
    c.roundRect(M, ty(y + box_h), CW, box_h, 8, fill=1, stroke=0)
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.2)
    c.roundRect(M, ty(y + box_h), CW, box_h, 8, fill=0, stroke=1)
    plain_text(c, PAGE_W / 2, ty(y + box_h / 2 + 5), C.HOW_RULE, "Fraunces-SemiBold",
               13, INK, center=True)
    y += box_h + 30

    for para in C.HOW_CLOSING:
        for ln in wrap(para, "Nunito-Reg", 11.5, CW):
            plain_text(c, M, ty(y), ln, "Nunito-Reg", 11.5, INK)
            y += 17
        y += 11

    footer(c, page_num)
    c.showPage()


def toc_page(c, page_num, section_meta):
    plain_text(c, M, ty(90), "What's Inside", "Fraunces-Black", 24, INK)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(106), PAGE_W - M, ty(106))

    y = 148
    for i, (title, note, divider_page, start_p, end_p, count) in enumerate(section_meta):
        plain_text(c, M, ty(y + 8), str(i + 1), "Fraunces-Black", 20, OCHRE)
        plain_text(c, M + 34, ty(y + 4), title, "Fraunces-SemiBold", 15, INK)
        meta_txt = f"prompts #{start_p}–#{end_p}   ·   p.{divider_page}"
        plain_text(c, M + 34, ty(y + 22), meta_txt, "Nunito-Reg", 10, OCHRE)
        yy = y + 40
        for ln in wrap(note, "Nunito-XLI", 10.5, CW - 34):
            plain_text(c, M + 34, ty(yy), ln, "Nunito-XLI", 10.5, INK)
            yy += 14
        y = yy + 16

    footer(c, page_num)
    c.showPage()


NUM_WORDS = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]


def divider_page(c, idx, title, note, count, start_p, end_p):
    putty_bg(c)
    label = f"SECTION {NUM_WORDS[idx]}  ·  {count} PROMPTS"
    tracked_text(c, PAGE_W / 2, PAGE_H / 2 + 52, label, "Nunito-Bold", 11, 2.4,
                 OCHRE, center=True)

    title_lines = wrap(title, "Fraunces-Black", 30, CW)
    title_top = PAGE_H / 2 + 6 + (len(title_lines) - 1) * 17  # extra lines push up
    for i, ln in enumerate(title_lines):
        plain_text(c, PAGE_W / 2, title_top - i * 34, ln, "Fraunces-Black", 30,
                   INK, center=True)
    below_title = title_top - (len(title_lines) - 1) * 34 - 32

    for i, ln in enumerate(wrap(note, "Nunito-XLI", 12, CW - 120)):
        plain_text(c, PAGE_W / 2, below_title - i * 17, ln, "Nunito-XLI",
                   12, INK, center=True)
    rule_y = below_title - 36
    c.setStrokeColorRGB(*rgb(OCHRE))
    c.setLineWidth(1.2)
    c.line(PAGE_W / 2 - 65, rule_y, PAGE_W / 2 + 65, rule_y)
    plain_text(c, PAGE_W / 2, rule_y - 30, f"prompts #{start_p}–#{end_p}",
               "Nunito-Reg", 10, INK, center=True)
    c.showPage()


PROMPT_CIRCLE_R = 24
PROMPT_CIRCLE_CY_TOP = 116


def compute_prompt_layout(prompt, hint):
    """Single source of truth for the prompt-page text layout, shared by the
    generator (to draw it) and the QA scanner (to know where the blank
    drawing box legitimately starts, since its top edge is adaptive)."""
    text_w = CW - (PROMPT_CIRCLE_R * 2 + 20)
    title_lines = wrap(prompt, "Fraunces-SemiBold", 18, text_w)
    y = 104 + len(title_lines) * 24
    y = max(y, PROMPT_CIRCLE_CY_TOP + PROMPT_CIRCLE_R + 4)
    y += 6
    hint_lines = wrap(f"Hint: {hint}", "Nunito-XLI", 12, CW)
    y += len(hint_lines) * 16
    box_top = max(y + 22, 200)
    return title_lines, hint_lines, box_top


def prompt_page(c, section_title, prompt_no, prompt, hint, page_num):
    # header
    tracked_text(c, M, ty(60), section_title.upper(), "Nunito-Bold", 10, 2.0, OCHRE)
    plain_text(c, PAGE_W - M, ty(60), f"No. {prompt_no:02d}", "Fraunces-SemiBold",
               12, INK, right=True)
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.line(M, ty(72), PAGE_W - M, ty(72))

    # number badge + prompt title
    circle_cx = M + PROMPT_CIRCLE_R
    c.setFillColorRGB(*rgb(OCHRE))
    c.circle(circle_cx, ty(PROMPT_CIRCLE_CY_TOP), PROMPT_CIRCLE_R, fill=1, stroke=0)
    plain_text(c, circle_cx, ty(PROMPT_CIRCLE_CY_TOP) - 6, str(prompt_no),
               "Fraunces-SemiBold", 17, PUTTY, center=True)

    title_lines, hint_lines, box_top = compute_prompt_layout(prompt, hint)

    text_x = M + PROMPT_CIRCLE_R * 2 + 20
    y = 104
    for ln in title_lines:
        plain_text(c, text_x, ty(y), ln, "Fraunces-SemiBold", 18, INK)
        y += 24
    y = max(y, PROMPT_CIRCLE_CY_TOP + PROMPT_CIRCLE_R + 4)
    y += 6

    for ln in hint_lines:
        plain_text(c, M, ty(y), ln, "Nunito-XLI", 12, INK)
        y += 16

    draw_box(c, box_top, 706)

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

    draw_gear(c, PAGE_W / 2, 500, scale=0.68)

    plain_text(c, PAGE_W / 2, ty(660), "M A Y B E W E L L   B O O K S",
               "Nunito-Bold", 10, INK, center=True)
    plain_text(c, PAGE_W / 2, ty(682), C.TAGLINE, "Nunito-XL", 10, INK,
               center=True)
    footer(c, page_num)
    c.showPage()


def colophon_page(c, page_num):
    for i, ln in enumerate(wrap(C.COLOPHON_LINE1, "Nunito-Reg", 11, CW - 100)):
        plain_text(c, PAGE_W / 2, ty(392 + i * 16), ln, "Nunito-Reg", 11, INK,
                   center=True)
    y = 392 + len(wrap(C.COLOPHON_LINE1, "Nunito-Reg", 11, CW - 100)) * 16 + 6
    plain_text(c, PAGE_W / 2, ty(y), C.COLOPHON_EDITION, "Nunito-Reg", 11, INK,
               center=True)
    y += 34
    plain_text(c, PAGE_W / 2, ty(y), C.COLOPHON_RIGHTS, "Nunito-Reg", 11, INK,
               center=True)
    y += 34
    for ln in wrap(C.COLOPHON_LICENSE, "Nunito-Reg", 10.5, CW - 140):
        plain_text(c, PAGE_W / 2, ty(y), ln, "Nunito-Reg", 10.5, INK, center=True)
        y += 15
    y += 20
    for ln in wrap(C.COLOPHON_MADE_FOR, "Nunito-Reg", 10.5, CW - 140):
        plain_text(c, PAGE_W / 2, ty(y), ln, "Nunito-Reg", 10.5, INK, center=True)
        y += 15
    y += 24
    tracked_text(c, PAGE_W / 2, ty(y), C.COLOPHON_URL, "Nunito-XL", 9, 0.54,
                 INK, center=True)

    footer(c, page_num)
    c.showPage()


def main():
    register_fonts()
    out = os.path.abspath(OUT_PATH)
    c = _canvas.Canvas(out, pagesize=letter)
    c.setTitle("Machines Nobody's Built Yet — Sixty prompts to draw the "
               "inventions that don't exist, yet")
    c.setAuthor("Maybewell Books")
    c.setSubject("Creative drawing prompts activity book, Imagine line — "
                 "sixty invention prompts, all ages")
    c.setCreator("anonymous")

    # pre-compute page numbers so the TOC and dividers agree
    page = 5
    prompt_counter = 0
    section_meta = []
    for title, note, prompts in C.SECTIONS:
        start_p = prompt_counter + 1
        end_p = prompt_counter + len(prompts)
        section_meta.append((title, note, page, start_p, end_p, len(prompts)))
        page += 1 + len(prompts)
        prompt_counter = end_p
    closing_page_num = page
    colophon_page_num = page + 1

    cover(c)                                  # p1
    dedication_page(c, 2)                     # p2
    how_to_page(c, 3)                         # p3
    toc_page(c, 4, section_meta)              # p4

    prompt_no = 0
    for idx, (title, note, prompts) in enumerate(C.SECTIONS):
        _, _, divider_page_num, start_p, end_p, count = section_meta[idx]
        divider_page(c, idx, title, note, count, start_p, end_p)
        for prompt, hint in prompts:
            prompt_no += 1
            prompt_page(c, title, prompt_no, prompt, hint, divider_page_num + prompt_no - start_p + 1)

    closing_page(c, closing_page_num)
    colophon_page(c, colophon_page_num)

    c.save()
    print(f"wrote {out} ({colophon_page_num} pages)")


if __name__ == "__main__":
    main()
