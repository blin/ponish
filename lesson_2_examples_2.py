# %%
from pathlib import Path

from draw import (
    DrawingContext,
    advance_after_glyph,
    draw_glyph,
)
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

# Example 1
with DrawingContext(output_path=dir / "example-bag.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["G"], pos=VP.AE)

# Example 2
with DrawingContext(output_path=dir / "example-big.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["G"], pos=VP.IY, gs=GS.DOUBLE)

# Example 3
with DrawingContext(output_path=dir / "example-bog.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["G"], pos=VP.OU)
