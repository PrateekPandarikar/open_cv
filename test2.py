import cv2
import numpy as np

image = np.zeros((500,500,3), np.uint8)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()