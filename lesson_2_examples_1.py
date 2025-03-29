# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from draw import advance_after_glyph, draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import VowelPosition, all as all_glyphs

texts = [
    ["B", " ", "L", " ", "U", " ", "E"],
    ["B", "L", " ", "U", " ", "E"],
    ["B", " ", "R", " ", "E", " ", "A", " ", "K"],
    ["BR", " ", "E", " ", "A", " ", "K"],
    ["S", " ", "T", " ", "A", " ", "N", " ", "D"],
    ["S", "T", " ", "A", " ", "N", "D"],
    ["S", " ", "T", " ", "R", " ", "I", " ", "K", " ", "E"],
    ["S", "TR", " ", "I", " ", "K", " ", "E"],
    ["E", " ", "N", " ", "V", " ", "I", " ", "S", " ", "I", " ", "O", " ", "N"],
    ["E", " ", "N", "V", " ", "I", " ", "ʃ", "N"],
    ["N", " ", "A", " ", "T", " ", "I", " ", "O", " ", "N"],
    ["N", " ", "A", " ", "ʃ", "N"],
    ["P", " ", "A", " ", "S", " ", "S", " ", "I", " ", "O", " ", "N"],
    ["P", " ", "A", " ", "ʃ", "N"],
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

            g = all_glyphs.get(c, None) or all_glyphs.get(c.upper(), None)
            assert g, f"Character {c} not found in character list"
            draw_glyph(t, p, g, pos=next_pos)
            next_pos = VowelPosition.CONT
