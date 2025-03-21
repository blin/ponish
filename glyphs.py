from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Point:
    y: float
    x: float


@dataclass(frozen=True)
class RelPoint:
    rel_y: float  # positive is down, negative is up
    rel_x: float  # positive is right, negative is left


class Rotation(Enum):
    CW = auto()
    CCW = auto()


class PenAction(Enum):
    LIFT = auto()
    PLACE = auto()


@dataclass(frozen=True)
class PolarLine:
    angle_deg: float
    rel_magnitude: float


@dataclass(frozen=True)
class RelCubicBezier:
    # All control points are specified relative to first control point,
    # which is context dependent.
    p2: RelPoint
    p3: RelPoint
    p4: RelPoint


@dataclass(frozen=True)
class Circle:
    rel_radius: float
    extent_deg: int
    rotation: Rotation
    heading_deg: float


GlyphAction = PolarLine | RelCubicBezier | Circle | PenAction


@dataclass(frozen=True)
class Glyph:
    start_pos: RelPoint
    draw_actions: tuple[GlyphAction, ...]
    is_vowel: bool = False


class GlyphSize(Enum):
    SINGLE = 1
    DOUBLE = 2


class VowelPosition(Enum):
    AE = "AE"
    IY = "IY"
    OU = "OU"
    CONT = "CONT"


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


letters: dict[str, Glyph] = dict()

letters["A-two-legs"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=1.0),
    ),
    is_vowel=True,
)


letters["A-one-leg"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),),
    is_vowel=True,
)

letters["B"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),),
)

letters["C"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.25),
    draw_actions=(
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ),
)

letters["F"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ),
)

letters["H"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.4),
    draw_actions=(
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=0.7),
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=0.7),
    ),
)

letters["I"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
    is_vowel=True,
)

# TODO: make bottom line shorter to match "C" and "F"
letters["J"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.5),
    ),
)

letters["M"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=1.0),),
)

# TODO: consider having a short "N" and long "N"
letters["N"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(PolarLine(angle_deg=Direction.E.value, rel_magnitude=1.0),),
)

letters["T"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=(PolarLine(angle_deg=Direction.SSW.value, rel_magnitude=1.0),),
)

letters["V"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
    ),
)

letters["W"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.4),
    ),
)

letters["X"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=1.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=1.4),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=1.0),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=1.4),
    ),
)

letters["Y"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.1),
    draw_actions=(
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=0.6),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.6),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=1.4),
    ),
    is_vowel=True,
)

letters["Z"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=1.4),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=1.0),
    ),
)


# CH - https://en.wikipedia.org/wiki/Voiceless_postalveolar_affricate
letters["ʧ"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=0.7),
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=0.7),
    ),
)


letters["D"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        Circle(
            rel_radius=0.5,
            extent_deg=180,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
    ),
)
letters["E"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.1),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.7),
        Circle(
            rel_radius=0.2,
            extent_deg=300,
            rotation=Rotation.CCW,
            heading_deg=Direction.NNE.value,
        ),
        PolarLine(angle_deg=Direction.ENE.value, rel_magnitude=0.7),
    ),
    is_vowel=True,
)

letters["G"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.2),
        Circle(
            rel_radius=0.3,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ),
)

letters["K"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        # NOTE: Doing this as two RelCubicBezier would
        # match the original shape better, same for all half-circle shapes.
        Circle(
            rel_radius=0.4,
            extent_deg=180,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ),
)

letters["L"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        Circle(
            rel_radius=0.4,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
    ),
)

letters["O"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=(
        Circle(
            rel_radius=0.5,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.W.value,
        ),
    ),
    is_vowel=True,
)

letters["P"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.4),
    draw_actions=(
        Circle(
            rel_radius=0.3,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.9),
    ),
)

letters["Q"] = Glyph(
    start_pos=RelPoint(rel_y=0.25, rel_x=0.4),
    draw_actions=(
        Circle(
            rel_radius=0.25,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ),
)

letters["R"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.3),
        Circle(
            rel_radius=0.5,
            extent_deg=90,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ),
)

# TODO: bezier
letters["S"] = Glyph(
    start_pos=RelPoint(rel_y=0.25, rel_x=0.0),
    draw_actions=(
        Circle(
            rel_radius=0.25,
            extent_deg=360,
            rotation=Rotation.CCW,
            heading_deg=Direction.SE.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ),
)


letters["U"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.SSE.value, rel_magnitude=0.5),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.75, rel_x=0.75),
            p3=RelPoint(rel_y=0.75, rel_x=-0.75),
            p4=RelPoint(rel_y=0.0, rel_x=0.0),
        ),
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.5),
    ),
    is_vowel=True,
)


