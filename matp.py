import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images/lena.png', -1)
cv.imshow('image',img)
img = cv.cvtColor(img , cv.COLOR_RGB2HLS)  #to convert

plt.imshow(img)
plt.xticks([]),plt.yticks([]) #to hide the values at x and y coordinates
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()