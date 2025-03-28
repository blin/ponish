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

dir = Path("manual/lesson-3")
dir.mkdir(parents=True, exist_ok=True)

text: list[str] = []

text = [
    "$(every)korps on mount $(ever)est was",
    "ons an x$(tr)emly motivated person",
]
for i, line in list(enumerate(text)):
    dc = DrawingContext(
        output_path=dir / f"every-corpse-{i + 1}.svg",
        drawing_width=1100,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_sentence(t, p, line)

text = [
    "The bi$(GR) yu bild the bonfir",
    "the mor dark$(ness) is reveld",
]
for i, line in list(enumerate(text)):
    dc = DrawingContext(
        output_path=dir / f"bonfire-{i + 1}.svg",
        drawing_width=1100,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_sentence(t, p, line)

# TODO: quotes in "aww thank you"
# TODO: "AW" blend
text = [
    "Its so $(FR)us$(TR)at$(ing) bi$(ing) a girl",
    "nd $(TR)y$(ing) to flirt wi$(TH) $(other)girls",
    "Lik yu tel $(TH)em $(TH)er",
    "cut nd $(TH)y go , aw $(thank) yu ! ,",
    "No No Im bi$(ing) ge wi$(TH) yu",
    "Homo ntendd . Damit .",
]
for i, line in list(enumerate(text)):
    dc = DrawingContext(
        output_path=dir / f"homo-intended-{i + 1}.svg",
        drawing_width=1100,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_sentence(t, p, line)

# TODO: make "otherthings" look good.
# TODO: blend AK, AL
text = [
    "On the $(sub)way today a man kam up to me to start a $(con)versa$(SH)n . He mad",
    "smal talk , He was a lonly man talk$(ing) $(about) the we$(TH)r nd $(other)$(thing)s . I",
    "$(TR)id to be $(pl)esant nd akomodat him but my hed began to hurt",
    "from his banality . I almost didnt notice it had hapened but I",
    "$(TH)ru up al $(over) him . He waz not $(PL)ezd . I culdnt stop laf$(ing) .",
]
for i, line in list(enumerate(text)):
    dc = DrawingContext(
        output_path=dir / f"subway-{i + 1}.svg",
        drawing_width=1100,
        drawing_height=150,
    )
    with dc as (p, t):
        draw_sentence(t, p, line)
