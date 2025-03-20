# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import draw_sentence
from draw_jupyturtle import DrawingContext

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

text = [
    "Betwen the tims wen the oʃns $(DR)ank $(AT)lantis $(AN)d the riz of",
    "the sons of $(AR)y$(AS) ðr was $(AN) $(AJ) un$(DR)emd of $(AN)d",
    "unto ðis Conan Destind to ber the juld crown of",
    "$(AQ)ilonia upon a $(TR)obld brow It is I his",
    "cronicler wo alone kan tel ðe of his saga",
    "Let me tel y of the des of hi $(AD)ven$(ʧR)e",
]
for i, line in list(enumerate(text)):
    dc = DrawingContext(
        output_path=dir / f"passage-1-line-{i + 1}.svg",
        drawing_width=750,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_sentence(t, p, line)
