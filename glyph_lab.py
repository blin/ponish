# %%
from draw import (
    draw_glyph,
)
from draw_jupyturtle import DrawingContext
from glyphs import (
    Direction,
    Glyph,
    PenAction,
    PolarLine,
    RelPoint,
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


with DrawingContext() as (p, t):
    p.vowel_area_height_px = 20
    p.current_line_bottom_px = 30
    p.current_line_left_px = 10

    draw_glyph(t, p, g, pos=VowelPosition.OU)
