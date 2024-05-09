import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread("images/gausimage2.jpg",cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img,cv.CV_64F,ksize=3)#cv-64f is a 64bit negative data type which is used in these method's
lap = np.uint8(np.absolute(lap))
sobelx=cv.Sobel(img,cv.CV_64F,1,0)
sobely=cv.Sobel(img,cv.CV_64F,0,1)
canny = cv.Canny(img,100,200)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelCombined = cv.bitwise_or(sobelx,sobely)

titles=['image','Laplacian','sobelx','sobely','sobelcombined','canny']
images=[img,lap,sobelx,sobely,sobelCombined,canny]

for i in range(6):
    plt.subplot(3, 3, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 


plt.show()