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

dir = Path("manual/lesson-4")
dir.mkdir(parents=True, exist_ok=True)

text = [
    "togoto",
    "togoto the mal",
    "iha$(VT)o",
    "iha$(VT)ogoto the mal",
    "$(AS)fastasposibl",
    "beritbak",
    "befor$(Y-consonant)unoit",
    "by$(AL)mens",
    "b the wa",
    "herand$(TH-top-start)er",
    "nfakt",
    "nmydefens",
    "a lotof",
    "nowand$(TH-top-start)en",
    "$(TH)ekanot",
    "$(Y-consonant)uwilnotba$(AB)lto",  # TODO: "A" in "$(AB)" should give an AE vowel position
    "we$(AR) the $(PR)isetsof the tem$(PL)sofsyrin$(X-from-left)",
    "clo$(TH)shors",
    "$(CR)o$(CH)tits",
    "fludin$(SH)urans",
    "horspusy",
    "mouspad",
    "poisonjok",
    "rok$(ING)$(CH)er",
    "s$(TR)etlit",
    "$(SH)ugarkubkornr",
    "swim$(ING)pul",
    "swi$(ING)set",
    "wa$(TR)botl",
]
if __name__ == "__main__":
    for i, line in list(enumerate(text)):
        dc = DrawingContext(
            output_path=dir / f"phrase-{i + 1:02}.svg",
            drawing_width=1100,
            drawing_height=150,
        )
        with dc as (p, t):
            draw_sentence(t, p, line)