# TH - https://en.wikipedia.org/wiki/Voiced_dental_fricative
letters["ð"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.5),
    draw_actions=(
        Circle(
            rel_radius=0.5,
            extent_deg=360,
            rotation=Rotation.CCW,
            heading_deg=Direction.E.value,
        ),
    ),
)

# SH - https://en.wikipedia.org/wiki/Voiceless_postalveolar_fricative
letters["ʃ"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.4),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.75, rel_x=0.0),
            p3=RelPoint(rel_y=0.0, rel_x=-0.75),
            p4=RelPoint(rel_y=0.0, rel_x=0.0),
        ),
    ),
)

aliases: dict[str, Glyph] = dict()
aliases["A"] = letters["A-two-legs"]
aliases["CH"] = letters["ʧ"]
aliases["TH"] = letters["ð"]
aliases["SH"] = letters["ʃ"]
aliases["ZH"] = letters["ʃ"]

blends: dict[str, Glyph] = dict()


blends["AD"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
        Circle(
            rel_radius=0.5,
            extent_deg=180,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
    ),
)

blends["AJ"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
    ),
)

blends["AN"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=1.0),
    ),
)

blends["AR"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.3),
        Circle(
            rel_radius=0.5,
            extent_deg=75,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ),
)

blends["AS"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.75),
        Circle(
            rel_radius=0.1,
            extent_deg=360,
            rotation=Rotation.CCW,
            heading_deg=Direction.SE.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ),
)

blends["AT"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.SSW.value, rel_magnitude=1.0),
    ),
)

blends["AQ"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.75),
        Circle(
            rel_radius=0.1,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ),
)

blends["BR"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.2),
        Circle(
            rel_radius=0.5,
            extent_deg=60,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ),
)

blends["CR"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.25),
    draw_actions=(
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        Circle(
            rel_radius=0.5,
            extent_deg=75,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ),
)

blends["DR"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        Circle(
            rel_radius=0.5,
            extent_deg=180,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
        Circle(
            rel_radius=0.5,
            extent_deg=75,
            rotation=Rotation.CW,
            heading_deg=Direction.NE.value,
        ),
    ),
)

blends["FR"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.25),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        Circle(
            rel_radius=0.5,
            extent_deg=75,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ),
)

blends["TR"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=(
        PolarLine(angle_deg=Direction.SSW.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.3),
        Circle(
            rel_radius=0.5,
            extent_deg=60,
            rotation=Rotation.CW,
            heading_deg=Direction.NNE.value,
        ),
    ),
)

blends["ʧR"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=(
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=0.7),
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=0.7),
        Circle(
            rel_radius=0.5,
            extent_deg=75,
            rotation=Rotation.CW,
            heading_deg=Direction.NE.value,
        ),
    ),
)

blends["NG"] = Glyph(
    start_pos=RelPoint(rel_y=0.3, rel_x=1.0),
    draw_actions=(
        Circle(
            rel_radius=0.3,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.2),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.3, rel_x=-0.1),
            p3=RelPoint(rel_y=0.4, rel_x=-0.3),
            p4=RelPoint(rel_y=0.4, rel_x=-0.5),
        ),
    ),
)

blends["ING"] = blends["NG"]
blends["THING"] = blends["NG"]

blends["NK"] = Glyph(
    start_pos=RelPoint(rel_y=0.3, rel_x=0.0),
    draw_actions=(
        Circle(
            rel_radius=0.3,
            extent_deg=360,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.2),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.3, rel_x=0.1),
            p3=RelPoint(rel_y=0.4, rel_x=0.3),
            p4=RelPoint(rel_y=0.4, rel_x=0.5),
        ),
    ),
)

blends["NC"] = blends["NK"]
blends["THINK"] = blends["NK"]
blends["THANK"] = blends["NK"]

blends["PR"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.3),
    draw_actions=(
        Circle(
            rel_radius=0.3,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.2),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.1, rel_x=0.3),
            p3=RelPoint(rel_y=0.3, rel_x=0.4),
            p4=RelPoint(rel_y=0.5, rel_x=0.4),
        ),
    ),
)

