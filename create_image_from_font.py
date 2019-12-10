"""
"""
import os
import re
from PIL import Image, ImageDraw, ImageFont
import sys

SIZE = W, H = 28, 28
font_dir = ""
 
def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def create_number_image(number,fnt):

    tw, th = fnt.getsize(str(number))
    w = tw + 2 
    h = th + 2
    size  = w,h
    
    back_image = Image.new("RGBA", size, (255, 255, 255, 0))
    txt_image = Image.new('RGBA', size, (0, 0, 0, 255))
    draw = ImageDraw.Draw(txt_image)
    draw.text(((w - tw) / 2, (h - th) / 2), str(number), font=fnt, fill=(255, 255, 255, 255))
    img = Image.alpha_composite(back_image, txt_image)

    # Resize to WxH
    img = img.resize((W,H))
    return img

        
def make_image(idx, font_name,id):
    print (font_name.strip(".ttf"))
    fnt = ImageFont.truetype(font_dir + "/{}".format(font_name), 25)

    # 0 
    all = create_number_image(0,fnt)

    # 1-9
    for i in range(1,10):
        img = create_number_image(i,fnt)
        all = get_concat_v(all, img)

    # 0 (again)    
    img = create_number_image(0,fnt)
    all = get_concat_v(all, img)

    # To grayscale
    all = all.convert('L')
    all.save("images/" + font_name.strip(".ttf") + id + ".bmp")
        
def main():
    font_dir = sys.argv[1]
    id = sys.argv[2]        
    rp = re.compile(".*ttf")
    font_list = [fnt for fnt in os.listdir(font_dir) if rp.match(fnt)]
 
    for idx, font_name in enumerate(font_list):
        make_image(idx, font_name,id)
 
if __name__ == '__main__':
    main()
