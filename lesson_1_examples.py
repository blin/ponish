# %%
from draw import (
    advance_after_glyph,
    advance_glyph,
    draw_glyph,
)
from draw_jupyturtle import DrawingContext
from glyphs import (
    VowelPosition,
    characters,
)

texts = [
    "ðe quick cute unicorn jumped",
    "over ðe lazy gryphon",
    "ðe vexed pegasus flew high",
    "and ʃat on ðe land bound Hydra",
    "ðe ʧeery and dutiful earth ponys",
    "pie won first place",
]
for i, text in enumerate(texts):
    output_path = f"manual/lesson-1/example-{i + 1}.svg"
    with DrawingContext(output_path=output_path, drawing_width=600) as (p, t):
        for c in text:
            if c == " ":
                advance_glyph(t, p)
                continue

            g = characters.get(c, None) or characters.get(c.upper(), None)
            assert g, f"Character {c} not found in character list"
            draw_glyph(t, p, g, pos=VowelPosition.AE)
            advance_after_glyph(t, p)
