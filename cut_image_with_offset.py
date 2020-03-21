import os
import re
from PIL import Image, ImageDraw, ImageFont
import sys

SIZE = W, H = 28,28

def main():
    srcdir = './images/'
    dstdir = './base/'
    offset_ratio = float(sys.argv[1])
    print('Offset Ratio='+str(offset_ratio))
    
    files = os.listdir(srcdir)
    count=0

    for file in files:
        src_img = Image.open(srcdir + file)

        w,h = src_img.size
        if h != w * 11:
            print("Height must be x11 of width.")
            continue
        delta = w / 2     
        offset = int(offset_ratio * w)
#        print(offset)
    
        for i in range(20):
#            print((0, delta*i+ offset, w, delta*i + w + offset))
                
            img = src_img.crop((0, delta*i+ offset, w, delta*i + w + offset))
            category = "{:02d}".format(i)    
                # Resize to WxH
            img = img.resize((W,H),Image.LANCZOS)
            img.save(dstdir + category + "/" + category + '_' + "{:03d}".format(count) + '+v' + str(offset) + ".bmp")
        count = count+1
    
if __name__ == '__main__':
    main()
