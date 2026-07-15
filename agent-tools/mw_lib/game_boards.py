"""Reusable paper-game board drawing primitives for reportlab."""

from reportlab.lib.units import inch
from mw_lib.brand import _hex_rgb


def draw_dots(c, x0, y0, w, h, cols, rows, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setFillColorRGB(r, g, b)
    gx = w / (cols - 1)
    gy = h / (rows - 1)
    for i in range(cols):
        for j in range(rows):
            c.circle(x0 + i * gx, y0 + j * gy, 2, fill=1, stroke=0)


def draw_multigrid(c, x0, y0, w, h, n_grids, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1.2)
    gap = 0.25 * inch
    size = min((w - gap * (n_grids - 1)) / n_grids, h)
    for n in range(n_grids):
        gx0 = x0 + n * (size + gap)
        for i in range(1, 3):
            c.line(gx0 + i * size / 3, y0, gx0 + i * size / 3, y0 + size)
            c.line(gx0, y0 + i * size / 3, gx0 + size, y0 + i * size / 3)
        c.rect(gx0, y0, size, size, fill=0, stroke=1)


def draw_grid(c, x0, y0, size_w, size_h, cols, rows, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1)
    cell_w = size_w / cols
    cell_h = size_h / rows
    for i in range(cols + 1):
        c.line(x0 + i * cell_w, y0, x0 + i * cell_w, y0 + size_h)
    for j in range(rows + 1):
        c.line(x0, y0 + j * cell_h, x0 + size_w, y0 + j * cell_h)


def draw_coordgrid(c, x0, y0, size, n, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1)
    cell = size / n
    draw_grid(c, x0, y0, size, size, n, n, ink_hex)
    c.setFillColorRGB(r, g, b)
    c.setFont("Helvetica-Bold", 8)
    letters = "ABCDEFGHIJ"
    for i in range(n):
        c.drawCentredString(x0 + i * cell + cell / 2, y0 + size + 6, letters[i])
        c.drawCentredString(x0 - 10, y0 + size - i * cell - cell / 2 - 3, str(i + 1))


def draw_bingo(c, x0, y0, size, items, ink_hex, accent_hex):
    r, g, b = _hex_rgb(ink_hex)
    draw_grid(c, x0, y0, size, size, 5, 5, ink_hex)
    cell = size / 5
    c.setFont("Helvetica", 7)
    idx = 0
    for row in range(5):
        for col in range(5):
            cx = x0 + col * cell + cell / 2
            cy = y0 + size - row * cell - cell / 2
            if row == 2 and col == 2:
                ra, ga, ba = _hex_rgb(accent_hex)
                c.setFillColorRGB(ra, ga, ba)
                c.setFont("Helvetica-Bold", 8)
                c.drawCentredString(cx, cy - 3, "FREE")
                c.setFillColorRGB(r, g, b)
                c.setFont("Helvetica", 7)
                continue
            word = items[idx % len(items)]
            idx += 1
            import textwrap
            wl = textwrap.wrap(word, 13, break_long_words=False)
            wy = cy + (len(wl) - 1) * 4
            for line in wl:
                c.drawCentredString(cx, wy - 3, line)
                wy -= 8


def draw_hangman(c, x0, y0, ink_hex, blanks=8):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(2)
    c.line(x0, y0, x0, y0 + 1.4 * inch)
    c.line(x0, y0 + 1.4 * inch, x0 + 0.9 * inch, y0 + 1.4 * inch)
    c.line(x0 + 0.9 * inch, y0 + 1.4 * inch, x0 + 0.9 * inch, y0 + 1.2 * inch)
    c.line(x0 - 0.25 * inch, y0, x0 + 0.25 * inch, y0)
    c.setLineWidth(1)
    for i in range(blanks):
        bx = x0 + 1.3 * inch + i * 0.4 * inch
        c.line(bx, y0, bx + 0.3 * inch, y0)


def draw_bracket(c, x0, y0, w, h, n_players, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1)
    import math
    rounds = int(math.log2(n_players))
    slot_h = h / n_players
    xs = [x0 + rc * (w / rounds) for rc in range(rounds + 1)]
    positions = [y0 + h - (i + 0.5) * slot_h for i in range(n_players)]
    cur = positions
    for rc in range(rounds):
        nxt = []
        for i in range(0, len(cur), 2):
            y1, y2 = cur[i], cur[i + 1]
            mid = (y1 + y2) / 2
            c.line(xs[rc], y1, xs[rc] + 0.3 * inch, y1)
            c.line(xs[rc], y2, xs[rc] + 0.3 * inch, y2)
            c.line(xs[rc] + 0.3 * inch, y1, xs[rc] + 0.3 * inch, y2)
            c.line(xs[rc] + 0.3 * inch, mid, xs[rc + 1], mid)
            nxt.append(mid)
        cur = nxt


def draw_categories_table(c, x0, y0, w, categories, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setFillColorRGB(r, g, b)
    c.setFont("Helvetica-Bold", 10)
    row_h = 0.35 * inch
    y = y0
    for i, cat in enumerate(categories):
        c.setFont("Helvetica", 10)
        c.drawString(x0, y - 12, cat)
        c.setLineWidth(0.7)
        c.line(x0 + 1.6 * inch, y - 14, x0 + w * 0.5, y - 14)
        c.line(x0 + w * 0.5 + 0.2 * inch, y - 14, x0 + w, y - 14)
        y -= row_h
    return y


def draw_checklist26(c, x0, y0, w, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setFillColorRGB(r, g, b)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols, rows = 7, 4
    cell = w / cols
    c.setFont("Helvetica-Bold", 11)
    for i, letter in enumerate(letters):
        col = i % cols
        row = i // cols
        cx = x0 + col * cell
        cy = y0 - row * (cell * 0.9)
        c.rect(cx, cy, cell * 0.8, cell * 0.7, fill=0, stroke=1)
        c.drawString(cx + 6, cy + 8, letter)


def draw_fold_template(c, x0, y0, size, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1)
    c.rect(x0, y0, size, size, fill=0, stroke=1)
    c.setDash(3, 3)
    c.line(x0, y0, x0 + size, y0 + size)
    c.line(x0, y0 + size, x0 + size, y0)
    c.line(x0 + size / 2, y0, x0 + size / 2, y0 + size)
    c.line(x0, y0 + size / 2, x0 + size, y0 + size / 2)
    c.setDash()
    c.setFont("Helvetica-Oblique", 8)
    c.setFillColorRGB(r, g, b)
    c.drawCentredString(x0 + size / 2, y0 + size / 2, "fold in")


def draw_dot_to_dot(c, x0, y0, size, points, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setFillColorRGB(r, g, b)
    c.setFont("Helvetica", 7)
    for i, (px, py) in enumerate(points, start=1):
        cx, cy = x0 + px * size, y0 + py * size
        c.circle(cx, cy, 1.6, fill=1, stroke=0)
        c.drawString(cx + 4, cy + 2, str(i))


def draw_word_ladder(c, x0, y0_top, w, start, end, rungs, ink_hex):
    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setFillColorRGB(r, g, b)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(x0 + w / 2, y0_top, start.upper())
    gap = 0.5 * inch
    y = y0_top - gap
    for _ in range(rungs):
        c.setLineWidth(0.8)
        c.line(x0 + w / 2 - 0.9 * inch, y, x0 + w / 2 + 0.9 * inch, y)
        y -= gap
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(x0 + w / 2, y, end.upper())
    return y
