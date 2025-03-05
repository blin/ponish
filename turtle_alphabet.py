# %%
import re

from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    draw_glyph,
)
from glyphs import (
    characters,
)


def get_svg(t: Turtle) -> str:
    svg = t.get_SVG()
    svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"')
    svg = re.sub(r"'$", "", svg, flags=re.MULTILINE)
    svg = re.sub(r"^$\n", "", svg, flags=re.MULTILINE)
    return svg


for char_id, char in characters.items():
    page_width = 60
    drawing = Drawing(width=30, height=40)
    p = Page(unit_size_px=20, current_line_bottom_px=30, current_line_left_px=10)
    t = Turtle(delay=0.00, drawing=drawing)

    draw_glyph(t, p, char, pos="O")
    t.hide()
    svg = get_svg(t)
    with open(f"manual/alphabet/{char_id}.svg", "w") as f:
        f.write(svg)
