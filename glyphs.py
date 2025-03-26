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
        RelCubicBezier(
            p2=RelPoint(rel_y=0.75, rel_x=0.0),
            p3=RelPoint(rel_y=0.0, rel_x=-0.75),
            p4=RelPoint(rel_y=0.0, rel_x=0.0),
        ),
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=0.5),
    ),
)

letters["Q"] = Glyph(
    start_pos=RelPoint(rel_y=0.25, rel_x=0.4),
    draw_actions=(
        RelCubicBezier(
            p2=RelPoint(rel_y=0.0, rel_x=-0.75),
            p3=RelPoint(rel_y=-0.75, rel_x=0.0),
            p4=RelPoint(rel_y=0.0, rel_x=0.0),
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ),
)

# Extent needs to be > 75 degree for R to look sensibly
# when followed by a consonant. Use "RT" as an example when changing.
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

letters["S"] = Glyph(
    start_pos=RelPoint(rel_y=0.25, rel_x=0.0),
    draw_actions=(
        RelCubicBezier(
            p2=RelPoint(rel_y=0.0, rel_x=0.75),
            p3=RelPoint(rel_y=-0.75, rel_x=0.0),
            p4=RelPoint(rel_y=0.0, rel_x=0.0),
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.75),
    ),
)


# TODO: make "up" combination look okay
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


def derive_from_letter(letter: str, more_actions: tuple[GlyphAction, ...]) -> Glyph:
    g = letters[letter]
    return Glyph(
        start_pos=g.start_pos,
        draw_actions=g.draw_actions + more_actions,
    )


def n_strike(move: RelPoint, draw_e_rel: float) -> tuple[GlyphAction, ...]:
    move_y_dir = Direction.N.value if move.rel_y < 0 else Direction.S.value
    move_x_dir = Direction.W.value if move.rel_x < 0 else Direction.E.value

    return (
        PenAction.LIFT,
        PolarLine(angle_deg=move_y_dir, rel_magnitude=abs(move.rel_y)),
        PolarLine(angle_deg=move_x_dir, rel_magnitude=abs(move.rel_x)),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.E.value, rel_magnitude=draw_e_rel),
    )


blends: dict[str, Glyph] = dict()

# TODO: use derive_from_letter where possible
blends["AD"] = derive_from_letter(
    "A-one-leg",
    more_actions=letters["D"].draw_actions,
)

blends["AJ"] = derive_from_letter(
    "A-one-leg",
    more_actions=(
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.W.value, rel_magnitude=0.2),
    ),
)

blends["AN"] = derive_from_letter(
    "A-one-leg",
    more_actions=letters["N"].draw_actions,
)

blends["AR"] = derive_from_letter(
    "A-one-leg",
    more_actions=(
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

# Can not derive from "A" because
# the left leg needs to be shorter
blends["AS"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.75),)
    + letters["S"].draw_actions,
)

# Can not derive from "A" because
# the angles between "A" and "T" must not match
blends["AT"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.SSW.value, rel_magnitude=1.0),
    ),
)

# Can not derive from "A" because
# the left leg needs to be shorter
blends["AQ"] = Glyph(
    start_pos=RelPoint(rel_y=1.0, rel_x=0.0),
    draw_actions=(PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.75),)
    + letters["Q"].draw_actions,
)

# Can not use "R" directly because
# the first stroke is not needed and the angle is different.
# Angle needs to be different to distinguish "BR" from just "R"
blends["BR"] = derive_from_letter(
    "B",
    more_actions=(
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.2),
        Circle(
            rel_radius=0.5,
            extent_deg=60,
            rotation=Rotation.CW,
            heading_deg=Direction.N.value,
        ),
    ),
)

blends["CR"] = derive_from_letter("C", more_actions=letters["R"].draw_actions[-1:])

blends["DR"] = derive_from_letter("D", more_actions=letters["R"].draw_actions[-1:])

blends["GR"] = derive_from_letter("G", more_actions=letters["R"].draw_actions[-1:])

blends["FR"] = derive_from_letter("F", more_actions=letters["R"].draw_actions[-1:])

# Can not use "R" directly because
# the heading is different
blends["TR"] = derive_from_letter(
    "T",
    more_actions=(
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.3),
        Circle(
            rel_radius=0.5,
            extent_deg=60,
            rotation=Rotation.CW,
            heading_deg=Direction.NNE.value,
        ),
    ),
)

# Can not use "R" directly because
# the heading is different
blends["ʧR"] = derive_from_letter(
    "ʧ",
    more_actions=(
        Circle(
            rel_radius=0.5,
            extent_deg=75,
            rotation=Rotation.CW,
            heading_deg=Direction.NE.value,
        ),
    ),
)

