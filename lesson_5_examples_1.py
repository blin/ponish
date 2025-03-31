# %%
import importlib

import draw
import glyphs

importlib.reload(glyphs)
importlib.reload(draw)
# https://github.com/ipython/ipython/issues/12399
# reloading draw first, then glyphs results in isinstance checks being broken

from pathlib import Path

from draw import draw_sentence
from draw_jupyturtle import DrawingContext

dir = Path("manual/part-2")
dir.mkdir(parents=True, exist_ok=True)

texts = [
    (
        # TODO: 2 as a number in a circle
        "Ons upon a tim n the majikal land of Eqes$(TR)ea $(TH)r wer two regal $(SS)$(TR)s wo ruld",
        "toge$(TH)er nd $(CR)e$(AT)ed harmony for $(AL) the land . Todo$(TH)is , the eldest usd her unikorn powers",
        "toraz the sun $(AT)dawn ; the yo$(NG)er $(BR)ot ot the mon tobegin the nit . $(TH)us , the two $(SS)$(TR)s mintind balans for $(TH)r",
        "ki$(ng)dom nd $(TH)r $(sub)jekts , $(AL) the di$(FR)ent typs of pones .",
        # paragraph
        "But as time went on , the younger $(SS)$(TR) became resentful . The ponies relished nd played in the day",
        "her elder $(SS)$(TR) brought for$(TH) , but shunnd , nd slept $(TH)rough her beautiful nit . One fateful",
        "day , the younger unikorn refused to lower the moon to make way for the dawn . The elder $(SS)$(TR) $(TR)ied to reason",
        "wi$(TH) her , but the bitterness in the young ones heart had $(TR)ansformed her into a wicked mare of darkness :",
        "nitmare Moon !",
        # paragraph
        "She vowed $(TH)at she would shroud the land in eternal nit . Reluctantly , the elder $(SS)$(TR) harnessed",
        "the most powerful magic known to Ponydom: the Elements of Harmony . Using the magic of",
        "the Elements of Harmony , she defeated her younger $(SS)$(TR) , nd banished her permanently in the moon .",
        "The elder $(SS)$(TR) took on responsibility for bo$(TH) sun , nd moon , nd harmony has",
        "been mintind in Eques$(TR)ea for generations since .",
    ),
]
if __name__ == "__main__":
    for tid, text in enumerate(texts):
        for lid, line in list(enumerate(text))[2:6]:
            dc = DrawingContext(
                output_path=dir / f"passage-{tid + 1}-line-{lid + 1:02}.svg",
                drawing_width=1100,
                drawing_height=150,
            )
            with dc as (p, t):
                draw_sentence(t, p, line)
