# %%

from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    draw_glyph,
)
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

drawing = Drawing(width=50, height=50)
p = Page(unit_size_px=20, current_line_bottom_px=30, current_line_left_px=10)
t = Turtle(delay=0.00, drawing=drawing)

draw_glyph(t, p, g, pos=VowelPosition.O)
t.hide()
