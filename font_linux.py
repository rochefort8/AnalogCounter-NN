"""
"""
import os
import re
from PIL import Image, ImageDraw, ImageFont
 
SIZE = W, H = 28, 28
 
def num_to_english(x):
    assert 0 <= x <= 9, "Input int x (0 <= x <= 9)"
    return ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")[x]
 

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def calculate_height(fnt):
    h = 0
    for i in range(0,10):
        tw, th = fnt.getsize(str(i))
        if h < th:
            h = th
    if H < h:
        h += 5
    else:
        h = H
    return h

def create_number_image(number,fnt,w,h):
    size  = w,h 
    back_image = Image.new("RGBA", size, (255, 255, 255, 0))
    txt_image = Image.new('RGBA', size, (0, 0, 0, 255))
    draw = ImageDraw.Draw(txt_image)
    tw, th = fnt.getsize(str(number))
    draw.text(((w - tw) / 2, (h - th) / 2), str(number), font=fnt, fill=(255, 255, 255, 255))
    img = Image.alpha_composite(back_image, txt_image)
    img = img.resize((W,H))
    return img
        
def make_image(idx, font_name):
    print (font_name.strip(".ttf"))
    fnt = ImageFont.truetype("./f/{}".format(font_name), 25)

    h = calculate_height(fnt)
    if H < h:
        return
    print("Height=" + str(h))
    all = create_number_image(0,fnt,W,h)
    for i in range(1,10):
        img = create_number_image(i,fnt,W,h)
        all = get_concat_v(all, img)
    img = create_number_image(0,fnt,W,h)
    all = get_concat_v(all, img)
    all = all.convert('L')
    all.save("fonts/" + font_name.strip(".ttf") + ".bmp")
    
        
def main():
    rp = re.compile(".*ttf")
    font_list = [fnt for fnt in os.listdir("./f") if rp.match(fnt)]
 
    for idx, font_name in enumerate(font_list):
        make_image(idx, font_name)
 
if __name__ == '__main__':
    main()
