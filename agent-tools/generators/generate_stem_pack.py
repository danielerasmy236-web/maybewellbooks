import sys
import os
import math
import textwrap

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mw_lib import brand, game_boards as gb
from content import stem_pack_content as ct
from reportlab.lib.units import inch


def _page_bg(c):
    c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
    c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)


def _header(c, n, title, brief, accent):
    c.setFillColorRGB(*brand._hex_rgb(accent))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, f"PROJECT #{n} OF 12")
    c.setFillColorRGB(*brand._hex_rgb(brand.INK))
    c.setFont("Helvetica-Bold", 18)
    c.drawString(brand.MARGIN, brand.PAGE_H - 1.25 * inch, title)
    c.setFont("Helvetica", 10)
    y = brand.PAGE_H - 1.6 * inch
    for line in textwrap.wrap(brief, 82):
        c.drawString(brand.MARGIN, y, line)
        y -= 0.2 * inch
    return y - 0.25 * inch


def render_project(c, proj, page_num, accent):
    _page_bg(c)
    top = _header(c, proj["n"], proj["title"], proj["brief"], accent)
    ink = brand.INK
    area_w = brand.PAGE_W - 2 * brand.MARGIN
    bottom = 1.0 * inch
    cx = brand.PAGE_W / 2
    t = proj["type"]

    if t == "sundial":
        r = 2.1 * inch
        cy0 = (top + bottom) / 2 + 0.5 * inch
        c.setStrokeColorRGB(*brand._hex_rgb(ink))
        c.setLineWidth(1.4)
        c.circle(cx, cy0, r, fill=0, stroke=1)
        c.setFont("Helvetica-Bold", 9)
        for h in range(12):
            ang = math.pi * (h / 11) if False else math.pi - h * (math.pi / 11)
            x, y = cx + r * 0.85 * math.cos(ang), cy0 + r * 0.85 * math.sin(ang)
            c.drawCentredString(x, y - 4, str(6 + h) if 6 + h <= 12 else str(6 + h - 12))
        c.setDash(3, 3)
        c.line(cx - r, cy0, cx + r, cy0)
        c.setDash()
        gx0, gy0 = brand.MARGIN + 0.6 * inch, bottom + 0.2 * inch
        c.setLineWidth(1.4)
        p = c.beginPath()
        p.moveTo(gx0, gy0)
        p.lineTo(gx0 + 1.6 * inch, gy0)
        p.lineTo(gx0, gy0 + 1.2 * inch)
        p.close()
        c.drawPath(p, fill=0, stroke=1)
        c.setDash(2, 2)
        c.line(gx0, gy0, gx0, gy0 + 1.2 * inch)
        c.setDash()
        c.setFont("Helvetica-Oblique", 8)
        c.drawString(gx0, gy0 - 14, "cut solid, fold dashed (gnomon)")

    elif t == "constellation":
        data = ct.CONSTELLATIONS[proj["stars"]]
        size = min(area_w, top - bottom, 4.6 * inch)
        x0 = brand.MARGIN + (area_w - size) / 2
        y0 = bottom + (top - bottom - size) / 2
        gb.draw_dot_to_dot(c, x0, y0, size, data["points"], ink)
        c.setFont("Helvetica-Oblique", 10)
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawCentredString(cx, y0 - 0.3 * inch, data["label"])

    elif t == "moonwheel":
        names = ["New Moon", "Waxing\nCrescent", "First\nQuarter", "Waxing\nGibbous",
                 "Full Moon", "Waning\nGibbous", "Last\nQuarter", "Waning\nCrescent"]
        r_big = 2.3 * inch
        cy0 = (top + bottom) / 2 + 0.3 * inch
        for i, name in enumerate(names):
            ang = i * (2 * math.pi / 8) - math.pi / 2
            x = cx + r_big * math.cos(ang)
            y = cy0 + r_big * math.sin(ang)
            c.setStrokeColorRGB(*brand._hex_rgb(ink))
            c.setLineWidth(1.2)
            c.circle(x, y, 0.32 * inch, fill=0, stroke=1)
            c.setFont("Helvetica", 7)
            c.setFillColorRGB(*brand._hex_rgb(ink))
            for j, line in enumerate(name.split("\n")):
                c.drawCentredString(x, y - 0.32 * inch - 10 - j * 9, line)

    elif t == "mathsheet":
        problems = ct.FUEL_PROBLEMS if proj["problems"] == "fuel" else ct.COUNTDOWN_PROBLEMS
        y = top
        c.setFont("Helvetica", 11)
        for i, prob in enumerate(problems, start=1):
            c.setFillColorRGB(*brand._hex_rgb(ink))
            lines = textwrap.wrap(f"{i}. {prob}", 78)
            for line in lines:
                c.drawString(brand.MARGIN, y, line)
                y -= 0.24 * inch
            c.setFont("Helvetica-Bold", 10)
            c.drawString(brand.MARGIN, y - 0.05 * inch, "Answer: ______________")
            c.setFont("Helvetica", 11)
            y -= 0.55 * inch

    elif t == "starfinder":
        r = 2.3 * inch
        cy0 = (top + bottom) / 2 + 0.3 * inch
        c.setStrokeColorRGB(*brand._hex_rgb(ink))
        c.setLineWidth(1.4)
        c.circle(cx, cy0, r, fill=0, stroke=1)
        months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
        c.setFont("Helvetica-Bold", 8)
        for i, m in enumerate(months):
            ang = i * (2 * math.pi / 12) - math.pi / 2
            x = cx + r * 0.85 * math.cos(ang)
            y = cy0 + r * 0.85 * math.sin(ang)
            c.drawCentredString(x, y - 3, m)
        c.setLineWidth(1)
        c.ellipse(cx - r * 0.45, cy0 - r * 0.6, cx + r * 0.45, cy0 + r * 0.6, fill=0, stroke=1)
        c.setFont("Helvetica-Oblique", 8)
        c.drawCentredString(cx, cy0 - r - 18, "cut out both circles, layer, pin at the center, and rotate")

    elif t == "scale":
        c.setFont("Helvetica-Bold", 11)
        y = top
        for name, desc in ct.SCALE_ROWS:
            c.setFillColorRGB(*brand._hex_rgb(ink))
            c.drawString(brand.MARGIN, y, name)
            c.setFont("Helvetica", 10)
            c.drawString(brand.MARGIN + 1.4 * inch, y, desc)
            c.setFont("Helvetica-Bold", 11)
            y -= 0.34 * inch

    elif t == "design":
        brand.draw_blank_box(c, brand.MARGIN, bottom + 0.6 * inch, area_w, top - bottom - 0.6 * inch, ink)
        labels = ["Power source", "Life support", "Propulsion", "Landing / return"]
        c.setFont("Helvetica", 9)
        yy = bottom + 0.4 * inch
        c.setFillColorRGB(*brand._hex_rgb(ink))
        c.drawString(brand.MARGIN, yy, "Label these on your design: " + "  •  ".join(labels))

    elif t == "experiment":
        c.setFont("Helvetica-Bold", 10)
        c.setFillColorRGB(*brand._hex_rgb(ink))
        headers = ["Object", "My prediction", "What happened"]
        colw = area_w / 3
        y = top
        for i, h in enumerate(headers):
            c.drawString(brand.MARGIN + i * colw, y, h)
        y -= 0.1 * inch
        c.line(brand.MARGIN, y, brand.PAGE_W - brand.MARGIN, y)
        y -= 0.35 * inch
        c.setFont("Helvetica", 10)
        for row in ct.EXPERIMENT_TABLE_ROWS:
            c.drawString(brand.MARGIN, y, row)
            c.line(brand.MARGIN + colw, y - 3, brand.MARGIN + 2 * colw - 10, y - 3)
            c.line(brand.MARGIN + 2 * colw, y - 3, brand.PAGE_W - brand.MARGIN, y - 3)
            y -= 0.6 * inch

    elif t == "namestars":
        import random
        rng = random.Random(99)
        pts = [(rng.uniform(0.1, 0.9), rng.uniform(0.1, 0.9)) for _ in range(7)]
        size = min(area_w, 3.2 * inch)
        x0 = brand.MARGIN + (area_w - size) / 2
        y0 = bottom + 1.6 * inch
        gb.draw_dot_to_dot(c, x0, y0, size, pts, ink)
        c.setFont("Helvetica", 10)
        c.drawCentredString(cx, y0 - 0.2 * inch, "Constellation name: ______________________")
        brand.draw_ruled_lines(c, brand.MARGIN, y0 - 0.6 * inch, area_w, 3, 0.3 * inch, ink)

    brand.draw_footer(c, page_num, accent)


