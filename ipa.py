import re

IPA_REPLACEMENTS = {
    "æ": "a",
    "ʌ": "a",
    "ə": "a",
    "ɑ": "o",
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
PUNCT_REPLACEMENTS = {
    ",": " ,",  # punctuation offset
    r"\.": " .",  # punctuation offset
    ";": " ;",  # punctuation offset
    r"\(": "( ",  # punctuation offset
    r"\)": " )",  # punctuation offset
    "-": " ",  # punctuation ignored
}
REPLACEMENTS = {
    **PUNCT_REPLACEMENTS,
    **IPA_REPLACEMENTS,
    r"(^|(?<=\s))ða ": "the ",
    r"(^|(?<=\s))ði ": "the ",
    " and ": " nd ",
    r"\band ": "nd ",
    # TODO: use all consonant-consonant blends automatically
    "br": "$(BR)",
    "fr": "$(FR)",
    "gr": "$(GR)",
    "pl": "$(PL)",
    "pr": "$(PR)",
    "tr": "$(TR)",
    # TODO: generate IPA to affix mapping automatically?
    # Can use a dictionary to find all words with an affix,
    # translate these words to IPA and then somehow find the IPA representation.
    "abaut": "$(about)",
    "aðar": "$(other)",
    "dis": "$(dis)",
    "evar": "$(ever)",
    "evri": "$(every)",
    "fal": "$(full)",
    "kam": "$(com)",
    "kan": "$(con)",
    "les": "$(less)",
    "mant": "$(ment)",
    "nas": "$(ness)",
    "nis": "$(ness)",
    "self": "$(self)",
    #
    r"\$\(TH\)i\$\(NG\)": "$(THING)",
    r"\$\(NG\)g": "$(NG)",
    r"\$\(NG\)k": "$(NK)",
    r"(^|(?<=\s))ak": "$(AK)",
    r"(^|(?<=\s))al": "$(AL)",
    r"ai\b": "y",
    r"(^|(?<=\s))ei ": "a ",
    r"\$\(every\)\$\(THING\)": "$(ever)i$(THING)",
    r"r\$\(TH\)": "r$(TH-left-start)",
    r"\$\(NK\)\$\(TH\)": "$(NK)$(TH-top-start)",
}


# IR for Intermediate Representation
def ipa_text_to_ir(text: str) -> str:
    for src, dst in REPLACEMENTS.items():
        text = re.sub(src, dst, text)
    return text
