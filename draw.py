import math
import re
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

from glyphs import (
    Circle,
    Glyph,
    GlyphAction,
    GlyphSize,
    PenAction,
    Point,
    PolarLine,
    Position,
    RelCubicBezier,
    Rotation,
    VowelPosition,
    find_rel_point,
)


@runtime_checkable
class Turtle(Protocol):
    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

    @property
    def heading(self) -> float: ...

    @heading.setter
    def heading(self, value: float) -> None: ...

    @property
    def pen_color(self) -> str: ...

    @pen_color.setter
    def pen_color(self, value: str) -> None: ...

    def forward(self, distance: float) -> None: ...

    def jump_to(self, x: int, y: int) -> None: ...

    def move_to(self, x: int, y: int) -> None: ...

    def pen_up(self) -> None: ...

    def pen_down(self) -> None: ...


@dataclass
class Page:
    vowel_area_height_px: int
    current_glyph_height_px: int = 0
    current_line_bottom_px: int = 0
    current_line_left_px: int = 0
    furthest_from_left_px: int = 0
    furthest_from_top_px: int = 0


def calc_bezier(p1: Point, p2: Point, p3: Point, p4: Point, t: float) -> tuple[int, int]:
    """
    Calculate a point on a cubic Bezier curve for a given parameter t.

    Args:
        p1: First control point
        p2: Second control point
        p3: Third control point
        p4: Fourth control point
        t: Parameter value between 0 and 1

    Returns:
        A tuple (x, y) representing a point on the Bezier curve
    """
    u = 1 - t  # u is the complement of t

    # First level of linear interpolation between adjacent points
    x_p1_p2 = u * p1.x + t * p2.x
    x_p2_p3 = u * p2.x + t * p3.x
    x_p3_p4 = u * p3.x + t * p4.x
    y_p1_p2 = u * p1.y + t * p2.y
    y_p2_p3 = u * p2.y + t * p3.y
    y_p3_p4 = u * p3.y + t * p4.y

    # Second level of linear interpolation
    x_p1p2_p2p3 = u * x_p1_p2 + t * x_p2_p3
    x_p2p3_p3p4 = u * x_p2_p3 + t * x_p3_p4
    y_p1p2_p2p3 = u * y_p1_p2 + t * y_p2_p3
    y_p2p3_p3p4 = u * y_p2_p3 + t * y_p3_p4

    # Final interpolation
    x = u * x_p1p2_p2p3 + t * x_p2p3_p3p4
    y = u * y_p1p2_p2p3 + t * y_p2p3_p3p4

    return (x, y)


# NOTE: have to use `turt` instead of `t` because of the name conflict
# with Bezier "t-parameter"
def draw_cubic_bezier(turt: Turtle, page: Page, curve: RelCubicBezier) -> None:
    p1 = Point(y=turt.y, x=turt.x)
    for i in range(21):
        t = i / 20
        p2 = find_rel_point(curve.p2, p1, page.current_glyph_height_px)
        p3 = find_rel_point(curve.p3, p1, page.current_glyph_height_px)
        p4 = find_rel_point(curve.p4, p1, page.current_glyph_height_px)
        x, y = calc_bezier(p1, p2, p3, p4, t)
        if i == 0:
            turt.jump_to(x, y)
            continue
        turt.move_to(x, y)


def draw_forward(t: Turtle, p: Page, distance_px: int) -> None:
    p.furthest_from_left_px = max(p.furthest_from_left_px, t.x)
    p.furthest_from_top_px = max(p.furthest_from_top_px, t.y)
    t.forward(distance_px)
    p.furthest_from_left_px = max(p.furthest_from_left_px, t.x)
    p.furthest_from_top_px = max(p.furthest_from_top_px, t.y)


