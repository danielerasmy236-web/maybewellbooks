"""Generate the six "For Teachers and Educators" PDFs.

Same pipeline as DWYI / The World Is Watching (ReportLab + instanced
Fraunces/Nunito), but a utilitarian classroom layout:

  - ALL text is ink (#20303A) on white — sheets must survive a black & white
    photocopier. Ochre appears only in tiny decorative shapes, never for
    anything a teacher or student needs to read or play.
  - Every activity is a full sheet: no cards, no cutting. The only fold in
    the whole line is Chain Story's, and that fold IS the activity.
  - Tracked labels go through tracked_text(), which always resets Tc inside
    the same text object (the DWYI Tc-leak guard).
"""

import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as _canvas

import content_teachers as C

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "..", "..", "The World Is Watching", "build", "fonts")
OUT_DIR = os.path.join(HERE, "..")

PAGE_W, PAGE_H = letter
M = 54.0
CW = PAGE_W - 2 * M

INK = "#20303A"
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
    if center:
        x = x - tracked_width(text, font, size, track) / 2
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setFillColorRGB(*rgb(color))
    t.setCharSpace(track)
    t.textOut(text)
    t.setCharSpace(0)
    c.drawText(t)


def plain(c, x, y, text, font, size, color=INK, right=False, center=False):
    c.setFont(font, size)
    c.setFillColorRGB(*rgb(color))
    if right:
        c.drawRightString(x, y, text)
    elif center:
        c.drawCentredString(x, y, text)
    else:
        c.drawString(x, y, text)


def wrap(text, font, size, width):
    words, lines, cur = text.split(), [], ""
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


def para(c, x, y_top, text, font, size, width, leading):
    y = y_top
    for ln in wrap(text, font, size, width):
        plain(c, x, ty(y), ln, font, size)
        y += leading
    return y


def hline(c, x0, x1, y_top, weight=0.8, dashed=False):
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(weight)
    if dashed:
        c.setDash(4, 4)
    c.line(x0, ty(y_top), x1, ty(y_top))
    if dashed:
        c.setDash()


def footer(c, page_num):
    c.setFillColorRGB(*rgb(OCHRE))
    c.circle(M + 2, ty(748), 2, fill=1, stroke=0)
    plain(c, M + 10, ty(750), C.FOOTER, "Nunito-Reg", 7.5)
    plain(c, PAGE_W - M, ty(750), str(page_num), "Nunito-Reg", 7.5, right=True)


def header(c, title, subtitle, tag):
    tracked_text(c, M, ty(52), "MAYBEWELL BOOKS · " + C.LINE_NAME, "Nunito-Bold", 8, 1.4)
    plain(c, PAGE_W - M, ty(52), tag, "Fraunces-SemiBold", 10, right=True)
    hline(c, M, PAGE_W - M, 62, 1.0)
    plain(c, M, ty(94), title, "Fraunces-Black", 25)
    sub_lines = wrap(subtitle, "Nunito-XLI", 11.5, CW)
    for i, ln in enumerate(sub_lines):
        plain(c, M, ty(112 + i * 14), ln, "Nunito-XLI", 11.5)


def teacher_box(c, line, y_top=126):
    """Boxed teacher strip: the only setup info a teacher needs, on-sheet."""
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1)
    c.rect(M, ty(y_top + 24), CW, 24, fill=0, stroke=1)
    size, track = 8.5, 0.9
    while tracked_width(line, "Nunito-Bold", size, track) > CW - 20 and size > 6.5:
        size -= 0.25
    tracked_text(c, PAGE_W / 2, ty(y_top + 15.5), line, "Nunito-Bold", size, track, center=True)
    return y_top + 24


# ------------------------------------------------------------------ chain story

