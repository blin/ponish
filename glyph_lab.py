# %%
from draw import (
    draw_glyph,
)
from draw_jupyturtle import DrawingContext
from glyphs import (
    Circle,
    Direction,
    Glyph,
    GlyphSize,
    PenAction,
    PolarLine,
    RelPoint,
    Rotation,
    VowelPosition,
)

g = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=1.0),
    draw_actions=[
        PolarLine(angle_deg=Direction.SW.value, rel_magnitude=1.0),
        PenAction.LIFT,
        PolarLine(angle_deg=Direction.N.value, rel_magnitude=0.7),
        PenAction.PLACE,
        PolarLine(angle_deg=Direction.SE.value, rel_magnitude=1.0),
    ],
)

g = Glyph(
    start_pos=RelPoint(rel_y=0.0, rel_x=0.5),
    draw_actions=[
        PolarLine(angle_deg=Direction.SSW.value, rel_magnitude=1.0),
        PolarLine(angle_deg=Direction.NNE.value, rel_magnitude=0.3),
        Circle(
            rel_radius=0.5,
            extent_deg=90,
            rotation=Rotation.CW,
            heading_deg=Direction.NNE.value,
        ),
    ],
)

with DrawingContext() as (p, t):
    draw_glyph(t, p, g, pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
