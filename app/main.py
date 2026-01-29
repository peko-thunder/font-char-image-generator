import shutil
from datetime import datetime
from itertools import product
from pathlib import Path
from app.lib.char import load_chars
from app.lib.font import has_char
from app.lib.image import generate_font_char_image


def run():
    cleanup("images")

    font_paths = [
        "fonts/ipamjm00601/ipamjm.ttf",
        "fonts/Noto_Sans_JP/static/NotoSansJP-Light.ttf",
        "fonts/Noto_Sans_JP/static/NotoSansJP-Medium.ttf",
        "fonts/Noto_Sans_JP/static/NotoSansJP-ExtraBold.ttf",
        "fonts/Noto_Serif_JP/static/NotoSerifJP-Light.ttf",
        "fonts/Noto_Serif_JP/static/NotoSerifJP-Medium.ttf",
        "fonts/Noto_Serif_JP/static/NotoSerifJP-ExtraBold.ttf",
    ]
    chars = load_chars(
        [
            "chars/jis_x_0208_level3_kanji.txt",
            "chars/jis_x_0208_level4_kanji.txt",
        ]
    )
    logs: list[str] = []

    for font_path, char in product(font_paths, chars):
        if not has_char(font_path, char):
            logs.append(f"{font_path} has not {char}")
            continue
        generate(font_path, char)

    output_logs(logs)


def cleanup(dir: str):
    dir_path = Path(dir)
    if dir_path.exists():
        shutil.rmtree(dir_path)
    dir_path.mkdir()


def generate(font_path: str, char: str):
    font_name = Path(font_path).stem
    unicode_hex = format(ord(char), "04X")
    output_dir = Path("images") / unicode_hex
    output_dir.mkdir(parents=True, exist_ok=True)
    output = output_dir / f"{font_name}.jpg"
    generate_font_char_image(font_path, char, str(output), 50)


def output_logs(logs: list[str]):
    if logs:
        log_dir = Path("logs")
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / f"{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
        log_file.write_text("\n".join(logs), encoding="utf-8")


if __name__ == "__main__":
    run()
