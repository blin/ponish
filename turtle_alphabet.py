# %%
from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    advance_glyph,
    draw_glyph,
    establish_line,
)
from glyphs import (
    characters,
)


def make_page(unit_size_px: int) -> Page:
    return Page(
        unit_size_px=unit_size_px,
        current_line_bottom_px=unit_size_px * 4,
        current_line_left_px=unit_size_px,
    )


page_width = 500
drawing = Drawing(width=page_width, height=400)
t = Turtle(delay=0.00, drawing=drawing)
p = make_page(unit_size_px=30)

establish_line(t, p)


for _, char in sorted(characters.items(), key=lambda x: x[0]):
    draw_glyph(t, p, char, pos="O")
    advance_glyph(t, p)
    if p.current_line_left_px > (page_width - 2 * p.unit_size_px):
        p.current_line_bottom_px += p.unit_size_px * 4
        p.current_line_left_px = p.unit_size_px
        establish_line(t, p)
