import cv2 as cv
import numpy as np

fonts = [
    cv.FONT_HERSHEY_COMPLEX | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_TRIPLEX | cv.FONT_ITALIC, 
    cv.FONT_HERSHEY_SCRIPT_COMPLEX | cv.FONT_ITALIC,
    cv.FONT_HERSHEY_COMPLEX,
    cv.FONT_HERSHEY_SIMPLEX,
#    cv.FONT_HERSHEY_PLAIN,
    cv.FONT_HERSHEY_DUPLEX, 
    cv.FONT_HERSHEY_TRIPLEX,
#    cv.FONT_HERSHEY_COMPLEX_SMALL,
    cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv.FONT_HERSHEY_SCRIPT_COMPLEX,
];
    
def main():

    size = (40, 30, 3)

    for i in range(len(fonts)):    
        for j in range(10):
            for k in range(2):
                img = np.zeros(size, dtype=np.uint8)

                cv.putText(img, str(j), (2, 32), fonts[i], 1.2, (255,255,255),k+1, cv.LINE_8)
                cv.imwrite(str(j) + '_f' +str(i) + '_'+ str(k) + '_0' + '.bmp',img)
                cv.putText(img, str(j), (20+40*j,100+300*i+100*k), fonts[i], 1.2, (255,255,255),k+1, cv.LINE_AA)
                cv.imwrite(str(j) + '_f' +str(i) + '_'+ str(k) + '_1' + '.bmp',img)

    cv.imwrite('result.png', img)
    
if __name__ == '__main__':
    main()
