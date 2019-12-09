import os
import re
from PIL import Image, ImageDraw, ImageFont

def main():
    files = os.listdir('./fonts/')
    count=0
    for file in files:
        img = Image.open('./fonts/' + file)
        for i in range(1,10):
            offset = 1
            c = img.crop((0,28*i - offset ,28,28*i+28 - offset))
            c.save('./input/' + str(i) + "/" + str(i) + '_off_m' + str(offset) + '_' + "{:03d}".format(count) + ".bmp")
        count = count+1
    
if __name__ == '__main__':
    main()
