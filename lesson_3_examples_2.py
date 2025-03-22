# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import draw_glyph
from draw_jupyturtle import DrawingContext

dir = Path("manual/lesson-3/affixes")
dir.mkdir(parents=True, exist_ok=True)

seen: set[glyphs.Glyph] = set()
for name, g in list(glyphs.affixes.items())[37:]:
    if g in seen:
        continue
    seen.add(g)
    dc = DrawingContext(
        output_path=dir / f"{name}.svg",
        drawing_width=150,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_glyph(t, p, g, pos=glyphs.VowelPosition.IY, gs=glyphs.GlyphSize.DOUBLE)
