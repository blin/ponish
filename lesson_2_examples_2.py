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

for c1, c2 in [
    ("B", "G"),
    ("T", "M"),
    ("F", "N"),
    ("L", "P"),
    ("D", "end-vowel-dot"),
    ("S", "end-vowel-dot"),
]:
    for pos in [VP.AE, VP.IY, VP.OU]:
        with DrawingContext(
            output_path=dir / f"example-{c1.lower()}-{pos.value}-{c2.lower()}.svg"
        ) as (p, t):
            draw_glyph(t, p, characters[c1], pos=VP.IY, gs=GS.DOUBLE)
            advance_after_glyph(t, p)
            draw_glyph(t, p, characters[c2], pos=pos, gs=GS.DOUBLE if pos == VP.IY else GS.SINGLE)


# %%
with DrawingContext(output_path=dir / f"example-pond.svg") as (p, t):
    draw_glyph(t, p, characters["P"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["N"], pos=VP.OU)
    draw_glyph(t, p, characters["D"], pos=VP.CONT)

with DrawingContext(output_path=dir / f"example-pound.svg") as (p, t):
    draw_glyph(t, p, characters["P"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["U"], pos=VP.OU)
    draw_glyph(t, p, characters["N"], pos=VP.CONT)
    draw_glyph(t, p, characters["D"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / f"example-crate.svg") as (p, t):
    draw_glyph(t, p, characters["CR"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["T"], pos=VP.AE)

with DrawingContext(output_path=dir / f"example-create.svg") as (p, t):
    draw_glyph(t, p, characters["CR"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["A"], pos=VP.AE)
    draw_glyph(t, p, characters["T"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / f"example-egg.svg") as (p, t):
    draw_glyph(t, p, characters["E"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, characters["G"], pos=VP.CONT, gs=GS.DOUBLE)

with DrawingContext(output_path=dir / f"example-oven.svg") as (p, t):
    draw_glyph(t, p, characters["O"], pos=VP.IY, gs=GS.SINGLE)
    draw_glyph(t, p, characters["V"], pos=VP.CONT, gs=GS.SINGLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["N"], pos=VP.AE)
