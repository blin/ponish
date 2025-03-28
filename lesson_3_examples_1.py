# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import draw_word
from draw_jupyturtle import DrawingContext

dir = Path("manual/lesson-3")
dir.mkdir(parents=True, exist_ok=True)

words = [
    ("thing", "$(THING)"),
    ("something", "som$(THING)"),
    ("going", "go$(ING)"),
    ("twang", "twa$(NG)"),
    ("think", "$(THINK)"),
    ("bank", "ba$(NK)"),
    ("flunk", "flu$(NK)"),
    ("thank-you", "$(THANK)iu"),
    ("pr", "$(PR)"),
    ("private", "$(PR)ivat"),
    ("project", "$(PR)ojekt"),
    ("preview", "$(PR)evu"),
    ("pl", "$(PL)"),
    ("pleasure", "$(PL)e$(ZH)r"),
    ("plastic", "$(PL)astik"),
    ("plebian", "$(PL)ebe$(AN)"),
    ("ss", "$(SS)"),
    ("princess", "$(PR)in$(SS)"),
    ("success", "suk$(SS)"),
    ("misses", "mi$(SS)"),
]
for name, spelling in words:
    dc = DrawingContext(
        output_path=dir / f"{name}.svg",
        drawing_width=350,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_word(t, p, spelling)
