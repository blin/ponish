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
    ("automobile", "$(auto)mobile"),
    ("await", "$(awa)it"),
    ("goaway", "go$(away)"),
    ("circulate", "$(circu)late"),
    ("circumscribe", "$(circum)scribe"),
    ("compose", "$(com)pose"),
    ("construct", "$(con)struct"),
    ("contradiction", "$(contr)adiction"),
    ("disparage", "$(dis)parage"),
    ("destitute", "$(des)titute"),
    ("peach", "p$(each)"),
    ("infect", "in$(fect)"),
    ("infection", "infection"),
    ("spiteful", "spiteful"),
    ("spitefulness", "spiteful$(ness)"),
    ("graphic", "$(graph)ic"),
    ("grammar", "$(gram)mar"),
    ("sluthood", "slut$(hood)"),
    ("pacify", "pac$(ify)"),
    ("pacification", "pacification"),
    ("guileless", "guile$(less)"),
    ("guilelessness", "guileless$(ness)"),
    ("biology", "bio$(logy)"),
    ("illogical", "illogical"),
    ("misrepresent", "$(mis)represent"),
    ("mismanagement", "$(mis)manage$(ment)"),
    ("cleanliness", "cleanli$(ness)"),
    ("overdone", "$(over)done"),
    ("otherwise", "$(other)wise"),
    ("outspoken", "$(out)spoken"),
    ("selfpublish", "$(self)publish"),
    ("semitruck", "$(semi)truck"),
    ("battleship", "battle$(ship)"),
    ("shipment", "$(ship)$(ment)"),
    ("subway", "$(sub)way"),
    ("subject", "$(sub)ject"),
    ("supersonic", "$(super)sonic"),
    ("superluminal", "$(super)luminal"),
    ("transit", "$(trans)it"),
    ("transfer", "$(trans)fer"),
    ("undergo", "$(under)go"),
    ("blunder", "bl$(under)"),
    ("forever", "for$(ever)"),
    ("everybody", "$(every)body"),
    ("variable", "variable"),
    ("verygood", "$(very)good"),
    ("toward", "to$(ward)"),
    ("downwards", "downwards"),
    ("warden", "$(ward)en"),
    ("wardaway", "$(ward)$(away)"),
]
for name, spelling in words:
    dc = DrawingContext(
        output_path=dir / f"{name}.svg",
        drawing_width=150,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_word(t, p, spelling)
