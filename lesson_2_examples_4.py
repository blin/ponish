# %%
from pathlib import Path

from draw import draw_sentence
from draw_jupyturtle import DrawingContext

dir = Path("manual/lesson-2")
dir.mkdir(parents=True, exist_ok=True)

text = [
    "My $(AR)mor is contempt",
    "My $(SH)ild is disgust",
    "My sord is ha$(TR)ed",
]
if __name__ == "__main__":
    for i, line in list(enumerate(text)):
        dc = DrawingContext(
            output_path=dir / f"my-armor-line-{i + 1}.svg",
            drawing_width=750,
            drawing_height=150,
        )
        with dc as (p, t):
            draw_sentence(t, p, line)

text = [
    "$(TH)r is no di$(FR)ens betwen",
    "wat is rit $(AN)d wat is",
    "nesesary",
]
if __name__ == "__main__":
    for i, line in list(enumerate(text)):
        dc = DrawingContext(
            output_path=dir / f"no-difference-line-{i + 1}.svg",
            drawing_width=750,
            drawing_height=150,
        )
        with dc as (p, t):
            draw_sentence(t, p, line)