def build(output_path):
    c = brand.new_canvas(output_path, "Space STEM Pack", "12 hands-on space science and math projects")
    accent = getattr(brand, ct.ACCENT)

    brand.draw_cover(c, ct.TITLE, ct.SUBTITLE, "maybewellbooks.com", accent)
    brand.draw_intro_page(c, "Mission Briefing", ct.INTRO_BODY, accent)

    page_num = 3
    for proj in ct.PROJECTS:
        render_project(c, proj, page_num, accent)
        c.showPage()
        page_num += 1

    brand.draw_section_divider(c, "FOR PARENTS & TEACHERS", "Notes", accent)
    page_num += 1
    c.setFillColorRGB(*brand._hex_rgb(brand.INK))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(brand.MARGIN, brand.PAGE_H - 1.0 * inch, "TEACHER NOTES")
    y = brand.PAGE_H - 1.4 * inch
    for label, note in ct.TEACHER_NOTES:
        c.setFont("Helvetica-Bold", 11)
        c.drawString(brand.MARGIN, y, label)
        y -= 0.24 * inch
        c.setFont("Helvetica", 10)
        for line in textwrap.wrap(note, 82):
            c.drawString(brand.MARGIN, y, line)
            y -= 0.22 * inch
        y -= 0.2 * inch
    brand.draw_footer(c, page_num, accent)
    c.showPage()
    page_num += 1

    c.save()
    return page_num - 1


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/stem_pack.pdf"
    total_pages = build(out)
    print(f"Generated {out} with {total_pages} pages")
