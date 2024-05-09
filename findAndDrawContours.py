import cv2
import numpy as np

img = cv2.imread('images/image.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
contours,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours= "+str(contours))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),3) # v use -1 to draw all the conoutrs or else v can use any number in the range of no of contours

cv2.imshow('image',img)
cv2.imshow('Image gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()