# %%
from jupyturtle.jupyturtle import Turtle, Drawing

from dataclasses import dataclass
from typing import Literal

# Percentages are in the range [0, 1]
type pct_norm = float


@dataclass
class Point:
    from_top_px: int
    from_left_px: int


@dataclass
class BoxRelativePoint:
    from_top_pct: pct_norm
    from_left_pct: pct_norm


def box_relative_to_absolute(rel: BoxRelativePoint, box_corner: Point, box_size_px: int) -> Point:
    return Point(
        from_top_px=box_corner.from_top_px + (box_size_px * rel.from_top_pct),
        from_left_px=box_corner.from_left_px + (box_size_px * rel.from_left_pct),
    )


@dataclass
class PolarLine:
    angle_deg: float
    magnitude_pct: pct_norm


@dataclass
class CubicBezier:
    p1: BoxRelativePoint
    p2: BoxRelativePoint
    p3: BoxRelativePoint
    p4: BoxRelativePoint


PenUp = Literal["pen-up"]
PenDown = Literal["pen-down"]

GlyphAction = PolarLine | CubicBezier | PenUp | PenDown


@dataclass
class Glyph:
    start_pos: BoxRelativePoint
    draw_actions: list[GlyphAction]


@dataclass
class Line:
    pass


@dataclass
class Page:
    unit_size_px: int
    current_line_bottom_px: int
    current_line_left_px: int


def cubic_bezier(points: list[Point], t: float) -> tuple[int, int]:
    """
    Calculate a point on a cubic Bezier curve for a given parameter t.

    Args:
        points: List of 4 points, where each point is a tuple (x, y)
        t: Parameter value between 0 and 1

    Returns:
        A tuple (x, y) representing a point on the Bezier curve
    """
    x0, y0 = points[0].from_left_px, points[0].from_top_px
    x1, y1 = points[1].from_left_px, points[1].from_top_px
    x2, y2 = points[2].from_left_px, points[2].from_top_px
    x3, y3 = points[3].from_left_px, points[3].from_top_px

    # Calculate x coordinate
    x = (1 - t) * ((1 - t) * ((1 - t) * x0 + t * x1) + t * ((1 - t) * x1 + t * x2)) + t * (
        (1 - t) * ((1 - t) * x1 + t * x2) + t * ((1 - t) * x2 + t * x3)
    )

    # Calculate y coordinate
    y = (1 - t) * ((1 - t) * ((1 - t) * y0 + t * y1) + t * ((1 - t) * y1 + t * y2)) + t * (
        (1 - t) * ((1 - t) * y1 + t * y2) + t * ((1 - t) * y2 + t * y3)
    )

    return (x, y)


def draw_cubic_bezier(turt: Turtle, page: Page, curve: CubicBezier) -> None:
    box_top_px = turt.y
    box_left_px = turt.x
    for i in range(21):
        t = i / 20
        p1 = box_relative_to_absolute(
            curve.p1, Point(from_top_px=box_top_px, from_left_px=box_left_px), page.unit_size_px
        )
        p2 = box_relative_to_absolute(
            curve.p2, Point(from_top_px=box_top_px, from_left_px=box_left_px), page.unit_size_px
        )
        p3 = box_relative_to_absolute(
            curve.p3, Point(from_top_px=box_top_px, from_left_px=box_left_px), page.unit_size_px
        )
        p4 = box_relative_to_absolute(
            curve.p4, Point(from_top_px=box_top_px, from_left_px=box_left_px), page.unit_size_px
        )
        x, y = cubic_bezier([p1, p2, p3, p4], t)
        if i == 0:
            turt.jump_to(x, y)
            continue
        turt.move_to(x, y)


def draw_action(t: Turtle, page: Page, action: GlyphAction) -> None:
    match action:
        case PolarLine(angle_deg=angle, magnitude_pct=magnitude):
            t.heading = -angle
            t.forward(page.unit_size_px * magnitude)
        case CubicBezier(p1=p1, p2=p2, p3=p3, p4=p4) as crv:
            draw_cubic_bezier(t, page, crv)
        case "pen-up":
            t.pen_up()
        case "pen-down":
            t.pen_down()


VowelPosition = Literal["A", "I", "O"]

Position = Literal["cont"] | VowelPosition


