# %%
from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    advance_after_glyph,
    advance_glyph,
    draw_glyph,
    get_svg,
)
from glyphs import (
    VowelPosition,
    characters,
)

texts = ["ðe quick cute unicorn jumped ", "over ðe lazy gryphon"]
for i, text in enumerate(texts):
    drawing = Drawing(width=500, height=40)
    p = Page(unit_size_px=20, current_line_bottom_px=30, current_line_left_px=20)
    t = Turtle(delay=0.00, drawing=drawing)
    for c in text:
        if c == " ":
            advance_glyph(t, p)
            continue

        g = characters.get(c, None) or characters.get(c.upper(), None)
        assert g
        draw_glyph(t, p, g, pos=VowelPosition.OU)
        advance_after_glyph(t, p, g)
    t.hide()
    svg = get_svg(t)
    with open(f"manual/lesson-1/example-{i + 1}.svg", "w") as f:
        f.write(svg)
