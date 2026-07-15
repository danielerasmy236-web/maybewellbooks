"""Procedural perfect-maze generation and reportlab rendering."""

import random
from collections import deque

N, S, E, W = "N", "S", "E", "W"
OPPOSITE = {N: S, S: N, E: W, W: E}
DELTA = {N: (0, -1), S: (0, 1), E: (1, 0), W: (-1, 0)}


def generate_maze(cols, rows, seed=None):
    rng = random.Random(seed)
    walls = [[{N: True, S: True, E: True, W: True} for _ in range(cols)] for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]

    stack = [(0, 0)]
    visited[0][0] = True
    while stack:
        cx, cy = stack[-1]
        neighbors = []
        for d, (dx, dy) in DELTA.items():
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx]:
                neighbors.append((d, nx, ny))
        if not neighbors:
            stack.pop()
            continue
        d, nx, ny = rng.choice(neighbors)
        walls[cy][cx][d] = False
        walls[ny][nx][OPPOSITE[d]] = False
        visited[ny][nx] = True
        stack.append((nx, ny))

    return walls


def solve_maze(walls, cols, rows, start=(0, 0), end=None):
    if end is None:
        end = (cols - 1, rows - 1)
    q = deque([start])
    came_from = {start: None}
    while q:
        cx, cy = q.popleft()
        if (cx, cy) == end:
            break
        for d, (dx, dy) in DELTA.items():
            if walls[cy][cx][d]:
                continue
            nxt = (cx + dx, cy + dy)
            if nxt not in came_from:
                came_from[nxt] = (cx, cy)
                q.append(nxt)
    path = [end]
    cur = end
    while came_from[cur] is not None:
        cur = came_from[cur]
        path.append(cur)
    path.reverse()
    return path


def render_maze(c, walls, cols, rows, x0, y0, size, ink_hex, path=None, path_hex=None):
    from mw_lib.brand import _hex_rgb
    cell = size / max(cols, rows)
    ox = x0 + (size - cell * cols) / 2
    oy = y0 + (size - cell * rows) / 2

    if path:
        r, g, b = _hex_rgb(path_hex or ink_hex)
        c.setStrokeColorRGB(r, g, b)
        c.setLineWidth(cell * 0.28)
        c.setLineCap(1)
        c.setLineJoin(1)
        p = c.beginPath()
        for i, (cx, cy) in enumerate(path):
            px = ox + (cx + 0.5) * cell
            py = oy + (rows - cy - 0.5) * cell
            if i == 0:
                p.moveTo(px, py)
            else:
                p.lineTo(px, py)
        c.drawPath(p, fill=0, stroke=1)

    r, g, b = _hex_rgb(ink_hex)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(1.4)
    c.setLineCap(0)
    for gy in range(rows):
        for gx in range(cols):
            cx0 = ox + gx * cell
            cy0 = oy + (rows - gy - 1) * cell
            cell_walls = walls[gy][gx]
            if cell_walls[N]:
                c.line(cx0, cy0 + cell, cx0 + cell, cy0 + cell)
            if cell_walls[S]:
                c.line(cx0, cy0, cx0 + cell, cy0)
            if cell_walls[W]:
                c.line(cx0, cy0, cx0, cy0 + cell)
            if cell_walls[E]:
                c.line(cx0 + cell, cy0, cx0 + cell, cy0 + cell)

    # entrance / exit markers
    r, g, b = _hex_rgb(ink_hex)
    c.setFillColorRGB(r, g, b)
    _tri_down(c, ox + 0.5 * cell, oy + rows * cell + 4)
    _tri_down(c, ox + (cols - 0.5) * cell, oy - 4)


def _tri_down(c, cx, top_y):
    p = c.beginPath()
    p.moveTo(cx - 4, top_y + 8)
    p.lineTo(cx + 4, top_y + 8)
    p.lineTo(cx, top_y)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
