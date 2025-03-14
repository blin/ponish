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

# %%
with DrawingContext(output_path=dir / f"example-there.svg") as (p, t):
    draw_glyph(t, p, characters["TH"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, characters["R"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-no.svg") as (p, t):
    draw_glyph(t, p, characters["N"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["end-vowel-dot"], pos=VP.OU)

# %%
with DrawingContext(output_path=dir / f"example-difference.svg") as (p, t):
    draw_glyph(t, p, characters["D"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["F"], pos=VP.IY)
    draw_glyph(t, p, characters["R"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["N"], pos=VP.AE)
    draw_glyph(t, p, characters["S"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-between.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["T"], pos=VP.AE)
    draw_glyph(t, p, characters["W"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["N"], pos=VP.AE)

# %%
with DrawingContext(output_path=dir / f"example-what.svg") as (p, t):
    draw_glyph(t, p, characters["W"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["T"], pos=VP.AE)

# %%
with DrawingContext(output_path=dir / f"example-right.svg") as (p, t):
    draw_glyph(t, p, characters["R"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["T"], pos=VP.IY, gs=GS.DOUBLE)

# %%
with DrawingContext(output_path=dir / f"example-and.svg") as (p, t):
    draw_glyph(t, p, characters["A-one-leg"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, characters["N"], pos="cont", gs=GS.DOUBLE)
    draw_glyph(t, p, characters["D"], pos="cont", gs=GS.DOUBLE)

# %%
with DrawingContext(output_path=dir / f"example-necessary.svg") as (p, t):
    draw_glyph(t, p, characters["N"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["S"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["S"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["R"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["end-vowel-dot"], pos=VP.IY)

# %%
with DrawingContext(output_path=dir / f"example-the-rewards.svg") as (p, t):
    draw_glyph(t, p, characters["article-dot"], pos=VP.OU)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["R"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["W"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["R"], pos=VP.AE)
    draw_glyph(t, p, characters["D"], pos="cont")
    draw_glyph(t, p, characters["S"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-of.svg") as (p, t):
    draw_glyph(t, p, characters["O"], pos=VP.IY)
    draw_glyph(t, p, characters["F"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-tolerance.svg") as (p, t):
    draw_glyph(t, p, characters["T"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["L"], pos=VP.OU)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["R"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["N"], pos=VP.AE)
    draw_glyph(t, p, characters["S"], pos="cont")

# %%
with DrawingContext(output_path=dir / f"example-are.svg") as (p, t):
    draw_glyph(t, p, characters["A-one-leg"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, characters["R"], pos="cont", gs=GS.DOUBLE)

# %%
with DrawingContext(output_path=dir / f"example-treachery.svg") as (p, t):
    draw_glyph(t, p, characters["T"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, characters["R"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["CH"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["R"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["end-vowel-dot"], pos=VP.IY)

# %%
with DrawingContext(output_path=dir / f"example-betrayal.svg") as (p, t):
    draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["T"], pos=VP.AE)
    draw_glyph(t, p, characters["R"], pos="cont")
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["Y"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["L"], pos=VP.AE)
