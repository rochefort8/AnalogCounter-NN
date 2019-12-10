import os
import re
from PIL import Image, ImageDraw, ImageFont
import sys

def main():
    srcdir = './images/'
    dstdir = './input/'
    offset = int(sys.argv[1])
    print('Offset='+str(offset))
    
    files = os.listdir(srcdir)
    
    count=0
    for file in files:
        img = Image.open(srcdir + file)
        for i in range(10):
            c = img.crop((0,28*i + offset,28,28*i+28 + offset))
            c.save(dstdir + str(i) + "/" + str(i) + '_' + "{:03d}".format(count) + '+v' + str(offset) + ".bmp")
        count = count+1
    
if __name__ == '__main__':
    main()
