"""
フォントを指定して数字の文字画像を生成する（黒背景白文字）
"""
import os
import re
from PIL import Image, ImageDraw, ImageFont
 
SIZE = W, H = 28, 28
 
 
def num_to_english(x):
    """ 数字の英語文字列を返す """
    assert 0 <= x <= 9, "Input int x (0 <= x <= 9)"
    return ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")[x]
 
 
def make_image(idx, font_name):
    """ フォントを指定して 0-9 の画像ファイルを作る """
    fnt = ImageFont.truetype("C:/Windows/Fonts/{}".format(font_name), 25)
    for i in range(10):
        back_image = Image.new("RGBA", SIZE, (255, 255, 255, 0))
        txt_image = Image.new('RGBA', SIZE, (0, 0, 0, 255))
        draw = ImageDraw.Draw(txt_image)
 
        tw, th = fnt.getsize(str(i))  # フォントを指定した時のサイズ（位置計算に使用）
        draw.text(((W - tw) / 2, (H - th) / 2), str(i), font=fnt, fill=(255, 255, 255, 255))
        file_name = "{}_{}.png".format(num_to_english(i), idx)
        out = Image.alpha_composite(back_image, txt_image)
        out.save("images/" + file_name)
 
 
def main():
    # ttfファイルのみ取得する
    rp = re.compile(".*ttf")
    font_list = [fnt for fnt in os.listdir("/System/Library/Fonts") if rp.match(fnt)]
 
    for idx, font_name in enumerate(font_list):
        make_image(idx, font_name)
 
 
if __name__ == '__main__':
    main()