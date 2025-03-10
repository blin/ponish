# %%
from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    advance_after_glyph,
    draw_glyph,
    get_svg,
)
from glyphs import (
    VowelPosition,
    characters,
)

texts = [
    "B L U E",
    "BL U E",
    "B R E A K",
    "BR E A K",
    "S T A N D",
    "ST A ND",
    "S T R I K E",
    "STR I K E",
    "E N V I S I O N",
    "E NV I ʃN",
    "N A T I O N",
    "N A ʃN",
    "P A S S I O N",
    "P A ʃN",
]
for i, text in list(enumerate(texts)):
    next_pos = VowelPosition.OU
    drawing = Drawing(width=180, height=80)
    u = 20
    p = Page(unit_size_px=u, current_line_bottom_px=u + (u // 2), current_line_left_px=u)
    t = Turtle(delay=0.00, drawing=drawing)
    for c in text:
        if c == " ":
            advance_after_glyph(t, p)
            next_pos = VowelPosition.OU
            continue

        g = characters.get(c, None) or characters.get(c.upper(), None)
        assert g, f"Character {c} not found in character list"
        draw_glyph(t, p, g, pos=next_pos)
        next_pos = "cont"
    t.hide()
    drawing.width = p.furthest_from_left_px + p.unit_size_px
    drawing.height = p.furthest_from_top_px + p.unit_size_px
    svg = get_svg(t)
    with open(f"manual/lesson-2/example-{i + 1}.svg", "w") as f:
        f.write(svg)