def chain_sheet(c, tag, open_label, open_text, draw_mode, page_num,
                write_own_line=False):
    header(c, C.CHAIN["title"], C.CHAIN["subtitle"], tag)
    y = teacher_box(c, C.CHAIN["teacher_line"]) + 18

    tracked_text(c, M, ty(y), open_label, "Nunito-Bold", 9, 1.6)
    y += 16
    y = para(c, M, y, open_text, "Fraunces-SemiBold", 12.5, CW, 17)
    if write_own_line:
        hline(c, M, PAGE_W - M, y + 8)
        y += 16
    y += 6

    closing_y = 726
    zone_top = y
    zones = 6
    zone_h = (closing_y - 18 - zone_top) / zones
    caption = C.CHAIN["zone_caption_draw"] if draw_mode else C.CHAIN["zone_caption"]
    who = "ARTIST" if draw_mode else "WRITER"
    for i in range(zones):
        zy = zone_top + i * zone_h
        tracked_text(c, M, ty(zy + 10), f"{who} {i + 1}", "Nunito-Bold", 7.5, 1.4)
        if not draw_mode:
            hline(c, M, PAGE_W - M, zy + zone_h * 0.48, 0.7)
            hline(c, M, PAGE_W - M, zy + zone_h * 0.78, 0.7)
        # the fold line, with its instruction sitting right on it
        fold_y = zy + zone_h
        gap_w = pdfmetrics.stringWidth(caption, "Nunito-Reg", 7) + 12
        hline(c, M, PAGE_W / 2 - gap_w / 2, fold_y, 0.8, dashed=True)
        hline(c, PAGE_W / 2 + gap_w / 2, PAGE_W - M, fold_y, 0.8, dashed=True)
        plain(c, PAGE_W / 2, ty(fold_y + 2.5), caption, "Nunito-Reg", 7, center=True)

    plain(c, PAGE_W / 2, ty(closing_y + 10), C.CHAIN["closing"], "Nunito-Bold", 9.5, center=True)
    footer(c, page_num)
    c.showPage()


def chain_closing(c, page_num):
    header(c, C.CHAIN["closing_title"], "The week's best story, unfolded and preserved.", "FRIDAY · WRAP-UP")
    y = para(c, M, 140, C.CHAIN["closing_sub"], "Nunito-Reg", 10.5, CW, 15) + 10
    for i in range(14):
        hline(c, M, PAGE_W - M, y + i * 28, 0.7)
    y += 14 * 28 + 10
    tracked_text(c, M, ty(y), C.CHAIN["closing_note"].upper(), "Nunito-Bold", 8, 1.4)
    hline(c, M + 150, PAGE_W - M, y, 0.7)
    footer(c, page_num)
    c.showPage()


# --------------------------------------------------------------- group detective

def detective_sheet(c, tag, brief, questions, page_num, blank_qs=False):
    header(c, C.DETECTIVE["title"], C.DETECTIVE["subtitle"], tag)
    y = teacher_box(c, C.DETECTIVE["teacher_line"]) + 16
    y = para(c, M, y, brief, "Nunito-Reg", 10, CW, 14) + 8

    box_top = 620
    qspace = (box_top - 14 - y) / len(questions)
    for i, q in enumerate(questions):
        qy = y + i * qspace
        plain(c, M, ty(qy + 12), f"{i + 1}.", "Fraunces-Black", 12)
        if blank_qs:
            hline(c, M + 20, PAGE_W - M, qy + 12, 0.7)          # write the question
            hline(c, M + 20, PAGE_W - M, qy + qspace - 12, 0.7)  # write the answer
        else:
            yy = qy + 12
            for ln in wrap(q, "Fraunces-SemiBold", 11.5, CW - 24):
                plain(c, M + 20, ty(yy), ln, "Fraunces-SemiBold", 11.5)
                yy += 15
            hline(c, M + 20, PAGE_W - M, qy + qspace - 10, 0.7)

    # case solved box
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.4)
    c.rect(M, ty(726), CW, ty(box_top) - ty(726), fill=0, stroke=1)
    tracked_text(c, PAGE_W / 2, ty(box_top + 22), C.DETECTIVE["solved_label"], "Nunito-Bold", 10, 2.2, center=True)
    plain(c, M + 16, ty(box_top + 48), C.DETECTIVE["solved_line"], "Fraunces-SemiBold", 12)
    hline(c, M + 60, PAGE_W - M - 16, box_top + 48, 0.7)
    plain(c, M + 16, ty(box_top + 76), C.DETECTIVE["signed_line"], "Nunito-Reg", 9)
    hline(c, M + 130, PAGE_W - M - 16, box_top + 76, 0.7)
    footer(c, page_num)
    c.showPage()


