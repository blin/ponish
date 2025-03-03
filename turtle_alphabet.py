# %%
from itertools import batched
from string import ascii_uppercase

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


for i, batch in enumerate(batched(ascii_uppercase, 7)):
    page_width = 350
    drawing = Drawing(width=page_width, height=80)
    t = Turtle(delay=0.00, drawing=drawing)
    p = make_page(unit_size_px=30)

    establish_line(t, p)
    for char in batch:
        glyph = characters[char]
        draw_glyph(t, p, glyph, pos="A")
        advance_glyph(t, p)
    with open(f"manual/alphabet_{i}.svg", "w") as f:
        f.write(t.get_SVG())
