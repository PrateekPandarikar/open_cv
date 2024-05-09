import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread("images/lena.png",0) 
#img = np.zeros((500,500),np.uint8)
#cv.rectangle(img,(0,100),(200,200),(255),-1)
#cv.imshow("img",img)
#b,g,r=cv.split(img)
hist =cv.calcHist([img], [0],None,[256],[0,256])
plt.plot(hist)


#cv.imshow("image",img)
#cv.imshow("b",b)
#cv.imshow("g",g)
#cv.imshow("r",r)
#plt.hist(img.ravel(),256,[0,256])
#plt.hist(b.ravel(),256,[0,256])
#plt.hist(g.ravel(),256,[0,256])
#plt.hist(r.ravel(),256,[0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()