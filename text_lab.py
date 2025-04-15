# %%
import re
from pathlib import Path

from draw import draw_sentence
from draw_jupyturtle import DrawingContext

dir = Path("texts/orwell-1984")
dir.mkdir(parents=True, exist_ok=True)


ipa_text = """\
ðə θɪŋ ðæt hi wʌz əˈbaʊt tu du wʌz tu ˈoʊpən ə ˈdaɪəri. ðɪs
wʌz nɑt ɪˈliɡəl (ˈnʌθɪŋ wʌz ɪˈliɡəl, sɪns ðɛr wɜr noʊ
ˈlɔŋɡər ˈɛni lɔz), bʌt ɪf dɪˈtɛktɪd ɪt wʌz ˈrizənəbli
ˈsɜrtən ðæt ɪt wʊd bi ˈpʌnɪʃt baɪ dɛθ, ɔr æt list baɪ
ˈtwɛnti-faɪv jɪrz ɪn ə fɔrst-ˈleɪˌbaʊr kæmp. ˈwɪnstən ˈfɪtɪd
ə nɪb ˈɪntu ðə ˈpɛnˌhəʊldər ænd sʌkt ɪt tu ɡɛt ðə ɡris ɔf.
ðə pɛn wʌz ən ɑrˈkeɪɪk ˈɪnstrəmənt, ˈsɛldəm juzd ˈivɪn fɔr
ˈsɪɡnəʧərz, ænd hi hæd proʊˈkjʊrd wʌn, ˈfɜrtɪvli ænd wɪð sʌm
ˈdɪfəkəlti, ˈsɪmpli bɪˈkɔz ʌv ə ˈfilɪŋ ðæt ðə ˈbjutəfəl
ˈkrimi ˈpeɪpər dɪˈzɜrvd tu bi ˈrɪtən ɑn wɪð ə riəl nɪb
ɪnˈstɛd ʌv ˈbiɪŋ skræʧt wɪð ən ɪŋk-ˈpɛnsəl. ˈækʧuəli hi wʌz
nɑt juzd tu ˈraɪtɪŋ baɪ hænd. əˈpɑrt frʌm ˈvɛri ʃɔrt noʊts,
ɪt wʌz ˈjuʒəwəl tu dɪkˈteɪt ˈɛvriˌθɪŋ ˈɪntu ði spik-raɪt wɪʧ
wʌz ʌv kɔrs ɪmˈpɑsəbəl fɔr hɪz ˈprɛzənt ˈpɜrpəs. hi dɪpt ðə
pɛn ˈɪntu ði ɪŋk ænd ðɛn ˈfɑltərd fɔr ʤʌst ə ˈsɛkənd. eɪ
ˈtrɛmər hæd ɡɔn θru hɪz ˈbaʊəlz. tu mɑrk ðə ˈpeɪpər wʌz ðə
dɪˈsaɪsɪv ækt. ɪn smɔl ˈklʌmzi ˈlɛtərz hi roʊt: ˈeɪprəl
fɔrθ, ˈnaɪnˈtin ˈeɪti fɔr.\
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
    r"\.": " .",  # punctuation offset
    ";": " ;",  # punctuation offset
    r"\(": "( ",  # punctuation offset
    r"\)": " )",  # punctuation offset
    "-": " ",  # punctuation ignored
}
replacements = {
    **punct_replacements,
    **ipa_replacements,
    r"(^|(?<=\s))ða ": "the ",
    r"(^|(?<=\s))ði ": "the ",
    " and ": " nd ",
    r"\band ": "nd ",
    #
    "fr": "$(FR)",
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
    r"\$\(TH\)i\$\(NG\)": "$(THING)",
    r"\$\(NG\)g": "$(NG)",
    r"\$\(NG\)k": "$(NK)",
    r"(^|(?<=\s))ak": "$(AK)",
    r"(^|(?<=\s))al": "$(AL)",
    r"ai\b": "y",
    r"(^|(?<=\s))ei ": "a ",
    r"\$\(every\)\$\(THING\)": "$(ever)i$(THING)",
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
