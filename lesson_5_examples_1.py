# %%
import importlib
from itertools import chain

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

text_combined: list[str] = []
texts: list[list[str]] = []

texts = [
    [
        "Ons upon a tim n the majikal land of Eqes$(TR)ea $(TH)r wer two regal $(SS)$(TR)s wo ruld",
        "toge$(TH)er nd $(CR)e$(AT)ed harmony for $(AL) the land . Todo$(TH)is , the eldest usd her unikorn powers",
        "toraz the sun $(AT)dawn ; the $(Y-consonant)o$(NG)r $(BR)ot ot the mon tobegin the nit . $(TH)us , the two $(SS)$(TR)s mintind balans for $(TH)r",
        "ki$(ng)dom nd $(TH)r $(sub)jekts , $(AL) the di$(FR)ent typs of pones .",
        # paragraph
        "But $(AS) tim went on , the $(Y-consonant)o$(NG)r $(SS)$(TR) bekam resent$(full) . The pones reli$(SH)ed nd $(PL)ayd n the dy",
        "her el$(DR) $(SS)$(TR) $(BR)ot for$(TH-left-start) , but $(SH)unnd , nd slept $(TH)ru her buti$(full) nit . On fat$(full)",
        "dy , the $(Y-consonant)o$(NG)r unikorn refusd tolower the mon tomak wy for the dawn . The el$(DR) $(SS)$(TR) $(TR)id toreson",
        "wi$(TH) her but the bi$(tr)$(ness) n the $(Y-consonant)o$(NG) ons hart had $(TR)ansformed her nto$(awa)iked mar of dark$(ness) :",
        "nitmar mon !",
        # paragraph
        "$(SH)evowed $(TH)at $(SH)ewould $(SH)roud the land n eternal nit . Reluktantly , the el$(DR) $(SS)$(TR) har$(ness)ed",
        "the most power$(full) majik nown toPonydom : the Ele$(ment)s of Harmony . Us$(ING) the majik of",
        "the Ele$(ment)s of Harmony , $(SH)edefeted her $(Y-consonant)o$(NG)r $(SS)$(TR) nd bani$(SH)d her permanently to the mon .",
        "The el$(DR) $(SS)$(TR) tok on responsibility for bo$(TH) sun nd mon , nd harmony has",
        "ben mintind n Eqes$(TR)ea for jenera$(SH)ns sins .",
    ],
    [
        "The $(PR)oblem isnt $(TH)at Joni kant red .",
        "The $(PR)oblem isnt evn $(TH)at Joni kant",
        "$(think) . The $(PR)oblem is $(TH)at Joni doznt",
        "nowat $(think)$(ng) is ; he$(con)fu$(SS) it",
        "wi$(TH) fel$(ng) .",
    ],
    [
        "Two figurs ly sprawld on the Eqes$(TR)e$(AN) $(GR)as talk$(ing) nd laf$(ing) merily . On was",
        # TODO: chunk after second consecutive vowel
        "human ; a relativly $(Y-consonant)o$(ng) man wi$(TH) the unlikly nam of Lero , $(SH)ort for Bie lilie rio pihio n",
        "for his parents had ben od folk , wod ndd up her $(TH)ru nomekanism he or $(AN)yon",
        "els had $(Y-consonant)et ben $(AB)l to$(dis)ern nd wo $(AS) $(Y-consonant)et waz unabl toreturn hom . Hewas",
        "slitly stoky wi$(TH) farly wid $(SH)ol$(DR)s nd a barel $(CH)est nd had $(SH)ol$(DR) le$(NG)$(TH-top-start) redi$(SH)blond har",
        "nd a netly $(tr)imed red musta$(SH) nd gote .",
        # paragraph
        "the $(other)figur waz mu$(CH) smalr . the skyblu cot nd ranbow man nd tal of the pega$(SS) $(AP)tly",
        "named RanboDa$(SH) stod $(out) $(AG)anst the dep $(GR)en of the $(GR)as . $(SH)ed flopd down half $(AT)op the human",
        "wen $(TH)eyd stopd torest nd now ly wi$(TH) her hed nd on forleg a$(CR)os his",
        "$(CH)est nd on wi$(NG) spred $(AK)ros his torso . the human idly s$(tr)okd her man wi$(TH) on",
        "hand wil the two $(CH)er$(full)y revisited the pikup hofbal gam $(TH)ed just fini$(SH)d n the vilaj",
        "$(GR)en .",
    ],
    [
        "statistiks $(AR) lik bikinis ; wat thy revel is",
        "sujestiv nd wat thy $(con)sil is vital but",
        "nakura$(SS) mad n a efort to$(pr)omot a pet",
        "posi$(SH)n $(AR) $(PR)ety ugly noma$(TR) wat $(TH)er",
        "$(DR)esd n .",
    ],
    [
        "fiften galaxis $(out)$(FR)om eqes$(TR)ea on of seleste$(AS) copes notisd an od radio signal",
        "manat$(ing) $(FR)om a nerby star $(SS)tem . on klosr nspek$(SH)n the signal aperd tobecom$(ING) $(FR)om a $(PL)anet",
        "$(SH)ehad sin many $(PL)anets giv of $(com)$(PL)ex nonregular radio signals but upon nvestiga$(SH)n non",
        "of $(TH)es $(PL)anets had human lif , mak$(ING) $(TH)em saf toreus $(AS) raw materi$(AL) to$(GR)o eqes$(TR)ea .",
        # paragraph
        "$(SH)estuded the signals ker$(full)y for $(Y-consonant)ers wil $(SH)e$(TR)avld $(TH)ru n$(TR)stelar spas . the mor $(SH)esaw the mor",
        "$(con)fident $(SH)ewas $(TH)at $(TH)ez signals wer sent by humans . selestea $(PR)edikted $(TH)at if $(SH)e $(SH)owd",
        "the dekodd videos to the $(very)ld pones bak n eqes$(TR)ea non of $(TH)em would hav rekognizd",
        "the $(CR)e$(CH)rs wi$(TH) six apendajes $(AS) humans but $(TH)at didnt ma$(TR) . hana had ritn the defini$(SH)n of",
        "wat a human was ntoher cor utility fu$(NK)$(SH)n .",
        # paragraph
        "the kopy of $(PR)in$(SS) selestia nu wat $(SH)ehad todo $(SH)ehad tosatisfy $(TH)r valus $(TH)ru $(FR)ind$(SH)ip",
        "nd pones",
    ],
    [
        "Hewolnot reson is a bigot ;",
        "hewo kanot is a ful ;",
        "nd he wo dars not is a slav",
    ],
    [
        "wat we xperiens n $(DR)ems $(AS)um$(ING) $(TH)at",
        "wexperiens it often belo$(NG)s n the nd",
        "just $(AS) mu$(CH) to the $(over)al ekonomy of",
        "our soul $(AS) ny$(THING) xperinsd $(AK)$(CH)u$(AL)y ; we$(AR)",
        "ri$(ʧR) or purer on $(AK)ount of it .",
    ],
]
text_combined.extend(chain.from_iterable(texts))
if __name__ == "__main__":
    for tid, text in list(enumerate(texts)):
        for lid, line in list(enumerate(text)):
            dc = DrawingContext(
                output_path=dir / f"passage-{tid + 1}-line-{lid + 1:02}.svg",
                drawing_width=1100,
                drawing_height=150,
            )
            with dc as (p, t):
                draw_sentence(t, p, line)

