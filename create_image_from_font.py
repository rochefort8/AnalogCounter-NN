
import os
import re
from PIL import Image, ImageDraw, ImageFont
import sys
import numpy

SIZE = W, H = 100, 100
FONT_SIZE = 100
 
def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def create_number_image(number,font):

    _number = str(number)

    # Font size
    font_size   = numpy.array(font.getsize(_number))
    font_offset = numpy.array(font.getoffset(_number))
    font_width, font_height = font_size - font_offset 
#    print(font_width,font_height)

    # Background image size
    image_height = int(font_height * 1.2)
    image_width  = image_height
    image_size   = numpy.array((image_width,image_height))
#    print(image_width,image_height)
 
    img = Image.new("RGB", image_size.tolist(),(0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw text at center
    draw.text((image_size - font_size - font_offset)/2,
            _number, font=font, fill=(255,255,255))

    # Resize to WxH
    img = img.resize((W,H),Image.LANCZOS)
#    img = img.resize((W,H),Image.BICUBIC)
    return img
        
def make_image(font_name,id):
    print (font_name.strip(".ttf"))

    font = ImageFont.truetype("/{}".format(font_name), FONT_SIZE)

    # 0 
    all = create_number_image(0,font)

    # 1-9
    for i in range(1,10):
        img = create_number_image(i,font)
        all = get_concat_v(all, img)

    # 0 (again)    
    img = create_number_image(0,font)
    all = get_concat_v(all, img)

    # To grayscale
    all = all.convert('L')
    all.save("images/" + font_name.strip(".ttf") + id + ".bmp")
        
def create_image_from_fontfile(dir,id) :
    rp = re.compile(".*ttf")
    fonts= [font for font in os.listdir(dir) if rp.match(font)]
    for index, font_name in enumerate(fonts):
        make_image(font_name,id)

def main():
    dir = sys.argv[1]
    id  = sys.argv[2]        
    create_image_from_fontfile(dir,id)
    
 
if __name__ == '__main__':
    main()
