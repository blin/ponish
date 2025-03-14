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

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-pony.svg") as (p, t):
        draw_glyph(t, p, characters["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["P"], pos=VP.IY, gs=GS.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["N"], pos=VP.OU)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["end-vowel-dot"], pos=VP.IY)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-bottle.svg") as (p, t):
        draw_glyph(t, p, characters["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["T"], pos=VP.OU)
        draw_glyph(t, p, characters["L"], pos="cont")

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-starship.svg") as (p, t):
        draw_glyph(t, p, characters["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["S"], pos=VP.IY)
        draw_glyph(t, p, characters["T"], pos="cont")
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["R"], pos=VP.AE)
        draw_glyph(t, p, characters["SH"], pos="cont")
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["P"], pos=VP.IY)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-orange.svg") as (p, t):
        draw_glyph(t, p, characters["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["O"], pos=VP.IY)
        draw_glyph(t, p, characters["R"], pos="cont")
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["N"], pos=VP.AE)
        draw_glyph(t, p, characters["J"], pos="cont")

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-edge.svg") as (p, t):
        draw_glyph(t, p, characters["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["E"], pos=VP.IY, gs=GS.DOUBLE)
        draw_glyph(t, p, characters["J"], pos="cont", gs=GS.DOUBLE)

# %%
for article in ["a", "the"]:
    article_pos = VP.OU if article == "the" else VP.AE
    with DrawingContext(output_path=dir / f"example-{article}-buffalo.svg") as (p, t):
        draw_glyph(t, p, characters["article-dot"], pos=article_pos)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["F"], pos=VP.OU)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["L"], pos=VP.AE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, characters["end-vowel-dot"], pos=VP.OU)
