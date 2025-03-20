# %%
from pathlib import Path

from draw import advance_after_glyph, draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import GlyphSize as GS
from glyphs import VowelPosition as VP
from glyphs import all as all_glyphs

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-pony.svg") as (p, t):
        draw_glyph(t, p, all_glyphs["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["P"], pos=VP.IY, gs=GS.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["N"], pos=VP.OU)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["end-vowel-dot"], pos=VP.IY)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-bottle.svg") as (p, t):
        draw_glyph(t, p, all_glyphs["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["B"], pos=VP.IY, gs=GS.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["T"], pos=VP.OU)
        draw_glyph(t, p, all_glyphs["L"], pos=VP.CONT)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-starship.svg") as (p, t):
        draw_glyph(t, p, all_glyphs["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["S"], pos=VP.IY)
        draw_glyph(t, p, all_glyphs["T"], pos=VP.CONT)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["R"], pos=VP.AE)
        draw_glyph(t, p, all_glyphs["SH"], pos=VP.CONT)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["P"], pos=VP.IY)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-orange.svg") as (p, t):
        draw_glyph(t, p, all_glyphs["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["O"], pos=VP.IY)
        draw_glyph(t, p, all_glyphs["R"], pos=VP.CONT)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["N"], pos=VP.AE)
        draw_glyph(t, p, all_glyphs["J"], pos=VP.CONT)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-edge.svg") as (p, t):
        draw_glyph(t, p, all_glyphs["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["E"], pos=VP.IY, gs=GS.DOUBLE)
        draw_glyph(t, p, all_glyphs["J"], pos=VP.CONT, gs=GS.DOUBLE)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-buffalo.svg") as (p, t):
        draw_glyph(t, p, all_glyphs["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["B"], pos=VP.IY, gs=GS.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["F"], pos=VP.OU)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["L"], pos=VP.AE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["end-vowel-dot"], pos=VP.OU)
