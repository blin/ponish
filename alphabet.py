# %%
import re

from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    draw_glyph,
    get_svg,
)
from glyphs import (
    VowelPosition,
    characters,
)

for char_id, char in characters.items():
    drawing = Drawing(width=40, height=40)
    p = Page(vowel_area_height_px=20, current_line_bottom_px=30, current_line_left_px=10)
    t = Turtle(delay=0.00, drawing=drawing)

    draw_glyph(t, p, char, pos=VowelPosition.OU)
    t.hide()
    svg = get_svg(t)
    with open(f"manual/alphabet/{char_id}.svg", "w") as f:
        f.write(svg)
