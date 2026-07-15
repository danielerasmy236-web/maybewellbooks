"""Word search grid generator with 8-direction placement and reportlab rendering."""

import random
import string

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def generate_grid(words, size, seed=None, max_attempts=400):
    rng = random.Random(seed)
    words = sorted(set(w.upper() for w in words), key=len, reverse=True)
    grid = [[None] * size for _ in range(size)]
    placements = {}

    for word in words:
        placed = False
        for _ in range(max_attempts):
            direction = rng.choice(DIRECTIONS)
            dx, dy = direction
            max_x = size - 1 if dx >= 0 else size - 1
            start_x = rng.randrange(size)
            start_y = rng.randrange(size)
            end_x = start_x + dx * (len(word) - 1)
            end_y = start_y + dy * (len(word) - 1)
            if not (0 <= end_x < size and 0 <= end_y < size):
                continue
            ok = True
            cells = []
            for i, ch in enumerate(word):
                x, y = start_x + dx * i, start_y + dy * i
                existing = grid[y][x]
                if existing is not None and existing != ch:
                    ok = False
                    break
                cells.append((x, y))
            if not ok:
                continue
            for (x, y), ch in zip(cells, word):
                grid[y][x] = ch
            placements[word] = cells
            placed = True
            break
        if not placed:
            continue

    for y in range(size):
        for x in range(size):
            if grid[y][x] is None:
                grid[y][x] = rng.choice(string.ascii_uppercase)

    return grid, placements


def render_grid(c, grid, size, x0, y0, area, ink_hex, cell_font=11):
    from mw_lib.brand import _hex_rgb
    cell = area / size
    r, g, b = _hex_rgb(ink_hex)
    c.setFillColorRGB(r, g, b)
    c.setFont("Courier-Bold", cell_font)
    for gy in range(size):
        for gx in range(size):
            ch = grid[gy][gx]
            px = x0 + gx * cell + cell / 2
            py = y0 + (size - gy - 1) * cell + cell / 2 - cell_font * 0.35
            c.drawCentredString(px, py, ch)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1)
    c.rect(x0, y0, area, area, fill=0, stroke=1)
    return cell


def render_solution_overlay(c, placements, size, x0, y0, area, accent_hex):
    from mw_lib.brand import _hex_rgb
    cell = area / size
    r, g, b = _hex_rgb(accent_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(cell * 0.55)
    c.setLineCap(1)
    for word, cells in placements.items():
        (x1, y1), (x2, y2) = cells[0], cells[-1]
        px1 = x0 + x1 * cell + cell / 2
        py1 = y0 + (size - y1 - 1) * cell + cell / 2
        px2 = x0 + x2 * cell + cell / 2
        py2 = y0 + (size - y2 - 1) * cell + cell / 2
        c.line(px1, py1, px2, py2)
