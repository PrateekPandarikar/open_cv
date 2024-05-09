import cv2
import numpy as np

img = cv2.imread('images/img.webp' , 0)

print(img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()