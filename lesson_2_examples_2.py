# %%
from pathlib import Path

from draw import advance_after_glyph, draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import GlyphSize as GS, VowelPosition as VP, all as all_glyphs

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

for c1, c2 in [
    ("B", "G"),
    ("T", "M"),
    ("F", "N"),
    ("L", "P"),
    ("D", "high-dot"),
    ("S", "high-dot"),
]:
    for pos in [VP.AE, VP.IY, VP.OU]:
        with DrawingContext(
            output_path=dir / f"example-{c1.lower()}-{pos.value}-{c2.lower()}.svg"
        ) as (p, t):
            draw_glyph(t, p, all_glyphs[c1], pos=VP.IY, gs=GS.DOUBLE)
            advance_after_glyph(t, p)
            draw_glyph(t, p, all_glyphs[c2], pos=pos, gs=GS.DOUBLE if pos == VP.IY else GS.SINGLE)


# %%
with DrawingContext(output_path=dir / "example-pond.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["P"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.OU)
    draw_glyph(t, p, all_glyphs["D"], pos=VP.CONT)

with DrawingContext(output_path=dir / "example-pound.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["P"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["U"], pos=VP.OU)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.CONT)
    draw_glyph(t, p, all_glyphs["D"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-crate.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["CR"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.AE)

with DrawingContext(output_path=dir / "example-create.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["CR"], pos=VP.IY, gs=GS.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["A"], pos=VP.AE)
    draw_glyph(t, p, all_glyphs["T"], pos=VP.CONT)

# %%
with DrawingContext(output_path=dir / "example-egg.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["E"], pos=VP.IY, gs=GS.DOUBLE)
    draw_glyph(t, p, all_glyphs["G"], pos=VP.CONT, gs=GS.DOUBLE)

with DrawingContext(output_path=dir / "example-oven.svg") as (p, t):
    draw_glyph(t, p, all_glyphs["O"], pos=VP.IY, gs=GS.SINGLE)
    draw_glyph(t, p, all_glyphs["V"], pos=VP.CONT, gs=GS.SINGLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, all_glyphs["N"], pos=VP.AE)
