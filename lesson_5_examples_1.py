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
    [
        # TODO: 2 as a number in a circle
        "Ons upon a tim n the majikal land of Eqes$(TR)ea $(TH)r wer two regal $(SS)$(TR)s wo ruld",
        "toge$(TH)er nd $(CR)e$(AT)ed harmony for $(AL) the land . Todo$(TH)is , the eldest usd her unikorn powers",
        "toraz the sun $(AT)dawn ; the $(Y-consonant)o$(NG)r $(BR)ot ot the mon tobegin the nit . $(TH)us , the two $(SS)$(TR)s mintind balans for $(TH)r",
        "ki$(ng)dom nd $(TH)r $(sub)jekts , $(AL) the di$(FR)ent typs of pones .",
        # paragraph
        "But $(AS) tim went on , the $(Y-consonant)o$(NG)r $(SS)$(TR) bekam resent$(full) . The pones reli$(SH)ed nd $(PL)ayd n the dy",
        # TODO: make "rth" in "forth" look better
        "her el$(DR) $(SS)$(TR) $(BR)ot for$(TH) , but $(SH)unnd , nd slept $(TH)ru her buti$(full) nit . On fat$(full)",
        "dy , the $(Y-consonant)o$(NG)r unikorn refusd tolower the mon tomak wy for the dawn . The el$(DR) $(SS)$(TR) $(TR)id toreson",
        "wi$(TH) her but the bi$(tr)$(ness) n the $(Y-consonant)o$(NG) ons hart had $(TR)ansformed her nto$(awa)iked mar of dark$(ness) :",
        "nitmar mon !",
        # paragraph
        "$(SH)evowed $(TH)at $(SH)ewould $(SH)roud the land n eternal nit . Reluktantly , the elder $(SS)$(TR) har$(ness)ed",
        # TODO: make "using" look better
        "the most power$(full) majik nown toPonydom : the Ele$(ment)s of Harmony . Us$(ING) the majik of",
        "the Ele$(ment)s of Harmony , $(SH)edefeted her $(Y-consonant)o$(NG)r $(SS)$(TR) nd bani$(SH)d her permanently to the mon .",
        "The elder $(SS)$(TR) tok on responsibility for bo$(TH) sun nd mon , nd harmony has",
        "ben mintind n Eqes$(TR)ea for jenera$(SH)ns sins .",
    ],
    [
        "The $(PR)oblem isnt $(TH)at Joni kant red .",
        "The $(PR)oblem isnt evn $(TH)at Joni kant",
        # TODO: check the "the" dot before "problem"
        "$(think) . The $(PR)oblem is $(TH)at Joni doznt",
        # TODO: make "thinking" look better
        "nowat $(think)$(ng) is ; he$(con)fu$(SS) it",
        # TODO: make "feeling" look better
        "wi$(TH) fel$(ng) .",
    ],
    [
        "Two figurs ly sprawld on the Eqes$(TR)e$(AN) $(GR)as talk$(ing) nd laf$(ing) merily . On was",
        # TODO: braces around Bellerophon
        # TODO: chunk after second consecutive vowel
        # TODO: "quote mode"
        "human ; a relativly $(Y-consonant)o$(ng) man wi$(TH) the unlikly nam of Lero , $(SH)ort for Bie lilie rio pihio n",
        "for his parents had ben od folk , wod ndd up her $(TH)ru nomekanism he or $(AN)yon",
        "els had $(Y-consonant)et ben $(AB)l to$(dis)ern nd wo $(AS) $(Y-consonant)et waz unabl toreturn hom . Hewas",
        "slitly stoky wi$(TH) farly wid $(SH)ol$(DR)s nd a barel $(CH)est nd had $(SH)ol$(DR) le$(NG)$(TH-top-start) redi$(SH)blond har",
        "nd a netly $(tr)imed red musta$(SH) nd gote .",
        # paragraph
        # TODO: "AP" blend
        "the $(other)figur waz mu$(CH) smalr . the skyblu cot nd ranbow man nd tal of the pega$(SS) aptly",
        # TOOD: "AG" blend
        "named RanboDa$(SH) stod $(out) aganst the dep $(GR)en of the $(GR)as . $(SH)ed flopd down half $(AT)op the human",
        # TODO: what to do with "acr" in "across"?
        "wen $(TH)eyd stopd torest nd now ly wi$(TH) her hed nd on forleg a$(CR)os his",
        "$(CH)est nd on wi$(NG) spred $(AK)ros his torso . the human idly s$(tr)okd her man wi$(TH) on",
        "hand wil the two $(CH)er$(full)y revisited the pikup hofbal gam $(TH)ed just fini$(SH)d n the vilaj",
        "$(GR)en .",
    ],
]
if __name__ == "__main__":
    for tid, text in list(enumerate(texts))[2:]:
        for lid, line in list(enumerate(text)):
            dc = DrawingContext(
                output_path=dir / f"passage-{tid + 1}-line-{lid + 1:02}.svg",
                drawing_width=1100,
                drawing_height=150,
            )
            with dc as (p, t):
                draw_sentence(t, p, line)
