# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import (
    Page,
    Turtle,
    advance_after_glyph,
    advance_after_word,
    draw_glyph,
)
from draw_jupyturtle import DrawingContext
from glyphs import (
    Glyph,
    characters,
)
from glyphs import (
    GlyphSize as GS,
)
from glyphs import (
    VowelPosition as VP,
)

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

text = [
    "Betwen tims wen oʃns drank Atlantis and riz of",
    "sons of Aryas ðr was an aj undremd of And",
    "unto ðis Conan Destind to ber juld crown of",
    "Aquilonia upon troubled brow It is I his",
    "chronicler wo alone can tel ðe of his saga",
    "Let me tell you of days of high adventure",
]


# NOTES
# Anchoring "B" in "Between" is double-sized
# Anchoring "T" in "times" is double-sized, IY continuing "M" is single-sized
# Anchoring "W" in "when" is double-sized
# Anchoring "O" in "oceans" is single-sized
# Anchoring "D" in "drank" is double-sized, but it is also blended with "R"
# Anchoring "A" in "Atlantis" is double-sized,
# even though it is followed by a consonant.
# But A is a raising character, so there is space to continue downward.
vowels = ["A", "E", "I", "O", "U", "Y"]
# "N" is tricky, the length varies depending on vowel area positioning
# and surrounding characters

def draw_word(
    t: Turtle,
    p: Page,
    word: str,
):
    gq = list(word)

    gpos = VP.IY
    gs = GS.DOUBLE
    first_g = True
    consecutive_vowels = 0

    while len(gq) > 0:
        gid = gq.pop(0)
        gid_up = gid.upper()
        g = characters.get(gid, None) or characters.get(gid.upper(), None)
        assert g, f"Character {gid} not found in character list"

        g_is_vowel = gid_up in vowels
        g_is_last = len(gq) == 0  # TODO: use for vowel-end-dot
        consecutive_vowels = consecutive_vowels + 1 if g_is_vowel else 0

        next_gid_is_vowel = False
        if len(gq) > 0:
            next_gid = gq[0]
            if next_gid.upper() in vowels:
                next_gid_is_vowel = True
        next_gid_is_last = False
        if len(gq) == 1:
            next_gid_is_last = True

        if first_g:
            first_g = False
            gs = GS.SINGLE
            if next_gid_is_vowel:
                gs = GS.DOUBLE
            draw_glyph(t, p, g, pos=VP.IY, gs=gs)
            gpos = VP.CONT
            gs = GS.SINGLE
            continue

        if g_is_vowel and consecutive_vowels == 2:
            consecutive_vowels = 0
        elif g_is_vowel:
            match gid_up:
                case "A" | "E":
                    gpos = VP.AE
                    gs = GS.SINGLE
                case "I" | "Y":
                    gpos = VP.IY
                    if next_gid_is_vowel or next_gid_is_last:
                        gs = GS.DOUBLE
                    else:
                        gs = GS.SINGLE
                case "O" | "U":
                    gpos = VP.OU
                    gs = GS.SINGLE
            advance_after_glyph(t, p)
            continue
        draw_glyph(t, p, g, pos=gpos, gs=gs)
        gpos = VP.CONT
        gs = GS.SINGLE


for i, line in list(enumerate(text)):
    dc = DrawingContext(
        output_path=dir / f"passage-1-line-{i + 1}.svg",
        drawing_width=750,
        drawing_height=150,
    )
    with dc as (p, t):
        wq = line.split(" ")
        for word in line.split():
            draw_word(t, p, word)
            advance_after_word(t, p)
