# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import draw_word
from draw_jupyturtle import DrawingContext

dir = Path("manual/lesson-3/affix-phrases")
dir.mkdir(parents=True, exist_ok=True)

words = [
    ("aboveground", "$(above)$(GR)ound"),
    ("layabout", "la$(about)"),
    ("antidote", "$(anti)dot"),
    ("automobile", "$(auto)omobil"),
    ("await", "$(awa)at"),
    ("goaway", "go$(away)"),
    ("circulate", "$(circu)lat"),
    ("circumscribe", "$(circum)skrib"),
    ("compose", "$(com)poz"),
    ("construct", "$(con)s$(TR)ukt"),
    ("contradiction", "$(contr)adik$(SH)n"),
    ("disparage", "$(dis)paraj"),
    ("destitute", "$(des)titut"),
    ("peach", "pe$(each)"),
    ("infect", "n$(fect)"),
    ("infection", "n$(fect)$(SH)n"),
    ("spiteful", "spit$(full)"),
    ("spitefulness", "spit$(full)$(ness)"),
    ("graphic", "$(graph)ic"),
    ("grammar", "$(gram)ar"),
    ("sluthood", "slut$(hood)"),
    ("pacify", "pas$(ify)"),
    ("pacification", "pas$(ifycation)"),
    ("guileless", "gil$(less)"),
    ("guilelessness", "gil$(less)$(ness)"),
    ("biology", "bio$(logy)"),
    ("illogical", "i$(logic)al"),
    ("misrepresent", "$(mis)re$(PR)esent"),
    ("mismanagement", "$(mis)manaj$(ment)"),
    ("cleanliness", "clenle$(ness)"),
    ("overdone", "$(over)don"),
    ("otherwise", "$(other)wiz"),
    ("outspoken", "$(out)spoken"),
    ("selfpublish", "$(self)publi$(SH)"),
    ("semitruck", "$(semi)$(TR)uk"),
    ("battleship", "batl$(ship)"),
    ("shipment", "$(ship)$(ment)"),
    ("subway", "$(sub)wa"),
    ("subject", "$(sub)jekt"),
    ("supersonic", "$(super)sonik"),
    ("superluminal", "$(super)luminal"),
    ("transit", "$(trans)it"),
    ("transfer", "$(trans)fer"),
    ("undergo", "$(under)go"),
    ("blunder", "bl$(under)"),
    ("forever", "for$(ever)"),
    ("everybody", "$(every)body"),
    ("variable", "$(very)abl"),
    ("verygood", "$(very)gud"),
    ("toward", "to$(ward)"),
    ("downwards", "down$(ward)s"),
    ("warden", "$(ward)en"),
    ("wardaway", "$(ward)$(away)"),
]
if __name__ == "__main__":
    for name, spelling in words:
        dc = DrawingContext(
            output_path=dir / f"{name}.svg",
            drawing_width=150,
            drawing_height=150,
        )
        with dc as (p, t):
            draw_word(t, p, spelling)
