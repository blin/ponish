# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from draw import Page, Turtle, advance_after_glyph, draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import GlyphSize, VowelPosition, all as all_glyphs


def show_lines(t: Turtle, p: Page) -> None:
    c1 = t.pen_color
    t.pen_color = "#DDDDDD"
    for i in range(4):
        y = p.current_line_bottom_px - (i * p.vowel_area_height_px)
        t.jump_to(y=y, x=0)
        t.heading = 0
        t.forward(1000)
    t.pen_color = c1


for g in all_glyphs.values():
    with DrawingContext(drawing_width=140) as (p, t):
        p.vowel_area_height_px = 20
        p.current_line_bottom_px = 70
        p.current_line_left_px = 10
        show_lines(t, p)
        draw_glyph(t, p, all_glyphs["J"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, g, pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
        advance_after_glyph(t, p)
        draw_glyph(t, p, all_glyphs["I"], pos=VowelPosition.IY, gs=GlyphSize.DOUBLE)
