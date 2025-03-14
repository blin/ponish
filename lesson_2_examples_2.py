# %%
from pathlib import Path

from draw import (
    advance_after_glyph,
    draw_glyph,
)
from draw_jupyturtle import DrawingContext
from glyphs import (
    GlyphSize as GS,
)
from glyphs import (
    VowelPosition as VP,
)
from glyphs import (
    characters,
)

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

with DrawingContext(output_path=dir / "example-bag.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["G"], pos=VP.AE)

with DrawingContext(output_path=dir / "example-big.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["G"], pos=VP.IY, gs=GS.DOUBLE)

with DrawingContext(output_path=dir / "example-bog.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["G"], pos=VP.OU)