texts = [
    [
        "id lik to$(PR)efas $(TH)is bysa$(ING) I de$(PL)y apolojiz for the $(DR)op n rit$(ING) qality to$(ward)s the nd . I have tolev",
        "n a few hours nd wilnot beher for somtim . I wantd tofini$(SH) qicly soikan $(AN)ser $(AN)y qes$(CH)ons if",
        "$(AN)yons evn her ritnow",
        # paragraph
        "iv $(AL)redy posted $(TH)is part , so$(TH)ers nopoint n go$(ING) ntodetel . Bak n desem$(BR) of twenty $(TH)irten Iwaz",
        "nvolved n a kar kra$(SH) $(TH)at ultimatly ndd n mybe$(ING) $(PR)onaunsed $(BR)anded . $(AS) Ibled $(out) just $(AS)",
        "the paramediks $(AR)ivd nd did $(about) forty min la$(TR) .",
        # paragraph
        "it tuk $(PL)as n $(TH)re diferent loka$(SH)ns . $(AT) first ifekam $(self)ewar n an $(AB)ys . $(TH)is n nd of it$(self) was",
        "no$(THING) spe$(SH)al , I figurd I must behavi$(NG) a lusid $(DR)em wi$(TH) noactu$(AL) $(DR)em$(ING) okur$(ing) . af$(TR) resid$(ing)",
        "n the $(AB)ys for around a minut I began to$(DR)ift of nd lost $(con)$(SH)es$(ness) for the se$(con)d tim .",
        # paragraph
        "the se$(con)d loka$(SH)n was posibly the most jenerik on . iwas n the hospital rom . $(AL)$(TH)o ihad nofisikal body",
        "myvi$(ZH)n was posi$(SH)nd $(AS) if I was len$(ING) $(over) the cot nd star$(ING) $(AT) my$(self) n $(TH)is staj of the xperiens .",
        "I couldnt fokus on $(AN)y$(THING) . I$(TR)id to$(under)stand wat was hapene$(NG) but $(com)$(PL)itly forgot my$(TR)al of $(TH)ot",
        "$(AF)$(TR) a fu sekonds . the only $(THING) I kould a$(CH)u$(AL)y focus on was a klok on a tabl next to the cot",
        "wi$(CH) red for etin P M . the same $(DR)owsy fel$(ING) $(FR)om the $(AB)ys returnd nd I fadd $(FR)om $(con)$(SH)es$(ness) $(AG)an .",
        # paragraph
        "I had now spent a colektiv tim of two minus n the $(AB)ys nd the rum .",
        # paragraph
        "the $(TH)ird loka$(SH)n waz nterly nexplikabl .ra$(TH)r $(TH)an be$(ING) n the hospital bed Iwaz $(PR)oped up $(AG)anst",
        "a $(TR)e n a smal fild . the sun waz begini$(NG) toset $(over) the o$(SH)n n the $(dis)tans nd loca$(SH)n $(AS)id no$(THING) was $(out)",
        "of the ordinary . $(con)$(TR)ary to the $(over)welm$(ING) majority of $(DR)ems $(TH)r was noblur bak$(DR)op $(TH)at faded ntno$(THING) . $(TH)r waz",
        "no$(GR)ogi haf $(awa)ak fel$(ING) $(TH)at $(AL)was li$(NG)rs n evn lusid $(DR)ems . I was wid $(awa)ak nd bri$(THING) nd",
        "swalo$(ING) manu$(AL)y . icould se perfektly klerly $(AL) the wyup to the horizon . I kould evn fel the vari$(ING)",
        "levels of pan wan I tested . For a mo$(ment) I $(TH)ot I was $(AK)$(CH)u$(AL)y $(awa)ak .",
        # paragraph
        "$(TH)ats wen I herd her .",
        # paragraph
        "$(ever)y$(THING) is go$(ING) tobe$(AL)rit , $(AN)on .",
        # paragraph
        "I rekognizd $(TH)at vois $(AS) sun $(AS) I herd it . I turnd toluk $(AT) her but couldnt say $(AN)i$(THING) .",
        "For som reson $(every)$(THING) sudnly mad sens . I remem$(BR)d the $(CR)a$(SH) , I remem$(BR)d the $(AB)ys , nd luk$(ing) $(AT) mybody . I wantd",
        "to$(THINK) I waz stil $(AL)iv nd it was just a $(DR)im , but I nu I had did .",
        # paragraph
        "Iv n$(ever) ben a relijius or spiri$(CH)u$(AL) person . $(AS) su$(CH) I $(CH)alkd the hol $(THING) up to$(every) x$(PL)ana$(SH)n to N D E S",
        "Id $(ever) herd of .",
    ],
    [
        "An $(AL)most hurt x$(PR)e$(SH)n $(GR)ew on her $(AS) the $(TH)ots wer run$(ING) $(TH)ru myhed . $(SH)esem$(ING)ly saw my$(dis)$(TR)es nd puld mento",
        "a hug .",
        # paragraph
        "I could fel her body warm$(TH) I could fel a tuft on her $(CH)est . I could fel ndividu$(AL) s$(TR)ands of",
        "her man on the bak of my nek . I kould evn her her bre$(THING) . $(every)$(THING) $(AB)out her was far toliflik",
        "tobe a $(DR)em or som fukd up halusina$(SH)n . Its wat leds metobeliv the hol $(THING) was n fakt rel .",
        # paragraph
        "sav for a soft $(BR)ez $(TH)at oka$(ZH)naly $(SH)uk the levs of the $(TR)e nd our bre$(THING) , we sat n ded silens . it semd",
        "lik an eternity . n re$(AL)ity it was only two and a half minuts or so . fanily i manajd to$(CH)ok $(out) a few words nd",
        "$(AS)ked her to$(con)firm my $(SS)pi$(SH)ns .",
        # paragraph
        "$(Y-consonant)es $(AN)on , but $(Y-consonant)umust no$(every)$(THING) wil be$(AL)rit .",
        # paragraph
        "I began to$(con)tem$(PL)at wat todonext wen I was blindd by a $(BR)it fla$(SH) of lit . it dimd $(AF)$(TR) a fuse$(con)ds nd I",
        "relizd i was be$(ING) puld bak . Befor i wok up for the for$(TH) nd final tim . I $(AS)ked if I would",
        "$(ever) seher $(AG)an . $(TH)r was a $(BR)if paus nd $(SH)e smild litly .",
        # paragraph
        "Wen $(Y-consonant)u$(AR) ment to . $(Y-consonant)u$(AR) not $(Y-consonant)et suposd tobeher , $(AN)on .",
        # paragraph
        "nd $(TH)at waz it . I wok up n the kot gasp$(ING) for $(AR) . I mede$(AT)ly luk $(over) $(AT) the klok nd was",
        "met with for twenty on P M . on of the first $(THING)s i did was $(AS)k a nurs wen xaktly i did . for sixten P M . I was",
        "ded for just $(over) fiv minuts nd $(TH)is litl klus$(TR)fuk okurd $(over) the cours of , $(PR)esumably $(TH)is fiv minuts .",
        # paragraph
        "to$(TH)is day I havnt spokn to$(AN)yon $(AB)out it . $(TH)ey kould $(under)stand met$(ING) a ded relativ or evn god , but",
        "not a kartun hors $(TH)at by $(AL) lojik $(SH)ud not xist .",
        # paragraph
        "$(AL) I kan say for surtan is $(TH)at mybelif n a $(AF)$(TR)lif has bin re$(AF)irmd nd I hop $(Y-consonant)ufagots",
        "ton down the $(Y-consonant)uwil n$(ever) x $(TH)i$(NK)$(ING) tomy xperiens .",
    ],
]
text_combined.extend(chain.from_iterable(texts))
if __name__ == "__main__":
    for tid, text in list(enumerate(texts)):
        for lid, line in list(enumerate(text)):
            dc = DrawingContext(
                output_path=dir / f"passage-8-part-{tid + 1}-line-{lid + 1:02}.svg",
                drawing_width=1100,
                drawing_height=150,
            )
            with dc as (p, t):
                draw_sentence(t, p, line)