def find_box_corner(page: Page, vowel_pos: VowelPosition) -> Point:
    lb = page.current_line_bottom_px
    ll = page.current_line_left_px
    us = page.unit_size_px
    box_top_px = 0
    match vowel_pos:
        case "A":
            box_top_px = lb - us * 3
        case "I":
            box_top_px = lb - us * 2
        case "O":
            box_top_px = lb - us * 1
    return Point(from_top_px=box_top_px, from_left_px=ll)


# TODO: replace bool with type
def draw_glyph(t: Turtle, page: Page, glyph: Glyph, pos: Position) -> None:
    match pos:
        case "A" | "I" | "O" as v:
            t.pen_up()

            box = find_box_corner(page, vowel_pos=v)
            y = box.from_top_px + page.unit_size_px * glyph.start_pos.from_top_pct
            x = box.from_left_px + page.unit_size_px * glyph.start_pos.from_left_pct
            t.jump_to(y=y, x=x)

            t.pen_down()
    for action in glyph.draw_actions:
        draw_action(t, page, action)


def make_page(unit_size_px: int) -> Page:
    return Page(
        unit_size_px=unit_size_px,
        current_line_bottom_px=unit_size_px * 4,
        current_line_left_px=unit_size_px,
    )


def establish_line(t: Turtle, page: Page) -> None:
    c1 = t.pen_color
    t.pen_color = "#DDDDDD"
    t.jump_to(y=page.current_line_bottom_px, x=0)
    t.heading = 0
    t.forward(1000)
    t.pen_color = c1


def advance_glyph(t: Turtle, page: Page) -> None:
    t.pen_up()
    page.current_line_left_px = t.x + page.unit_size_px
    t.jump_to(y=page.current_line_bottom_px, x=page.current_line_left_px)
    t.pen_down()


# %%
characters = dict()

up = 90
right = 0
down = -90
left = 180

characters["A-1"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=70, magnitude_pct=1.0),
        PolarLine(angle_deg=-70, magnitude_pct=1.0),
    ],
)

# B
characters["B"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=-90, magnitude_pct=1.0),
    ],
)

# C
characters["C"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.25),
    draw_actions=[
        PolarLine(angle_deg=180, magnitude_pct=0.25),
        PolarLine(angle_deg=-90, magnitude_pct=1.0),
    ],
)

characters["D"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
            p2=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.6),
            p3=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.6),
            p4=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
        )
    ],
)

# E
characters["E"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.6),
            p2=BoxRelativePoint(from_top_pct=0.0, from_left_pct=1.0),
            p3=BoxRelativePoint(from_top_pct=0.6, from_left_pct=0.0),
            p4=BoxRelativePoint(from_top_pct=0.6, from_left_pct=0.7),
        ),
        PolarLine(angle_deg=right, magnitude_pct=0.4),
    ],
)

# F
characters["F"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=0, magnitude_pct=0.25),
        PolarLine(angle_deg=-90, magnitude_pct=1.0),
    ],
)

characters["G"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
            p2=BoxRelativePoint(from_top_pct=0.5, from_left_pct=0.0),
            p3=BoxRelativePoint(from_top_pct=0.5, from_left_pct=0.5),
            p4=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
        ),
        PolarLine(angle_deg=down, magnitude_pct=1.0),
    ],
)

# H
characters["H"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
    draw_actions=[
        PolarLine(angle_deg=-120, magnitude_pct=0.55),
        PolarLine(angle_deg=-60, magnitude_pct=0.55),
    ],
)

# I
characters["I"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=-90, magnitude_pct=1.0),
        PolarLine(angle_deg=0, magnitude_pct=0.5),
    ],
)

# J
characters["J"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
    draw_actions=[
        PolarLine(angle_deg=-90, magnitude_pct=1.0),
        PolarLine(angle_deg=180, magnitude_pct=0.5),
    ],
)

characters["K"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
            p2=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
            p3=BoxRelativePoint(from_top_pct=0.0, from_left_pct=1.0),
            p4=BoxRelativePoint(from_top_pct=1.0, from_left_pct=1.0),
        )
    ],
)


characters["L"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.2, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
            p2=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
            p3=BoxRelativePoint(from_top_pct=1.0, from_left_pct=1.0),
            p4=BoxRelativePoint(from_top_pct=0.0, from_left_pct=1.0),
        )
    ],
)

# M
characters["M"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=-70, magnitude_pct=1.0),
    ],
)

# N
characters["N"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=0, magnitude_pct=0.5),
    ],
)

# O
characters["O"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.6),
            p2=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
            p3=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
            p4=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.6),
        ),
    ],
)

