# %%
from pathlib import Path

from draw import (
    advance_after_glyph,
    draw_glyph,
)
from draw_jupyturtle import DrawingContext
from glyphs import (
    Circle,
    Direction,
    Glyph,
    PolarLine,
    RelPoint,
    Rotation,
    characters,
)
from glyphs import (
    GlyphSize as GS,
)
from glyphs import (
    VowelPosition as VP,
)

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

with DrawingContext(output_path=dir / f"example-my.svg") as (p, t):
    draw_glyph(t, p, characters["M"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["end-vowel-dot"], pos=VP.IY)

# %%
with DrawingContext(output_path=dir / f"example-armor.svg") as (p, t):
    draw_glyph(t, p, characters["A-one-leg"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, characters["R"], pos="cont")
    draw_glyph(t, p, characters["M"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["R"], pos=VP.OU)

# %%
with DrawingContext(output_path=dir / f"example-is.svg") as (p, t):
    draw_glyph(t, p, characters["I"], pos=VP.IY)
    draw_glyph(t, p, characters["S"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-contempt.svg") as (p, t):
    draw_glyph(t, p, characters["C"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["N"], pos=VP.OU)
    draw_glyph(t, p, characters["T"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["M"], pos=VP.AE)
    draw_glyph(t, p, characters["P"], pos="cont")
    draw_glyph(t, p, characters["T"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-shield.svg") as (p, t):
    draw_glyph(t, p, characters["SH"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["L"], pos=VP.IY)
    draw_glyph(t, p, characters["D"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-disgust.svg") as (p, t):
    draw_glyph(t, p, characters["D"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["S"], pos=VP.IY)
    draw_glyph(t, p, characters["G"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["S"], pos=VP.OU)
    draw_glyph(t, p, characters["T"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-sword.svg") as (p, t):
    draw_glyph(t, p, characters["S"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["R"], pos=VP.OU)
    draw_glyph(t, p, characters["D"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-hatred.svg") as (p, t):
    draw_glyph(t, p, characters["H"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["T"], pos=VP.AE)
    draw_glyph(t, p, characters["R"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["D"], pos=VP.AE)