def draw_circle(t: Turtle, circle: Circle, page: Page) -> None:
    # Set initial heading
    t.heading = -circle.heading_deg  # Negative because turtle heading is clockwise

    # Calculate the number of steps based on the extent
    steps = max(int(abs(circle.extent_deg) / 5), 1)  # At least 1 step, otherwise 5 degrees per step
    angle_per_step = circle.extent_deg / steps

    # Calculate the side length for a regular polygon approximating the circle
    # When drawing a circle as a regular polygon, each segment is a chord of the circle
    # For a chord of a circle:
    # - The angle at the center is angle_per_step
    # - The chord length (side_length) = 2 * radius * sin(angle/2)
    # This formula gives the exact length needed to draw each side of the polygon
    step_angle_rad = math.radians(angle_per_step)
    radius_px = circle.rel_radius * page.current_glyph_height_px
    side_length = 2 * radius_px * math.sin(step_angle_rad / 2)

    for _ in range(steps):
        draw_forward(t, page, side_length)
        match circle.rotation:
            case Rotation.CCW:
                t.heading -= angle_per_step
            case Rotation.CW:
                t.heading += angle_per_step


def draw_polar_line(t: Turtle, p: Page, line: PolarLine) -> None:
    t.heading = -line.angle_deg
    draw_forward(t, p, p.current_glyph_height_px * line.rel_magnitude)


def draw_action(t: Turtle, page: Page, action: GlyphAction) -> None:
    match action:
        case PolarLine() as l:
            draw_polar_line(t, page, l)
        case RelCubicBezier() as crv:
            draw_cubic_bezier(t, page, crv)
        case Circle() as c:
            draw_circle(t, c, page)
        case PenAction.LIFT:
            t.pen_up()
        case PenAction.PLACE:
            t.pen_down()


def find_box_corner(page: Page, vowel_pos: VowelPosition) -> Point:
    lb = page.current_line_bottom_px
    ll = page.current_line_left_px
    us = page.vowel_area_height_px
    box_top_px = 0
    match vowel_pos:
        case VowelPosition.AE:
            box_top_px = lb - us * 3
        case VowelPosition.IY:
            box_top_px = lb - us * 2
        case VowelPosition.OU:
            box_top_px = lb - us * 1
    return Point(y=box_top_px, x=ll)


def draw_glyph(
    t: Turtle, page: Page, glyph: Glyph, pos: Position, gs: GlyphSize = GlyphSize.SINGLE
) -> None:
    page.current_glyph_height_px = page.vowel_area_height_px * gs.value
    match pos:
        case VowelPosition.AE | VowelPosition.IY | VowelPosition.OU as v:
            t.pen_up()

            box = find_box_corner(page, vowel_pos=v)
            y = box.y + page.current_glyph_height_px * glyph.start_pos.rel_y
            x = box.x + page.current_glyph_height_px * glyph.start_pos.rel_x
            t.jump_to(y=y, x=x)

            t.pen_down()
    for action in glyph.draw_actions:
        draw_action(t, page, action)


def outline_vowel_areas(t: Turtle, p: Page) -> None:
    c1 = t.pen_color
    t.pen_color = "#DDDDDD"
    for i in range(4):
        y = p.current_line_bottom_px - (i * p.vowel_area_height_px)
        print(f"{y=}")
        t.jump_to(y=y, x=0)
        t.heading = 0
        t.forward(1000)
    t.pen_color = c1


def advance_glyph(t: Turtle, page: Page) -> None:
    t.pen_up()
    page.current_line_left_px = t.x + (page.vowel_area_height_px / 2)
    t.jump_to(y=page.current_line_bottom_px, x=page.current_line_left_px)
    t.pen_down()


def advance_after_glyph(t: Turtle, page: Page) -> None:
    t.pen_up()
    page.current_line_left_px = page.furthest_from_left_px + (page.vowel_area_height_px / 3)
    t.jump_to(y=page.current_line_bottom_px, x=page.current_line_left_px)
    t.pen_down()


def get_svg(t: Turtle) -> str:
    svg = t.get_SVG()
    svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"')
    svg = re.sub(r"'$", "", svg, flags=re.MULTILINE)
    svg = re.sub(r"^$\n", "", svg, flags=re.MULTILINE)
    return svg