def detective_closing(c, page_num):
    header(c, C.DETECTIVE["closing_title"], C.DETECTIVE["closing_sub"], "FRIDAY · WRAP-UP")
    # a full-sheet certificate: double border, no cutting
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(2)
    c.rect(M, ty(720), CW, ty(160) - ty(720), fill=0, stroke=1)
    c.setLineWidth(0.8)
    c.rect(M + 8, ty(712), CW - 16, ty(168) - ty(712), fill=0, stroke=1)

    tracked_text(c, PAGE_W / 2, ty(240), "OFFICIAL FINDING · MAYBEWELL BUREAU OF SMALL DISCOVERIES",
                 "Nunito-Bold", 8, 1.6, center=True)
    plain(c, PAGE_W / 2, ty(296), "Certificate", "Fraunces-Black", 34, center=True)
    plain(c, PAGE_W / 2, ty(330), "of Detection", "Fraunces-Black", 22, center=True)

    fields = C.DETECTIVE["closing_fields"]
    plain(c, PAGE_W / 2, ty(392), fields[0], "Nunito-Reg", 11, center=True)
    hline(c, M + 90, PAGE_W - M - 90, 424, 0.8)
    plain(c, PAGE_W / 2, ty(456), fields[1], "Nunito-Reg", 11, center=True)
    hline(c, M + 60, PAGE_W - M - 60, 492, 0.8)
    hline(c, M + 60, PAGE_W - M - 60, 524, 0.8)
    plain(c, PAGE_W / 2, ty(560), fields[2], "Nunito-Reg", 11, center=True)
    hline(c, M + 150, PAGE_W - M - 150, 592, 0.8)

    import math
    for k in (-1, 1):
        cx = PAGE_W / 2 + k * 190
        pts = []
        for i in range(10):
            ang = math.pi / 2 + i * math.pi / 5
            rad = 11 if i % 2 == 0 else 4.6
            pts.append((cx + rad * math.cos(ang), ty(660) + rad * math.sin(ang)))
        p = c.beginPath()
        p.moveTo(*pts[0])
        for pt in pts[1:]:
            p.lineTo(*pt)
        p.close()
        c.setFillColorRGB(*rgb(INK))
        c.drawPath(p, fill=1, stroke=0)
    tracked_text(c, PAGE_W / 2, ty(664), "CASE CLOSED", "Nunito-Bold", 9, 2.4, center=True)
    footer(c, page_num)
    c.showPage()


# ----------------------------------------------------------- build without words

def silent_sheet(c, tag, constraint, page_num, grid=False, mural=False):
    header(c, C.SILENT["title"], C.SILENT["subtitle"], tag)
    y = teacher_box(c, C.SILENT["teacher_line"]) + 16

    for i, rule in enumerate(C.SILENT["rules"]):
        plain(c, M, ty(y + 2), f"{i + 1}.", "Fraunces-Black", 10.5)
        yy = y
        for ln in wrap(rule, "Nunito-Reg", 9.5, CW - 22):
            plain(c, M + 18, ty(yy), ln, "Nunito-Reg", 9.5)
            yy += 12.5
        y = yy + 3
    y += 4
    if constraint:
        yy = y
        for ln in wrap(constraint, "Nunito-Bold", 9.5, CW):
            plain(c, M, ty(yy), ln, "Nunito-Bold", 9.5)
            yy += 12.5
        y = yy + 4

    top, bottom = y + 6, 726
    c.setStrokeColorRGB(*rgb(INK))
    c.setLineWidth(1.2)
    c.rect(M, ty(bottom), CW, ty(top) - ty(bottom), fill=0, stroke=1)
    tracked_text(c, M + 10, ty(top + 16), C.SILENT["canvas_label"], "Nunito-Bold", 7.5, 1.4)

    if grid:
        h = bottom - top
        c.setLineWidth(0.6)
        c.line(M + CW / 2, ty(top), M + CW / 2, ty(bottom))
        for k in (1, 2):
            c.line(M, ty(top + h * k / 3), PAGE_W - M, ty(top + h * k / 3))
    if mural:
        # edge-connection marks: short ticks crossing each edge at 25% / 75%
        c.setLineWidth(1.6)
        h = bottom - top
        for f in (0.25, 0.75):
            c.line(M + CW * f, ty(top - 5), M + CW * f, ty(top + 5))
            c.line(M + CW * f, ty(bottom - 5), M + CW * f, ty(bottom + 5))
            c.line(M - 5, ty(top + h * f), M + 5, ty(top + h * f))
            c.line(PAGE_W - M - 5, ty(top + h * f), PAGE_W - M + 5, ty(top + h * f))
    footer(c, page_num)
    c.showPage()


