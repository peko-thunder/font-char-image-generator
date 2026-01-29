from pathlib import Path

from app.lib.char import load_chars
from app.lib.image import generate_font_char_image


def run():
    chars = load_chars(
        [
            "chars/jis_x_0208_level3_kanji.txt",
            "chars/jis_x_0208_level4_kanji.txt",
        ]
    )
    font_paths = ["fonts/ipamjm00601/ipamjm.ttf"]

    for font_path in font_paths:
        font_name = Path(font_path).parent.name
        for char in chars:
            unicode_hex = format(ord(char), "04X")
            output_dir = Path("images") / unicode_hex
            output_dir.mkdir(parents=True, exist_ok=True)
            output = output_dir / f"{font_name}.jpg"
            generate_font_char_image(font_path, char, str(output), 50)


if __name__ == "__main__":
    run()
