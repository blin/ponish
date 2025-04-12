import argparse
from pathlib import Path
from typing import Tuple

from PIL import Image

BRAILLE_DOT_MAP = {
    (0, 0): 0x01,
    (0, 1): 0x02,
    (0, 2): 0x04,
    (0, 3): 0x40,
    (1, 0): 0x08,
    (1, 1): 0x10,
    (1, 2): 0x20,
    (1, 3): 0x80,
}
RGBPixel = Tuple[int, int, int]


def is_dark(pixel: RGBPixel, threshold: float) -> bool:
    return sum(pixel) < threshold


# Translated from
# https://github.com/TheZoraiz/ascii-image-converter/blob/d05a757c5e02ab23e97b6f6fca4e1fbeb10ab559/image_manipulation/ascii_conversions.go#L176
def image_to_braille(image_path: str | Path) -> list[str]:
    img = Image.open(image_path).convert("RGB")

    width, height = img.size

    def align(n: int, k: int):
        return ((n + k - 1) // k) * k

    target_width = align((width // 1), 2)
    target_height = align((height // 1), 4)

    if (target_width, target_height) != (width, height):
        img = img.resize((target_width, target_height))
        width, height = target_width, target_height

    threshold = (255 * 3) / 2

    lines: list[str] = []
    for y in range(0, height, 4):
        line = ""
        for x in range(0, width, 2):
            braille_code = 0x2800
            for (dx, dy), dot_value in BRAILLE_DOT_MAP.items():
                pixel_value = img.getpixel((x + dx, y + dy))
                assert isinstance(pixel_value, tuple)
                assert len(pixel_value) == 3
                if is_dark(pixel_value, threshold):
                    braille_code += dot_value
            line += chr(braille_code)
        lines.append(line)
    return lines


def chunk_braile(lines: list[str], max_line_width: int) -> list[list[str]]:
    line_length = len(lines[0])
    chunks: list[list[str]] = [list() for _ in range(1 + (line_length // max_line_width))]
    for i, chunk in enumerate(chunks):
        for line in lines:
            line_adj = line[i * max_line_width : (i + 1) * max_line_width]
            chunk.append(line_adj)
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert image to Braille art.")
    parser.add_argument("input_path", type=Path, help="Path to the input image file.")
    args = parser.parse_args()
    lines = image_to_braille(args.input_path)
    for chunk in chunk_braile(lines, 140):
        for line in chunk:
            print(line)
        print()


if __name__ == "__main__":
    main()
