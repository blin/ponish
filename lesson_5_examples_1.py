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
        "passage-1",
        [
            "Once upon a time , in the magical land of Equestria , there were two regal sisters who ruled",
            "together and created harmony for all the land . To do this , the eldest used her unicorn powers",
            "to raise the sun at dawn ; the younger brought out the moon to begin the night . Thus , the two sisters maintained balance for their",
            "kingdom and their subjects , all the different types of ponies .",
            # paragraph
            "But as time went on , the younger sister became resentful . The ponies relished and played in the day",
            "her elder sister brought forth , but shunned , and slept through her beautiful night . One fateful",
            "day , the younger unicorn refused to lower the moon to make way for the dawn . The elder sister tried to reason",
            "with her , but the bitterness in the young ones heart had transformed her into a wicked mare of darkness :",
            "Nightmare Moon !",
            # paragraph
            "She vowed that she would shroud the land in eternal night . Reluctantly , the elder sister harnessed",
            "the most powerful magic known to Ponydom: the Elements of Harmony . Using the magic of",
            "the Elements of Harmony , she defeated her younger sister , and banished her permanently in the moon .",
            "The elder sister took on responsibility for both sun , and moon , and harmony has",
            "been maintained in Equestria for generations since .",
        ],
    ),
]
if __name__ == "__main__":
    for text_name, text in texts:
        for i, line in list(enumerate(text)):
            dc = DrawingContext(
                output_path=dir / f"{text_name}-line-{i + 1:02}.svg",
                drawing_width=1100,
                drawing_height=150,
            )
            with dc as (p, t):
                draw_sentence(t, p, line)
