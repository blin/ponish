# %%
from jupyturtle.jupyturtle import Drawing, Turtle

from draw import (
    Page,
    advance_after_glyph,
    draw_glyph,
    get_svg,
)
from glyphs import (
    GlyphSize,
    VowelPosition,
    characters,
)

u = 20

def prepare() -> tuple[Page, Turtle]:
    """
    Prepare a new drawing environment with standard settings.
    
    Returns:
        A tuple containing (page, turtle)
    """
    drawing = Drawing(width=180, height=u * 5)
    page = Page(vowel_area_height_px=u, current_line_bottom_px=(u * 3) + (u // 2), current_line_left_px=u)
    turtle = Turtle(delay=0.00, drawing=drawing)
    return page, turtle

# Example 1
p, t = prepare()
draw_glyph(t, p, characters["B"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
advance_after_glyph(t, p)
draw_glyph(t, p, characters["G"], pos=VowelPosition.AE)
t.hide()

# Example 2
p, t = prepare()
draw_glyph(t, p, characters["B"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
advance_after_glyph(t, p)
draw_glyph(t, p, characters["G"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
t.hide()

# Example 3
p, t = prepare()
draw_glyph(t, p, characters["B"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
advance_after_glyph(t, p)
draw_glyph(t, p, characters["G"], pos=VowelPosition.OU)
t.hide()