blends["NG"] = Glyph(
    start_pos=RelPoint(rel_y=0.3, rel_x=0.6),
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


affixes: dict[str, Glyph] = dict()

affixes["above"] = Glyph(
    start_pos=RelPoint(rel_y=0.4, rel_x=0.0),
    draw_actions=(
        PolarLine(angle_deg=Direction.NE.value, rel_magnitude=0.4),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    )
    + n_strike(RelPoint(rel_y=-0.5, rel_x=-0.2), 0.4),
)
affixes["about"] = affixes["above"]

affixes["anti"] = derive_from_letter(
    "A-two-legs",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=-0.8), 0.9),
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


affixes["circ"] = derive_from_letter(
    "C",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=-0.2), 0.4),
)
affixes["circu"] = affixes["circ"]
affixes["circum"] = affixes["circ"]

# The base is K not C, because of pronounciation.
affixes["com"] = derive_from_letter(
    "K",
    more_actions=n_strike(RelPoint(rel_y=-0.2, rel_x=-0.3), 0.5),
)
affixes["con"] = affixes["com"]
affixes["contr"] = affixes["com"]

affixes["dis"] = derive_from_letter(
    "D",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=0.2), 0.5),
)
affixes["des"] = affixes["dis"]

affixes["each"] = derive_from_letter(
    "ʧ",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=0.2), 0.5),
)

# TODO [k-l-second-form]: K-line/L-line second forms are used when affix
# precedes K or L, so that the combination forms a sine wave.
affixes["fect"] = derive_from_letter(
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

affixes["full"] = derive_from_letter(
    "F",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=-0.2), 0.4),
)

affixes["graph"] = derive_from_letter(
    "G",
    more_actions=n_strike(RelPoint(rel_y=-0.3, rel_x=-0.2), 0.4),
)
affixes["gram"] = affixes["graph"]

# TODO: adjust start_pos
affixes["hood"] = derive_from_letter(
    "H",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=-0.7), 0.5),
)

# That's basically inversed "above"
affixes["ify"] = Glyph(
    start_pos=RelPoint(rel_y=0.4, rel_x=0.4),
    draw_actions=(
        PolarLine(angle_deg=Direction.NW.value, rel_magnitude=0.4),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=1.0),
    )
    + n_strike(RelPoint(rel_y=-0.5, rel_x=-0.2), 0.4),
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

# Using S instead of N for the first movement
affixes["less"] = derive_from_letter(
    "L",
    more_actions=n_strike(RelPoint(rel_y=0.2, rel_x=-0.3), 0.5),
)

# TODO [k-l-second-form]
# The base is J not G, because of pronounciation.
affixes["logy"] = derive_from_letter(
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

affixes["mis"] = derive_from_letter(
    "M",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=-0.55), 0.7),
)
affixes["ment"] = affixes["mis"]

affixes["ness"] = derive_from_letter(
    "N",
    more_actions=(
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=0.4),
        Circle(
            rel_radius=0.3,
            extent_deg=180,
            rotation=Rotation.CW,
            heading_deg=Direction.E.value,
        ),
    ),
)

# TODO: adjust start_pos
affixes["over"] = derive_from_letter(
    "O",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=-0.8), 1.0),
)
affixes["other"] = affixes["over"]
affixes["out"] = affixes["over"]

affixes["self"] = derive_from_letter(
    "S",
    more_actions=letters["L"].draw_actions + n_strike(RelPoint(rel_y=-0.4, rel_x=-1.0), 0.4),
)

affixes["semi"] = derive_from_letter(
    "S",
    more_actions=letters["M"].draw_actions + n_strike(RelPoint(rel_y=-1.0, rel_x=-0.8), 1.3),
)

affixes["ship"] = derive_from_letter(
    "ʃ",
    more_actions=n_strike(RelPoint(rel_y=-0.4, rel_x=-0.4), 1.0),
)

affixes["sub"] = derive_from_letter(
    "S",
    more_actions=n_strike(RelPoint(rel_y=-0.4, rel_x=-0.2), 0.4),
)

# TODO [k-l-second-form]
affixes["super"] = derive_from_letter(
    "S",
    more_actions=(
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.5),
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

affixes["trans"] = derive_from_letter(
    "T",
    more_actions=n_strike(RelPoint(rel_y=-0.5, rel_x=0.0), 0.4),
)

affixes["under"] = derive_from_letter(
    "U",
    more_actions=n_strike(RelPoint(rel_y=0.4, rel_x=-0.5), 0.7),
)

affixes["ever"] = derive_from_letter(
    "V",
    more_actions=n_strike(RelPoint(rel_y=0.5, rel_x=-0.8), 0.85),
)
affixes["every"] = affixes["ever"]
affixes["very"] = affixes["ever"]

affixes["ward"] = derive_from_letter(
    "W",
    more_actions=n_strike(RelPoint(rel_y=-0.2, rel_x=-0.8), 1.1),
)


all: dict[str, Glyph] = {
    **letters,
    **aliases,
    **blends,
    **punctuation,
    **affixes,
}