blends["PL"] = Glyph(
    start_pos=RelPoint(rel_y=0.6, rel_x=0.3),
    draw_actions=(
        Circle(
            rel_radius=0.3,
            extent_deg=360,
            rotation=Rotation.CCW,
            heading_deg=Direction.E.value,
        ),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.2),
        RelCubicBezier(
            p2=RelPoint(rel_y=-0.1, rel_x=0.3),
            p3=RelPoint(rel_y=-0.3, rel_x=0.4),
            p4=RelPoint(rel_y=-0.5, rel_x=0.4),
        ),
    ),
)

blends["SS"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=(
        Circle(
            rel_radius=0.3,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    ),
)

punctuation: dict[str, Glyph] = dict()

punctuation["high-dot"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.01),
    ),
)

punctuation["low-dot"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.01),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.01),
    ),
)

punctuation["."] = punctuation["low-dot"]

punctuation[","] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        RelCubicBezier(
            p2=RelPoint(rel_y=0.0, rel_x=0.4),
            p3=RelPoint(rel_y=0.3, rel_x=0.3),
            p4=RelPoint(rel_y=0.6, rel_x=0.0),
        ),
    ),
)

punctuation[":"] = Glyph(
    start_pos=RelPoint(rel_y=0.3, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.02),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.4),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.02),
    ),
)

punctuation["!"] = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.8),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.02),
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.02),
    ),
)


def affix_from_letter(letter: str, more_actions: tuple[GlyphAction, ...]) -> Glyph:
    g = letters[letter]
    return Glyph(
        start_pos=g.start_pos,
        draw_actions=g.draw_actions + more_actions,
    )


affixes: dict[str, Glyph] = dict()

affixes["above"] = Glyph(
    start_pos=RelPoint(rel_y=0.4, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.4),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.4),
    ),
)
affixes["about"] = affixes["above"]

affixes["anti"] = affix_from_letter(
    "A-two-legs",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.NNW.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.6),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.9),
    ),
)
affixes["auto"] = affixes["anti"]

affixes["away"] = Glyph(
    start_pos=RelPoint(rel_y=0.4, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.4),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.4),
    ),
)
affixes["awa"] = affixes["away"]


affixes["circ"] = affix_from_letter(
    "C",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.4),
    ),
)
affixes["circu"] = affixes["circ"]
affixes["circum"] = affixes["circ"]

## The base is K not C, because of pronounciation.
affixes["com"] = affix_from_letter(
    "K",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.2),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.3),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
)
affixes["con"] = affixes["com"]
affixes["contr"] = affixes["com"]

affixes["dis"] = affix_from_letter(
    "D",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
)
affixes["des"] = affixes["dis"]

affixes["each"] = affix_from_letter(
    "ʧ",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
)

# There is a second form of "fect" that has an L-line instead of K-line,
# but I do not yet understand why it is needed.
affixes["fect"] = affix_from_letter(
    "F",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.7),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
        PenAction.PLACE,
        Circle(
            rel_radius=0.2,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
    ),
)

affixes["full"] = affix_from_letter(
    "F",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.4),
    ),
)

affixes["graph"] = affix_from_letter(
    "G",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.3),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.4),
    ),
)
affixes["gram"] = affixes["graph"]

# TODO: adjust start_pos
affixes["hood"] = affix_from_letter(
    "H",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.7),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
)

# That's basically inversed "above"
affixes["ify"] = Glyph(
    start_pos=RelPoint(rel_y=0.4, rel_x=0.4),
    draw_actions=(
        PolarLine(angle_deg=Direction.NW.value, rel_magnitude=0.4),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.4),
    ),
)

affixes["ifycation"] = Glyph(
    start_pos=RelPoint(rel_y=0.4, rel_x=0.4),
    # Not using "N" because it is too long
    draw_actions=(
        affixes["ify"].draw_actions
        + letters["ʃ"].draw_actions
        + (PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.4),)
    ),
)

affixes["less"] = affix_from_letter(
    "L",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.2),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.3),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
)

# There is a second form of "logy" that has an K-line instead of L-line,
# but I do not yet understand why it is needed.
# The base is J not G, because of pronounciation.
affixes["logy"] = affix_from_letter(
    "J",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.7),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.3),
        PenAction.PLACE,
        Circle(
            rel_radius=0.2,
            extent_deg=180,
            rotation=Rotation.CCW,
            heading_deg=Direction.S.value,
        ),
    ),
)
affixes["logic"] = affixes["logy"]

affixes["mis"] = affix_from_letter(
    "M",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.45),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
)
affixes["ment"] = affixes["mis"]

all: dict[str, Glyph] = {
    **letters,
    **aliases,
    **blends,
    **punctuation,
    **affixes,
}
