# %%
from pathlib import Path

from draw import advance_after_glyph, draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import GlyphSize as GS, VowelPosition as VP, all as all_glyphs

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

with DrawingContext(output_path=dir / "example-my.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["M"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["high-dot"], pos=VP.IY)

# %%
with DrawingContext(output_path=dir / "example-armor.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["A-one-leg"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.CONT)
    draw_glyph(t, p, all_glyphs["M"], pos=VP.CONT)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.OU)

# %%
with DrawingContext(output_path=dir / "example-is.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["I"], pos=VP.IY)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-contempt.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["C"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.OU)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.CONT)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["M"], pos=VP.AE)
    draw_glyph(t, p, all_glyphs["P"], pos=VP.CONT)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-shield.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["SH"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["L"], pos=VP.IY)
    draw_glyph(t, p, all_glyphs["D"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-disgust.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["D"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.IY)
    draw_glyph(t, p, all_glyphs["G"], pos=VP.CONT)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.OU)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-sword.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["S"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.OU)
    draw_glyph(t, p, all_glyphs["D"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-hatred.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["H"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["TR"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["D"], pos=VP.AE)

# %%
with DrawingContext(output_path=dir / "example-there.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["TH"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-no.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["N"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["high-dot"], pos=VP.OU)

# %%
with DrawingContext(output_path=dir / "example-difference.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["D"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["FR"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.AE)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-between.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.AE)
    draw_glyph(t, p, all_glyphs["W"], pos=VP.CONT)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.AE)

# %%
with DrawingContext(output_path=dir / "example-what.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["W"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.AE)

# %%
with DrawingContext(output_path=dir / "example-right.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["R"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.IY, gs=GS.DOUBLE)

# %%
with DrawingContext(output_path=dir / "example-and.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["A-one-leg"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.CONT, gs=GS.DOUBLE)
    draw_glyph(t, p, all_glyphs["D"], pos=VP.CONT, gs=GS.DOUBLE)

# %%
with DrawingContext(output_path=dir / "example-necessary.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["N"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["high-dot"], pos=VP.IY)

# %%
with DrawingContext(output_path=dir / "example-the-rewards.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["low-dot"], pos=VP.OU)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["W"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.AE)
    draw_glyph(t, p, all_glyphs["D"], pos=VP.CONT)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-of.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["O"], pos=VP.IY)
    draw_glyph(t, p, all_glyphs["F"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-tolerance.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["T"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["L"], pos=VP.OU)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.AE)
    draw_glyph(t, p, all_glyphs["S"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-are.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["A-one-leg"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.CONT, gs=GS.DOUBLE)

# %%
with DrawingContext(output_path=dir / "example-treachery.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["TR"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["CH"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["R"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["high-dot"], pos=VP.IY)

# %%
with DrawingContext(output_path=dir / "example-betrayal.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["B"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["TR"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["Y"], pos=VP.AE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["L"], pos=VP.AE)
