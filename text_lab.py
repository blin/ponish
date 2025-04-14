# %%
import re
from pathlib import Path

from draw import draw_sentence
from draw_jupyturtle import DrawingContext

dir = Path("texts/desiderata")
dir.mkdir(parents=True, exist_ok=True)


ipa_text = """\
ɡəʊ ˈplæsɪdli əˈmɪd ðə nɔɪz ænd ðə heɪst,
ænd rɪˈmɛmbə wɒt piːs ðeə meɪ biː ɪn ˈsaɪləns.
æz fɑːr æz ˈpɒsəbᵊl, wɪˈðaʊt səˈrɛndə,
biː ɒn ɡʊd tɜːmz wɪð ɔːl ˈpɜːsᵊnz.
spiːk jɔː truːθ ˈkwaɪətli ænd ˈklɪəli;
ænd ˈlɪsᵊn tuː ˈʌðəz,
ˈiːvᵊn tuː ðə dʌl ænd ði ˈɪɡnᵊrᵊnt;
ðeɪ tuː hæv ðeə ˈstɔːri.
əˈvɔɪd laʊd ænd əˈɡrɛsɪv ˈpɜːsᵊnz;
ðeɪ ɑː vɛkˈseɪʃəs tuː ðə ˈspɪrɪt.
ɪf juː kəmˈpeə jɔːˈsɛlf wɪð ˈʌðəz,
juː meɪ bɪˈkʌm veɪn ɔː ˈbɪtə,
fɔːr ˈɔːlweɪz ðeə wɪl biː ˈɡreɪtər ænd ˈlɛsə ˈpɜːsᵊnz ðæn jɔːˈsɛlf.
ɪnˈʤɔɪ jɔːr əˈʧiːvmənts æz wɛl æz jɔː plænz.
kiːp ˈɪntrɛstɪd ɪn jɔːr əʊn kəˈrɪə, haʊˈɛvə ˈhʌmbᵊl;
ɪt ɪz ə rɪəl pəˈzɛʃᵊn ɪn ðə ˈʧeɪnʤɪŋ ˈfɔːʧuːnz ɒv taɪm.
ˈɛksəsaɪz ˈkɔːʃᵊn ɪn jɔː ˈbɪznɪs əˈfeəz,
fɔː ðə wɜːld ɪz fʊl ɒv ˈtrɪkᵊri.
bʌt lɛt ðɪs nɒt blaɪnd juː tuː wɒt ˈvɜːʧuː ðeər ɪz;
ˈmɛni ˈpɜːsᵊnz straɪv fɔː haɪ aɪˈdɪəlz,
ænd ˈɛvriweə laɪf ɪz fʊl ɒv ˈhɛrəʊɪzᵊm.
biː jɔːˈsɛlf. ɪˈspɛʃᵊli duː nɒt feɪn əˈfɛkʃᵊn.
ˈnaɪðə biː ˈsɪnɪkᵊl əˈbaʊt lʌv,
fɔːr ɪn ðə feɪs ɒv ɔːl æˈrɪdəti ænd ˌdɪsɪnˈʧɑːntmənt,
ɪt ɪz æz pəˈrɛniəl æz ðə ɡrɑːs.
teɪk ˈkaɪndli ðə ˈkaʊnsᵊl ɒv ðə jɪəz,
ˈɡreɪsfᵊli səˈrɛndərɪŋ ðə θɪŋz ɒv juːθ.
ˈnɜːʧə strɛŋθ ɒv ˈspɪrɪt tuː ʃiːld juː ɪn ˈsʌdᵊn ˌmɪsˈfɔːʧuːn.
bʌt duː nɒt dɪˈstrɛs jɔːˈsɛlf wɪð dɑːk ɪˈmæʤɪnɪŋz.
ˈmɛni fɪəz ɑː bɔːn ɒv fəˈtiːɡ ænd ˈləʊnlɪnəs.
bɪˈjɒnd ə ˈhəʊlsəm ˈdɪsəplɪn,
biː ˈʤɛntᵊl wɪð jɔːˈsɛlf.
juː ɑːr ə ʧaɪld ɒv ðə ˈjuːnɪvɜːs
nəʊ lɛs ðæn ðə triːz ænd ðə stɑːz;
juː hæv ə raɪt tuː biː hɪə.
ænd ˈwɛðər ɔː nɒt ɪt ɪz klɪə tuː juː,
nəʊ daʊt ðə ˈjuːnɪvɜːs ɪz ʌnˈfəʊldɪŋ æz ɪt ʃʊd.
ˈðeəfɔː biː æt piːs wɪð ɡɒd,
wɒtˈɛvə juː kənˈsiːv hɪm tuː biː.
ænd wɒtˈɛvə jɔː ˈleɪbəz ænd ˌæspɪˈreɪʃᵊnz,
ɪn ðə ˈnɔɪzi kənˈfjuːʒᵊn ɒv laɪf,
kiːp piːs ɪn jɔː səʊl.
wɪð ɔːl ɪts ʃæm, ˈdrʌʤᵊri, ænd ˈbrəʊkᵊn driːmz,
ɪt ɪz stɪl ə ˈbjuːtɪfᵊl wɜːld.
biː ˈʧɪəfᵊl. straɪv tuː biː ˈhæpi.\
"""

ipa_replacements = {
    "æ": "a",
    "ɑ": "a",
    "ʌ": "a",
    "ə": "a",
    "ɒ": "o",
    "ɔ": "o",
    "ɛ": "e",
    "ɜ": "e",
    "ɪ": "i",
    "ʊ": "u",
    "ɡ": "g",
    "ʒ": "$(ZH)",
    "ʤ": "$(ZH)",
    "θ": "$(TH)",
    "ŋ": "$(NG)",  # TODO: ING
    "ˈ": "",  # primary stress ignored
    "ˌ": "",  # secondary stress ignored
    "ː": "",  # length mark ignored
    "ᵊ": "",  # superscript schwa ignored
}
punct_replacements = {
    ",": " ,",  # punctuation offset
    "\\.": " .",  # punctuation offset
    ";": " ;",  # punctuation offset
}
replacements = {
    **ipa_replacements,
    **punct_replacements,
    " ða ": " the ",
    " ði ": " the ",
    " and ": " nd ",
    r"\band ": "nd ",
    #
    "tr": "$(TR)",
    "gr": "$(GR)",
    "pl": "$(PL)",
    "pr": "$(PR)",
    #
    "kam": "$(com)",
    "kan": "$(con)",
    "aða": "$(other)",
    "self": "$(self)",
    "les": "$(less)",
    "mant": "$(ment)",
    "eva": "$(ever)",
    "evri": "$(every)",
    "nis": "$(ness)",
    "nas": "$(ness)",
    "abaut": "$(about)",
    "dis": "$(dis)",
}

for src, dst in replacements.items():
    ipa_text = re.sub(src, dst, ipa_text)

if __name__ == "__main__":
    for lid, line in list(enumerate(ipa_text.split("\n"))):
        dc = DrawingContext(
            output_path=dir / f"ipa-{lid + 1:02}.svg",
            drawing_width=1100,
            drawing_height=150,
        )
        with dc as (p, t):
            draw_sentence(t, p, line)
