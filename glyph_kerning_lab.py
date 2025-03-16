# %%
import importlib

from jupyturtle.jupyturtle import Drawing, Turtle

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from draw import (
    Page,
    advance_after_glyph,
    draw_glyph,
)
from glyphs import (
    GlyphSize,
    VowelPosition,
    characters,
    chars_with_curves,
)


def show_lines(t: Turtle, p: Page) -> None:
    c1 = t.pen_color
    t.pen_color = "#DDDDDD"
    for i in range(4):
        y = p.current_line_bottom_px - (i * p.vowel_area_height_px)
        print(f"{y=}")
        t.jump_to(y=y, x=0)
        t.heading = 0
        t.forward(1000)
    t.pen_color = c1


i = 3
for g in characters.values():
    drawing = Drawing(width=140, height=80)
    p = Page(vowel_area_height_px=20, current_line_bottom_px=70, current_line_left_px=10)
    t = Turtle(delay=0.00, drawing=drawing)
    show_lines(t, p)
    draw_glyph(t, p, characters["J"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, g, pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
    advance_after_glyph(t, p)
    draw_glyph(t, p, characters["I"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
    t.hide()
