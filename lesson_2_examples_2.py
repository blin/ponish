# %%
from pathlib import Path

from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    advance_after_glyph,
    draw_glyph,
    get_svg,
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


def prepare() -> tuple[Page, Turtle]:
    u = 20
    drawing = Drawing(width=180, height=u * 5)
    page = Page(
        vowel_area_height_px=u, current_line_bottom_px=(u * 3) + (u // 2), current_line_left_px=u
    )
    turtle = Turtle(delay=0.00, drawing=drawing)
    return page, turtle


def save_turtle(t: Turtle, p: Page, path: Path) -> None:
    t.hide()
    t.drawing.width = p.furthest_from_left_px + p.vowel_area_height_px
    t.drawing.height = p.furthest_from_top_px + p.vowel_area_height_px
    svg = get_svg(t)
    with open(path, "w") as f:
        f.write(svg)


dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

# Example 1
p, t = prepare()
draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
advance_after_glyph(t, p)
draw_glyph(t, p, characters["G"], pos=VP.AE)
save_turtle(t, p, dir / "example-bag.svg")

# Example 2
p, t = prepare()
draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
advance_after_glyph(t, p)
draw_glyph(t, p, characters["G"], pos=VP.IY, gs=GS.DOUBLE)
save_turtle(t, p, dir / "example-big.svg")

# Example 3
p, t = prepare()
draw_glyph(t, p, characters["B"], pos=VP.IY, gs=GS.DOUBLE)
advance_after_glyph(t, p)
draw_glyph(t, p, characters["G"], pos=VP.OU)
save_turtle(t, p, dir / "example-bog.svg")
