import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('images/gausimage2.jpg')
img = cv.cvtColor(img , cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
dst = cv.filter2D(img, -1, kernel) #to get smoothend image
blur =cv.blur(img ,(5,5))# to get blur image#blur method
gblur = cv.GaussianBlur(img ,(5,5) ,0)#gaussian blur method
median = cv.medianBlur(img, 5) #medianfilter method
bfilter=cv.bilateralFilter(img, 9,75, 75) #bilateral filter

titles = ['image','2D Convolution','blur','gblur','median','bfilter']
images = [img , dst , blur,gblur,median,bfilter]

for i in range(6):
    plt.subplot(3, 3, i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([]) 

plt.show()