def silent_closing(c, page_num):
    header(c, C.SILENT["closing_title"], C.SILENT["closing_sub"], "FRIDAY · WRAP-UP")
    y = 150
    for i, step in enumerate(C.SILENT["closing_steps"]):
        plain(c, M, ty(y + 2), f"{i + 1}.", "Fraunces-Black", 12)
        yy = y
        for ln in wrap(step, "Nunito-Reg", 10.5, CW - 24):
            plain(c, M + 22, ty(yy), ln, "Nunito-Reg", 10.5)
            yy += 15
        y = yy + 10

    # little assembly diagram: 3x2 taped grid
    gx, gy, gw, gh, gap = M + 90, y + 30, 100, 74, 8
    c.setStrokeColorRGB(*rgb(INK))
    for row in range(2):
        for col in range(3):
            x0 = gx + col * (gw + gap)
            y0 = gy + row * (gh + gap)
            c.setLineWidth(1)
            c.rect(x0, ty(y0 + gh), gw, gh, fill=0, stroke=1)
    c.setLineWidth(0.8)
    c.setDash(3, 3)
    for col in range(1, 3):
        xm = gx + col * (gw + gap) - gap / 2
        c.line(xm, ty(gy + 2 * gh + gap), xm, ty(gy))
    ym = gy + gh + gap / 2
    c.line(gx, ty(ym), gx + 3 * gw + 2 * gap, ty(ym))
    c.setDash()
    plain(c, gx + (3 * gw + 2 * gap) / 2, ty(gy + 2 * gh + gap + 26),
          "dashed = tape on the back", "Nunito-XLI", 9, center=True)
    footer(c, page_num)
    c.showPage()


# --------------------------------------------------------------- shared pages

def guide_page(c, product, page_num):
    header(c, "Teacher's Quick Guide", product["title"] + " — everything useful, nothing else.", "NOTES")
    y = 150
    for h, b in product["guide"]:
        tracked_text(c, M, ty(y), h.upper(), "Nunito-Bold", 9, 1.6)
        y += 15
        y = para(c, M, y, b, "Nunito-Reg", 10.5, CW, 14.5) + 10
    footer(c, page_num)
    c.showPage()


def intro_page(c, product, days_line_fn, page_num):
    header(c, product["title"], "Weekly Module — one class period per day, five days.", "TEACHER INTRO")
    y = 150
    tracked_text(c, M, ty(y), "THE WEEK'S ARC", "Nunito-Bold", 9, 1.6)
    y += 15
    y = para(c, M, y, product["week_arc"], "Nunito-Reg", 10.5, CW, 14.5) + 14

    tracked_text(c, M, ty(y), "THE WEEK AT A GLANCE", "Nunito-Bold", 9, 1.6)
    y += 18
    for d in product["days"]:
        plain(c, M, ty(y), d[0], "Fraunces-SemiBold", 10.5)
        y = para(c, M + 100, y, days_line_fn(d), "Nunito-Reg", 10, CW - 100, 13.5) + 6

    y += 8
    tracked_text(c, M, ty(y), "ONE TIP", "Nunito-Bold", 9, 1.6)
    y += 15
    y = para(c, M, y, product["week_tip"], "Nunito-Reg", 10.5, CW, 14.5) + 12

    y += 6
    y = para(c, M, y, "This module is enrichment — a supplement to your own plans, not a "
                      "curriculum. Print one sheet per group per day, and photocopy freely "
                      "for your own classroom.", "Nunito-XLI", 9.5, CW, 13)
    footer(c, page_num)
    c.showPage()


