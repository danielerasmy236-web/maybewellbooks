"""Simple vector nature-icon drawing for The Autumn Book."""

import math
from mw_lib.brand import _hex_rgb


def _stroke(c, hex_color, width=1.6):
    r, g, b = _hex_rgb(hex_color)
    c.setStrokeColorRGB(r, g, b)
    c.setLineWidth(width)


def draw_leaf(c, cx, cy, size, style, ink_hex):
    _stroke(c, ink_hex, 2)
    p = c.beginPath()
    if style in ("birch", "gingko"):
        p.moveTo(cx, cy - size / 2)
        p.curveTo(cx + size * 0.55, cy - size * 0.1, cx + size * 0.3, cy + size * 0.45, cx, cy + size / 2)
        p.curveTo(cx - size * 0.3, cy + size * 0.45, cx - size * 0.55, cy - size * 0.1, cx, cy - size / 2)
        p.close()
        c.drawPath(p, fill=0, stroke=1)
    elif style == "maple":
        pts = []
        n_points = 5
        for i in range(n_points * 2):
            angle = math.pi / 2 + i * math.pi / n_points
            r = size / 2 if i % 2 == 0 else size * 0.25
            pts.append((cx + r * math.cos(angle) * 0.9, cy + r * math.sin(angle)))
        p.moveTo(*pts[0])
        for pt in pts[1:]:
            p.lineTo(*pt)
        p.close()
        c.drawPath(p, fill=0, stroke=1)
    else:  # oak: lobed edges
        n_lobes = 5
        pts = []
        for i in range(n_lobes * 2 + 1):
            t = i / (n_lobes * 2)
            y = cy + size / 2 - t * size
            bulge = size * 0.28 if i % 2 == 0 else size * 0.12
            pts.append((cx + bulge, y))
        p.moveTo(cx, cy - size / 2)
        for x, y in pts:
            p.lineTo(x, y)
        pts_left = [(cx - (x - cx), y) for x, y in reversed(pts)]
        for x, y in pts_left:
            p.lineTo(x, y)
        p.close()
        c.drawPath(p, fill=0, stroke=1)

    c.line(cx, cy - size / 2, cx, cy + size / 2)
    c.line(cx, cy - size * 0.35, cx, cy + size * 0.35)


def draw_pumpkin(c, cx, cy, size, ink_hex):
    _stroke(c, ink_hex, 1.8)
    w, h = size, size * 0.8
    c.ellipse(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, fill=0, stroke=1)
    for dx in (-w * 0.3, -w * 0.1, w * 0.1, w * 0.3):
        p = c.beginPath()
        p.moveTo(cx + dx, cy - h / 2)
        p.curveTo(cx + dx * 1.3, cy - h * 0.1, cx + dx * 1.3, cy + h * 0.1, cx + dx, cy + h / 2)
        c.drawPath(p, fill=0, stroke=1)
    c.rect(cx - w * 0.04, cy + h / 2, w * 0.08, h * 0.18, fill=0, stroke=1)


def draw_apple(c, cx, cy, size, ink_hex):
    _stroke(c, ink_hex, 1.8)
    r = size / 2.4
    c.circle(cx - r * 0.55, cy, r, fill=0, stroke=1)
    c.circle(cx + r * 0.55, cy, r, fill=0, stroke=1)
    c.line(cx, cy + r * 0.9, cx, cy + r * 1.4)


def draw_acorn(c, cx, cy, size, ink_hex):
    _stroke(c, ink_hex, 1.8)
    c.ellipse(cx - size * 0.32, cy - size * 0.55, cx + size * 0.32, cy + size * 0.15, fill=0, stroke=1)
    p = c.beginPath()
    p.moveTo(cx - size * 0.38, cy + size * 0.05)
    p.curveTo(cx - size * 0.3, cy + size * 0.3, cx + size * 0.3, cy + size * 0.3, cx + size * 0.38, cy + size * 0.05)
    p.lineTo(cx - size * 0.38, cy + size * 0.05)
    p.close()
    c.drawPath(p, fill=0, stroke=1)
    for i in range(4):
        y = cy - size * 0.4 + i * size * 0.13
        c.line(cx - size * 0.3, y, cx + size * 0.3, y)


def draw_pinecone(c, cx, cy, size, ink_hex):
    _stroke(c, ink_hex, 1.8)
    c.ellipse(cx - size * 0.28, cy - size / 2, cx + size * 0.28, cy + size / 2, fill=0, stroke=1)
    for i in range(5):
        y = cy - size * 0.4 + i * size * 0.2
        c.line(cx - size * 0.25, y, cx + size * 0.05, y - size * 0.06)
        c.line(cx + size * 0.25, y, cx - size * 0.05, y - size * 0.06)


DOT_TO_DOT_PUMPKIN = [
    (0.5, 0.98), (0.75, 0.8), (0.9, 0.55), (0.8, 0.2),
    (0.5, 0.05), (0.2, 0.2), (0.1, 0.55), (0.25, 0.8),
]

DOT_TO_DOT_LEAF = [
    (0.5, 0.95), (0.75, 0.6), (0.7, 0.35), (0.55, 0.15), (0.5, 0.02),
    (0.45, 0.15), (0.3, 0.35), (0.25, 0.6),
]

SHAPE_FN = {
    "pumpkin": draw_pumpkin,
    "apple": draw_apple,
    "acorn": draw_acorn,
    "pinecone": draw_pinecone,
}
