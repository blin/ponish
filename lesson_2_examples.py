# %%
from draw import (
    advance_after_glyph,
    draw_glyph,
)
from draw_jupyturtle import DrawingContext
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
    next_pos = VowelPosition.AE

    output_path = f"manual/lesson-2/example-{i + 1}.svg"
    with DrawingContext(output_path=output_path) as (p, t):
        for c in text:
            if c == " ":
                advance_after_glyph(t, p)
                next_pos = VowelPosition.AE
                continue

            g = characters.get(c, None) or characters.get(c.upper(), None)
            assert g, f"Character {c} not found in character list"
            draw_glyph(t, p, g, pos=next_pos)
            next_pos = VowelPosition.CONT