def new_doc(path, title, subject):
    c = _canvas.Canvas(path, pagesize=letter)
    c.setTitle(title)
    c.setAuthor("Maybewell Books")
    c.setSubject(subject)
    c.setCreator("anonymous")
    return c


def main():
    register_fonts()
    made = []

    # ---- Chain Story
    p = os.path.join(OUT_DIR, "chain-story-single-sheet_v1.0_letter.pdf")
    c = new_doc(p, "Chain Story — Single-Sheet Activity",
                "Fold-and-pass collaborative storytelling on one printable sheet. No prep, no cutting.")
    chain_sheet(c, "SINGLE SHEET", *C.CHAIN["single_open"], False, 1)
    guide_page(c, C.CHAIN, 2)
    chain_sheet(c, "ALTERNATE SHEET", *C.CHAIN["single_alt_open"], False, 3)
    c.save(); made.append(p)

    p = os.path.join(OUT_DIR, "chain-story-weekly-module_v1.0_letter.pdf")
    c = new_doc(p, "Chain Story — Weekly Module",
                "Five days of fold-and-pass storytelling, one genre per day, plus a Friday story gallery.")
    intro_page(c, C.CHAIN, lambda d: f"{d[1]} — “{d[3][:64]}…”" if len(d[3]) > 64 else f"{d[1]} — “{d[3]}”", 1)
    for i, (day, genre, label, text, draw_mode) in enumerate(C.CHAIN["days"]):
        chain_sheet(c, f"{day} · DAY {i + 1}", label, text, draw_mode, i + 2,
                    write_own_line=(day == "FRIDAY"))
    chain_closing(c, 7)
    c.save(); made.append(p)

    # ---- Group Detective
    p = os.path.join(OUT_DIR, "group-detective-single-sheet_v1.0_letter.pdf")
    c = new_doc(p, "Group Detective — Single-Sheet Activity",
                "A structured investigation that helps a small group find a real thing they share.")
    detective_sheet(c, "SINGLE SHEET", C.DETECTIVE["brief"], C.DETECTIVE["single_qs"], 1)
    guide_page(c, C.DETECTIVE, 2)
    detective_sheet(c, "ALTERNATE SHEET", C.DETECTIVE["brief"], C.DETECTIVE["single_alt_qs"], 3)
    c.save(); made.append(p)

    p = os.path.join(OUT_DIR, "group-detective-weekly-module_v1.0_letter.pdf")
    c = new_doc(p, "Group Detective — Weekly Module",
                "Five cases in five days: experiences, preferences, fears and dreams, family patterns, and an open case.")
    intro_page(c, C.DETECTIVE, lambda d: f"{d[1]} — {d[2]}", 1)
    for i, (day, theme, case, qs) in enumerate(C.DETECTIVE["days"]):
        detective_sheet(c, f"{day} · DAY {i + 1}", case, qs, i + 2, blank_qs=(day == "FRIDAY"))
    detective_closing(c, 7)
    c.save(); made.append(p)

    # ---- Build Without Words
    p = os.path.join(OUT_DIR, "build-without-words-single-sheet_v1.0_letter.pdf")
    c = new_doc(p, "Build Without Words — Single-Sheet Activity",
                "A silent collaborative drawing on one shared sheet. Works as a calming or transition activity.")
    silent_sheet(c, "SINGLE SHEET", None, 1)
    guide_page(c, C.SILENT, 2)
    silent_sheet(c, "ALTERNATE SHEET", C.SILENT["single_alt_note"], 3, grid=True)
    c.save(); made.append(p)

    p = os.path.join(OUT_DIR, "build-without-words-weekly-module_v1.0_letter.pdf")
    c = new_doc(p, "Build Without Words — Weekly Module",
                "Five silent scenes with one new constraint per day, ending in a taped-edge class mural.")
    intro_page(c, C.SILENT, lambda d: f"{d[1]} — {d[2]}", 1)
    for i, (day, theme, constraint) in enumerate(C.SILENT["days"]):
        silent_sheet(c, f"{day} · DAY {i + 1}", "TODAY: " + constraint, i + 2,
                     mural=(day == "FRIDAY"))
    silent_closing(c, 7)
    c.save(); made.append(p)

    for m in made:
        print("wrote", os.path.abspath(m))


if __name__ == "__main__":
    main()
