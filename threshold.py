import cv2 as cv
import numpy as np


img = cv.imread('images/image.jgp.jpg',0)
_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
_,th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
_,th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
cv.imshow("image",img)
cv.imshow("img",th1)
cv.imshow("img2",th2)
cv.imshow("img3",th3)
cv.imshow("img4",th4)

cv.waitKey(0)
cv.destroyAllWindows()