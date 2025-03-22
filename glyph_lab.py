# %%
from draw import draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import (
    Circle,
    Direction,
    Glyph,
    GlyphSize,
    PolarLine,
    RelCubicBezier,
    RelPoint,
    Rotation,
    VowelPosition,
)

g = Glyph(
    start_pos=RelPoint(rel_y=0.4, rel_x=1.0),
    draw_actions=(
        Circle(
            rel_radius=0.2,
            extent_deg=360,
            rotation=Rotation.CW,
            heading_deg=Direction.S.value,
        ),
        PolarLine(angle_deg=Direction.S.value, rel_magnitude=0.2),
        RelCubicBezier(
            p2=RelPoint(rel_y=0.2, rel_x=0.0),
            p3=RelPoint(rel_y=0.2, rel_x=-0.1),
            p4=RelPoint(rel_y=0.2, rel_x=-0.3),
        ),
    ),
)

with DrawingContext() as (p, t):
    draw_glyph(t, p, g, pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
