# %%
from draw import advance_after_glyph, advance_after_word, draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import VowelPosition
from glyphs import all as all_glyphs

texts = [
    "ðe quick cute unicorn jumped",
    "over ðe lazy gryphon",
    "ðe vexed pegasus flew high",
    "and ʃat on ðe land bound Hydra",
    "ðe ʧeery and dutiful earð ponys",
    "pie won first place",
]
for i, text in enumerate(texts):
    output_path = f"manual/lesson-1/example-{i + 1}.svg"
    with DrawingContext(output_path=output_path, drawing_width=600) as (p, t):
        for c in text:
            if c == " ":
                advance_after_word(t, p)
                continue

            g = all_glyphs.get(c, None) or all_glyphs.get(c.upper(), None)
            assert g, f"Character {c} not found in character list"
            draw_glyph(t, p, g, pos=VowelPosition.AE)
            advance_after_glyph(t, p)
