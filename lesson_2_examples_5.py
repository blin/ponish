# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import advance_after_word, draw_word
from draw_jupyturtle import DrawingContext

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

text = [
    "Betwen tims wen oʃns $(DR)ank $(AT)lantis $(AN)d riz of",
    "sons of $(AR)y$(AS) ðr was $(AN) $(AJ) un$(DR)emd of $(AN)d",
    "unto ðis Conan Destind to ber juld crown of",
    "$(AQ)ilonia upon $(TR)obld brow It is I his",
    "cronicler wo alone kan tel ðe of his saga",
    "Let me tel y of des of hi $(AD)ven$(ʧR)e",
]
for i, line in list(enumerate(text)):
    dc = DrawingContext(
        output_path=dir / f"passage-1-line-{i + 1}.svg",
        drawing_width=750,
        drawing_height=150,
    )
    with dc as (p, t):
        wq = line.split(" ")
        for word in line.split():
            draw_word(t, p, word)
            advance_after_word(t, p)
