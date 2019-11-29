import cv2 as cv
import numpy as np

fonts = [
    cv.FONT_HERSHEY_SIMPLEX,
    cv.FONT_HERSHEY_PLAIN,
    cv.FONT_HERSHEY_DUPLEX, 
    cv.FONT_HERSHEY_COMPLEX,
    cv.FONT_HERSHEY_TRIPLEX,
    cv.FONT_HERSHEY_COMPLEX_SMALL,
    cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv.FONT_HERSHEY_SCRIPT_COMPLEX,
    cv.FONT_HERSHEY_SIMPLEX | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_PLAIN | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_DUPLEX | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_COMPLEX | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_TRIPLEX | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_COMPLEX_SMALL | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_SCRIPT_SIMPLEX | cv.FONT_ITALIC,
    cv.FONT_HERSHEY_SCRIPT_COMPLEX | cv.FONT_ITALIC
];
    
def main():

    size = (1000, 1000, 3)

    img = np.zeros(size, dtype=np.uint8)

    for i in range(len(fonts)):    
        for j in range(10):
            cv.putText(img, str(j), (20+40*j,50+50*i), fonts[i], 1, (255,255,255), 2, cv.LINE_AA)

    cv.imwrite('result.png', img)
    
if __name__ == '__main__':
    main()
