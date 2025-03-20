# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import Page, Turtle, advance_after_glyph, advance_after_word, draw_glyph
from draw_jupyturtle import DrawingContext
from glyphs import Glyph
from glyphs import GlyphSize as GS
from glyphs import VowelPosition as VP
from glyphs import all as all_glyphs

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

text = [
    "Betwen tims wen oʃns $(DR)ank $(AT)lantis $(AN)d riz of",
    "sons of $(AR)y$(AS) ðr was $(AN) $(AJ) un$(DR)emd of $(AN)d",
    "unto ðis Conan Destind to ber juld crown of",
    "$(AQ)ilonia upon $(TR)obld brow It is I his",
    "cronicler wo alone kan tel ðe of his saga",
    "Let me tel y of des of hi $(AD)ven$(ʧR)e",
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
# and surrounding all_glyphs


def gid_at(word: str, idx: int) -> tuple[str, int]:
    subword = word[idx:]
    assert len(subword) > 0, f"id_at({word=}, {idx=}), empty subword"
    if len(subword) > 3 and subword[0] == "$" and subword[1] == "(":
        rb = subword.find(")")
        if rb == -1:
            raise ValueError(f"unterminated $() sequence in {word=}")
        gid = subword[2:rb]
        return gid, len(gid) + 3
    return subword[0], 1


def draw_word(
    t: Turtle,
    p: Page,
    word: str,
):
    word_pos = 0

    gpos = VP.IY
    gs = GS.DOUBLE
    first_g = True
    consecutive_vowels = 0

    while word_pos < len(word):
        gid, advance = gid_at(word, word_pos)
        word_pos += advance

        gid_up = gid.upper()
        g = all_glyphs.get(gid, None) or all_glyphs.get(gid.upper(), None)
        assert g, f"Character {gid} not found in character list"

        g_is_vowel = gid_up in vowels
        g_is_last = word_pos >= len(word)  # TODO: use for vowel-end-dot
        consecutive_vowels = consecutive_vowels + 1 if g_is_vowel else 0

        next_gid_is_vowel = False
        next_gid_advance = 0
        if word_pos < len(word):
            next_gid, next_gid_advance = gid_at(word, word_pos)
            if next_gid.upper() in vowels:
                next_gid_is_vowel = True
        next_gid_is_last = False
        if word_pos + next_gid_advance >= len(word):
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
