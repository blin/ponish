from dataclasses import dataclass
from enum import Enum, auto
from typing import Literal, Union


@dataclass
class Point:
    y: int
    x: int


@dataclass
class RelPoint:
    rel_y: float  # positive is down, negative is up
    rel_x: float  # positive is right, negative is left


def find_rel_point(rel: RelPoint, ref_point: Point, unit_size_px: int) -> Point:
    return Point(
        y=ref_point.y + (unit_size_px * rel.rel_y),
        x=ref_point.x + (unit_size_px * rel.rel_x),
    )


class Rotation(Enum):
    CW = auto()
    CCW = auto()


class PenAction(Enum):
    LIFT = auto()
    PLACE = auto()


@dataclass
class PolarLine:
    angle_deg: float
    rel_magnitude: float


@dataclass
class RelCubicBezier:
    # All control points are specified relative to first control point,
    # which is context dependent.
    p2: RelPoint
    p3: RelPoint
    p4: RelPoint


@dataclass
class Circle:
    rel_radius: float
    extent_deg: int
    rotation: Rotation
    heading_deg: float


GlyphAction = PolarLine | RelCubicBezier | Circle | PenAction


@dataclass
class Glyph:
    start_pos: RelPoint
    draw_actions: list[GlyphAction]
    is_vowel: bool = False


class GlyphSize(Enum):
    SINGLE = 1
    DOUBLE = 2


class VowelPosition(Enum):
    AE = "AE"
    IY = "IY"
    OU = "OU"


Position = Union[Literal["cont"], VowelPosition]


class Direction(Enum):
    # Cardinal directions (4-wind)
    N = 90
    E = 0
    S = -90
    W = 180

    # Ordinal directions (8-wind)
    NE = 45
    SE = -45
    SW = -135
    NW = 135

    # Half-wind directions (16-wind)
    NNE = 67.5
    ENE = 22.5
    ESE = -22.5
    SSE = -67.5
    SSW = -112.5
    WSW = -157.5
    WNW = 157.5
    NNW = 112.5


# Characters that only use PolarLine draw actions
chars_without_curves = dict()

chars_without_curves["A-two-legs"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=1.0),
    ],
    is_vowel=True,
)

chars_without_curves["A"] = chars_without_curves["A-two-legs"]

chars_without_curves["A-one-leg"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
    ],
    is_vowel=True,
)

chars_without_curves["B"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ],
)

chars_without_curves["C"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.25),
    draw_actions=[
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ],
)

chars_without_curves["F"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ],
)

chars_without_curves["H"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.4),
    draw_actions=[
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=0.7),
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=0.7),
    ],
)

chars_without_curves["I"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ],
    is_vowel=True,
)

chars_without_curves["J"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=[
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.5),
    ],
)

chars_without_curves["M"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=1.0),
    ],
)

chars_without_curves["N"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ],
)

chars_without_curves["T"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=[
        PolarLine(angle_deg=Direction.SSW.value, rel_magnitude=1.0),
    ],
)

chars_without_curves["V"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
    ],
)

chars_without_curves["W"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.4),
    ],
)

chars_without_curves["X"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=1.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=1.4),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=1.0),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=1.4),
    ],
)

chars_without_curves["Y"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.1),
    draw_actions=[
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=0.6),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.6),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=1.4),
    ],
    is_vowel=True,
)

chars_without_curves["Z"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=1.4),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=1.0),
    ],
)


chars_without_curves["CH"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=0.7),
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=0.7),
    ],
)
chars_without_curves["ʧ"] = chars_without_curves["CH"]

chars_without_curves["end-vowel-dot"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.01),
    ],
)

chars_without_curves["article-dot"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=1.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.01),
    ],
)


chars_with_curves = dict()

chars_with_curves["D"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        Circle(
            rel_radius=0.5,
            extent_deg=180,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
    ],
)
chars_with_curves["E"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.1),
    draw_actions=[
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.7),
        Circle(
            rel_radius=0.2,
            extent_deg=300,
            rotation=Rotation.CCW,
            heading_deg=Direction.NNE.value,
        ),
        PolarLine(angle_deg=Direction.ENE.value, rel_magnitude=0.7),
    ],
    is_vowel=True,
)

chars_with_curves["G"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.2),
        Circle(
            rel_radius=0.3,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ],
)

chars_with_curves["K"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=[
        # NOTE: Doing this as two RelCubicBezier would
        # match the original shape better, same for all half-circle shapes.
        Circle(
            rel_radius=0.4,
            extent_deg=180,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ],
)

chars_with_curves["L"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        Circle(
            rel_radius=0.4,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
    ],
)

chars_with_curves["O"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=[
        Circle(
            rel_radius=0.5,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.W.value,
        ),
    ],
    is_vowel=True,
)

chars_with_curves["P"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.4),
    draw_actions=[
        Circle(
            rel_radius=0.3,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.9),
    ],
)

chars_with_curves["Q"] = Glyph(
    start_pos=RelPoint(rel_y=0.25, rel_x=0.4),
    draw_actions=[
        Circle(
            rel_radius=0.25,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ],
)

chars_with_curves["R"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        Circle(
            rel_radius=0.5,
            extent_deg=90,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ],
)

chars_with_curves["S"] = Glyph(
    start_pos=RelPoint(rel_y=0.25, rel_x=0.0),
    draw_actions=[
        Circle(
            rel_radius=0.25,
            extent_deg=360,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ],
)


chars_with_curves["U"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=0.5),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.75, rel_x=0.75),
            p3=RelPoint(rel_y=0.75, rel_x=-0.75),
            p4=RelPoint(rel_y=0.0, rel_x=0.0),
        ),
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.5),
    ],
    is_vowel=True,
)


chars_with_curves["TH"] = Glyph(
    start_pos=RelPoint(rel_y=0.5, rel_x=1.0),
    draw_actions=[
        Circle(
            rel_radius=0.5,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.S.value,
        ),
    ],
)
chars_with_curves["ð"] = chars_with_curves["TH"]

chars_with_curves["SH"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.4),
    draw_actions=[
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.75, rel_x=0.0),
            p3=RelPoint(rel_y=0.0, rel_x=-0.75),
            p4=RelPoint(rel_y=0.0, rel_x=0.0),
        ),
    ],
)
chars_with_curves["ʃ"] = chars_with_curves["SH"]

characters: dict[str, Glyph] = {**chars_without_curves, **chars_with_curves}
