# %%
from draw import draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import VowelPosition, letters

for letter_id, letter in letters.items():
    output_path = f"manual/alphabet/{letter_id}.svg"
    with DrawingContext(output_path=output_path, drawing_width=40) as (p, t):
        p.vowel_area_height_px = 20
        p.current_line_bottom_px = 30
        p.current_line_left_px = 10
        draw_glyph(t, p, letter, pos=VowelPosition.OU)
