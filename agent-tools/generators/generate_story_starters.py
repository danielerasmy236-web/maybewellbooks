import sys
import os
import textwrap

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mw_lib import brand
from content import story_starters_content as ct
from reportlab.lib.units import inch


def _prompt_page(c, page_num, category_label, index, total, prompt_text, accent, layout, wrap_width=58):
    c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
    c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)

    c.setFillColorRGB(*brand._hex_rgb(accent))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, f"{category_label.upper()} · #{index} OF {total}")

    c.setFillColorRGB(*brand._hex_rgb(brand.INK))
    c.setFont("Helvetica-Bold", 16)
    lines = textwrap.wrap(prompt_text, wrap_width)
    y = brand.PAGE_H - 1.4 * inch
    for line in lines:
        c.drawString(brand.MARGIN, y, line)
        y -= 0.3 * inch

    y -= 0.25 * inch
    if layout == "ruled":
        brand.draw_ruled_lines(c, brand.MARGIN, y, brand.PAGE_W - 2 * brand.MARGIN, 14, 0.35 * inch, brand.INK)
    else:
        box_h = y - 1.0 * inch
        brand.draw_blank_box(c, brand.MARGIN, 1.0 * inch, brand.PAGE_W - 2 * brand.MARGIN, box_h, brand.INK)

    brand.draw_footer(c, page_num, accent)
    c.showPage()


def build(output_path):
    c = brand.new_canvas(output_path, "Story Starters", "60 writing prompts: first lines, last lines, and impossible situations")
    accent = getattr(brand, ct.ACCENT)

    brand.draw_cover(c, ct.TITLE, ct.SUBTITLE, ct.TAGLINE, accent)
    brand.draw_intro_page(c, "Welcome, Writer", ct.INTRO_BODY, accent)

    page_num = 3
    sections = [
        ("First Lines", ct.FIRST_LINES, "Start here. Write what happens next."),
        ("Last Lines", ct.LAST_LINES, "Work backward. What led here?"),
        ("Impossible Situations", ct.IMPOSSIBLE_SITUATIONS, "Whatever the rule is, follow it seriously."),
    ]

    for name, prompts, note in sections:
        label = f"{len(prompts)} PROMPTS · {name.upper()}"
        brand.draw_section_divider(c, label, name, accent, note)
        page_num += 1
        for i, prompt in enumerate(prompts, start=1):
            layout = "ruled" if i % 2 == 1 else "blank"
            _prompt_page(c, page_num, name, i, len(prompts), prompt, accent, layout)
            page_num += 1

    brand.draw_section_divider(c, "BONUS", "Finish This Story", accent, "Three openings. You write the rest.")
    page_num += 1

    for story in ct.FINISH_THIS_STORY:
        c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
        c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)
        c.setFillColorRGB(*brand._hex_rgb(accent))
        c.setFont("Helvetica-Bold", 10)
        c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, "FINISH THIS STORY")
        c.setFillColorRGB(*brand._hex_rgb(brand.INK))
        c.setFont("Helvetica-Bold", 18)
        c.drawString(brand.MARGIN, brand.PAGE_H - 1.3 * inch, story["title"])
        c.setFont("Helvetica", 11)
        lines = textwrap.wrap(story["body"], 62)
        y = brand.PAGE_H - 1.8 * inch
        for line in lines:
            c.drawString(brand.MARGIN, y, line)
            y -= 0.24 * inch
        y -= 0.2 * inch
        brand.draw_ruled_lines(c, brand.MARGIN, y, brand.PAGE_W - 2 * brand.MARGIN, 10, 0.34 * inch, brand.INK)
        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

        # second page of ruled lines to keep writing
        c.setFillColorRGB(*brand._hex_rgb(brand.CREAM))
        c.rect(0, 0, brand.PAGE_W, brand.PAGE_H, fill=1, stroke=0)
        c.setFillColorRGB(*brand._hex_rgb(accent))
        c.setFont("Helvetica-Oblique", 10)
        c.drawString(brand.MARGIN, brand.PAGE_H - 0.9 * inch, f"...{story['title']}, continued")
        brand.draw_ruled_lines(c, brand.MARGIN, brand.PAGE_H - 1.4 * inch, brand.PAGE_W - 2 * brand.MARGIN, 24, 0.34 * inch, brand.INK)
        brand.draw_footer(c, page_num, accent)
        c.showPage()
        page_num += 1

    c.save()
    return page_num - 1


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/story_starters.pdf"
    total_pages = build(out)
    print(f"Generated {out} with {total_pages} pages")
