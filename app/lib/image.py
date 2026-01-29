from PIL import Image, ImageDraw, ImageFont


def generate_font_char_image(
    font_path: str,
    char: str,
    output: str,
    image_size: int = 256,
    font_size: int | None = None,
) -> None:
    """指定されたフォントを使って文字の画像を生成する。

    Args:
        font_path: フォントファイルのパス
        char: 画像にする文字
        output: 出力画像のパス
        image_size: 画像のサイズ（ピクセル）
        font_size: フォントサイズ（Noneの場合は image_size * 0.8）
    """
    if font_size is None:
        font_size = int(image_size * 0.8)
    font = ImageFont.truetype(font_path, size=font_size)
    image = Image.new("RGB", (image_size, image_size), color="white")
    draw = ImageDraw.Draw(image)

    bbox = draw.textbbox((0, 0), char, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (image_size - text_width) / 2 - bbox[0]
    y = (image_size - text_height) / 2 - bbox[1]

    draw.text((x, y), char, font=font, fill="black")
    image.save(output)
