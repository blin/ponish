# %%
import importlib
from pathlib import Path

import ipa
from draw import draw_sentence
from draw_jupyturtle import DrawingContext

importlib.reload(ipa)


dir = Path("texts/orwell-1984")
dir.mkdir(parents=True, exist_ok=True)


ipa_text = """\
ðə θɪŋ ðæt hi wʌz əˈbaʊt tu du wʌz tu ˈoʊpən ə ˈdaɪəri. ðɪs
wʌz nɑt ɪˈliɡəl (ˈnʌθɪŋ wʌz ɪˈliɡəl, sɪns ðɛr wɜr noʊ
ˈlɔŋɡər ˈɛni lɔz), bʌt ɪf dɪˈtɛktɪd ɪt wʌz ˈrizənəbli
ˈsɜrtən ðæt ɪt wʊd bi ˈpʌnɪʃt baɪ dɛθ, ɔr æt list baɪ
ˈtwɛnti-faɪv jɪrz ɪn ə fɔrst-ˈleɪˌbaʊr kæmp. ˈwɪnstən ˈfɪtɪd
ə nɪb ˈɪntu ðə ˈpɛnˌhoʊldər ænd sʌkt ɪt tu ɡɛt ðə ɡris ɔf.
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

ir_text = ipa.ipa_text_to_ir(ipa_text)
print(ir_text)


if __name__ == "__main__":
    for lid, line in list(enumerate(ir_text.split("\n"))):
        dc = DrawingContext(
            output_path=dir / f"ipa-{lid + 1:02}.svg",
            drawing_width=1100,
            drawing_height=150,
        )
        with dc as (p, t):
            draw_sentence(t, p, line)


dir = Path("texts/desiderata")
dir.mkdir(parents=True, exist_ok=True)


ipa_text = """\
ɡoʊ ˈplæsɪdli əˈmɪd ðə nɔɪz ænd ðə heɪst,
ænd rɪˈmɛmbər wɑt pis ðɛr meɪ bi ɪn ˈsaɪləns.
æz fɑr æz ˈpɑsəbəl, wɪˈθaʊt səˈrɛndər,
bi ɑn ɡʊd tɜrmz wɪð ɔl ˈpɜrsənz.
spik jʊər truθ ˈkwaɪətli ænd ˈklɪrli;
ænd ˈlɪsən tu ˈʌðərz,
ˈivɪn tu ðə dʌl ænd ði ˈɪɡnərənt;
ðeɪ tu hæv ðɛr ˈstɔri.
əˈvɔɪd laʊd ænd əˈɡrɛsɪv ˈpɜrsənz;
ðeɪ ɑr vɛkˈseɪʃəs tu ðə ˈspɪrət.
ɪf ju kəmˈpɛr jərˈsɛlf wɪð ˈʌðərz,
ju meɪ bɪˈkʌm veɪn ɔr ˈbɪtər,
fɔr ˈɔlˌweɪz ðɛr wɪl bi ˈɡreɪtər ænd ˈlɛsər ˈpɜrsənz ðæn jərˈsɛlf.
ɛnˈʤɔɪ jʊər əˈʧivmənts æz wɛl æz jʊər plænz.
kip ˈɪntrɪstɪd ɪn jʊər oʊn kəˈrɪr, ˌhaʊˈɛvər ˈhʌmbəl;
ɪt ɪz ə riəl pəˈzɛʃən ɪn ðə ˈʧeɪnʤɪŋ ˈfɔrʧənz ʌv taɪm.
ˈɛksərˌsaɪz ˈkɑʃən ɪn jʊər ˈbɪznəs əˈfɛrz,
fɔr ðə wɜrld ɪz fʊl ʌv ˈtrɪkəri.
bʌt lɛt ðɪs nɑt blaɪnd ju tu wɑt ˈvɜrʧu ðɛr ɪz;
ˈmɛni ˈpɜrsənz straɪv fɔr haɪ aɪˈdilz,
ænd ˈɛvriˌwɛr laɪf ɪz fʊl ʌv ˈhɛroʊˌɪzəm.
bi jərˈsɛlf. əˈspɛʃli du nɑt feɪn əˈfɛkʃən.
ˈniðər bi ˈsɪnɪkəl əˈbaʊt lʌv,
fɔr ɪn ðə feɪs ʌv ɔl erˈɪdˌəti ænd dɪsɪnˈʧæntmənt,
ɪt ɪz æz pəˈrɛniəl æz ðə ɡræs.
teɪk ˈkaɪndli ðə ˈkaʊnsəl ʌv ðə jɪrz,
ˈɡreɪsfəli səˈrɛndərɪŋ ðə θɪŋz ʌv juθ.
ˈnɜrʧər strɛŋkθ ʌv ˈspɪrət tu ʃild ju ɪn ˈsʌdən mɪsˈfɔrʧən.
bʌt du nɑt dɪˈstrɛs jərˈsɛlf wɪð dɑrk ɪˈmæʤənɪŋz.
ˈmɛni fɪrz ɑr bɔrn ʌv fəˈtiɡ ænd ˈloʊnlinəs.
bɪˈɑnd ə ˈhoʊlsəm ˈdɪsəplən,
bi ˈʤɛntəl wɪð jərˈsɛlf.
ju ɑr ə ʧaɪld ʌv ðə ˈjunəˌvɜrs
noʊ lɛs ðæn ðə triz ænd ðə stɑrz;
ju hæv ə raɪt tu bi hir.
ænd ˈwɛðər ɔr nɑt ɪt ɪz klɪr tu ju,
noʊ daʊt ðə ˈjunəˌvɜrs ɪz ənˈfoʊldɪŋ æz ɪt ʃʊd.
ˈðɛrˌfɔr bi æt pis wɪð ɡɑd,
ˌwʌˈtɛvər ju kənˈsiv hɪm tu bi.
ænd ˌwʌˈtɛvər jʊər ˈleɪbərz ænd ˌæspəˈreɪʃənz,
ɪn ðə ˈnɔɪzi kənˈfjuʒən ʌv laɪf,
kip pis ɪn jʊər soʊl.
wɪð ɔl ɪts ʃæm, ˈdrʌʤəri, ænd ˈbroʊkən drimz,
ɪt ɪz stɪl ə ˈbjutəfəl wɜrld.
bi ˈʧɪrfəl. straɪv tu bi ˈhæpi.\
"""

ir_text = ipa.ipa_text_to_ir(ipa_text)
print(ir_text)


if __name__ == "__main__":
    for lid, line in list(enumerate(ir_text.split("\n"))):
        dc = DrawingContext(
            output_path=dir / f"ipa-{lid + 1:02}.svg",
            drawing_width=1100,
            drawing_height=150,
        )
        with dc as (p, t):
            draw_sentence(t, p, line)
