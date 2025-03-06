# %%
from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    advance_glyph,
    draw_glyph,
)
from glyphs import (
    VowelPosition,
    characters,
)


drawing = Drawing(width=1000, height=50)
p = Page(unit_size_px=20, current_line_bottom_px=30, current_line_left_px=20)
t = Turtle(delay=0.00, drawing=drawing)

text = "ðe quick cute unicorn jumped over the lazy gryphon"
for i, c in enumerate(text):
    if c == ' ':
        advance_glyph(t, p)
        continue

    g = characters.get(c, None) or characters.get(c.upper(), None)
    if g is not None:
        draw_glyph(t, p, g, pos=VowelPosition.OU)
        advance_glyph(t, p)
    else:
        print(f"Character '{c}' not found in characters")