# P
characters["P"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
            p2=BoxRelativePoint(from_top_pct=0.0, from_left_pct=1.0),
            p3=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
            p4=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.3),
        ),
        PolarLine(angle_deg=right, magnitude_pct=0.9),
    ],
)

# Q
characters["Q"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.4, from_left_pct=1.0),
            p2=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.4),
            p3=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.4),
            p4=BoxRelativePoint(from_top_pct=0.4, from_left_pct=1.0),
        ),
        PolarLine(angle_deg=down, magnitude_pct=0.5),
    ],
)

# R
# TODO: Need to re-do bezier so that it can follow a polar line :(
characters["R"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
            p2=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
            p3=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
            p4=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
        ),
        "pen-up",
        PolarLine(angle_deg=left, magnitude_pct=0.5),
        "pen-down",
        PolarLine(angle_deg=down, magnitude_pct=1.0),
    ],
)

# S
characters["S"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.4, from_left_pct=0.0),
            p2=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.4),
            p3=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.4),
            p4=BoxRelativePoint(from_top_pct=0.4, from_left_pct=0.0),
        ),
        PolarLine(angle_deg=down, magnitude_pct=0.5),
    ],
)

# T
characters["T"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
    draw_actions=[
        PolarLine(angle_deg=-110, magnitude_pct=1.0),
    ],
)

# U
characters["U"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.3),
            p2=BoxRelativePoint(from_top_pct=1.0, from_left_pct=1.0),
            p3=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
            p4=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.7),
        ),
    ],
)

# V
characters["V"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=-70, magnitude_pct=1.0),
        PolarLine(angle_deg=70, magnitude_pct=1.0),
    ],
)

# W
characters["W"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=down, magnitude_pct=1.0),
        PolarLine(angle_deg=50, magnitude_pct=0.4),
    ],
)

# X
characters["X"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
    draw_actions=[
        PolarLine(angle_deg=-45, magnitude_pct=1.3),
        "pen-up",
        PolarLine(angle_deg=left, magnitude_pct=1.0),
        "pen-down",
        PolarLine(angle_deg=45, magnitude_pct=1.3),
    ],
)

# Y
characters["Y"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=-50, magnitude_pct=0.5),
        "pen-up",
        PolarLine(angle_deg=50, magnitude_pct=0.5),
        "pen-down",
        PolarLine(angle_deg=180 + 50, magnitude_pct=1.3),
    ],
)

# Z
characters["Z"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.5),
    draw_actions=[
        PolarLine(angle_deg=right, magnitude_pct=0.5),
        PolarLine(angle_deg=180 + 60, magnitude_pct=1.1),
        PolarLine(angle_deg=right, magnitude_pct=0.5),
    ],
)

# TH
# TODO: cubic bezier or sine?
characters["TH"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.5, from_left_pct=0.5),
            p2=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.0),
            p3=BoxRelativePoint(from_top_pct=1.0, from_left_pct=1.0),
            p4=BoxRelativePoint(from_top_pct=0.5, from_left_pct=0.5),
        ),
    ],
)

# SH
# TODO: wrong direction fix
characters["SH"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.3, from_left_pct=0.0),
    draw_actions=[
        CubicBezier(
            p1=BoxRelativePoint(from_top_pct=0.4, from_left_pct=1.0),
            p2=BoxRelativePoint(from_top_pct=1.0, from_left_pct=0.4),
            p3=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.4),
            p4=BoxRelativePoint(from_top_pct=0.4, from_left_pct=1.0),
        ),
        PolarLine(angle_deg=up, magnitude_pct=0.5),
    ],
)

# CH
characters["CH"] = Glyph(
    start_pos=BoxRelativePoint(from_top_pct=0.0, from_left_pct=0.0),
    draw_actions=[
        PolarLine(angle_deg=-60, magnitude_pct=0.55),
        PolarLine(angle_deg=-120, magnitude_pct=0.55),
    ],
)


page_width = 500
drawing = Drawing(width=page_width, height=400)
t = Turtle(delay=0.0, drawing=drawing)
p = make_page(unit_size_px=30)

establish_line(t, p)


for char in characters.values():
    draw_glyph(t, p, char, pos="O")
    advance_glyph(t, p)
    if p.current_line_left_px > (page_width - 2 * p.unit_size_px):
        p.current_line_bottom_px += p.unit_size_px * 4
        p.current_line_left_px = p.unit_size_px
        establish_line(t, p)

# %%
t.hide()
print(t.get_SVG())
