import cv2
import numpy as np

img = cv2.imread("images/orange2.jpg")
grey_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template =cv2.imread("images/orange2edit.jpg",0)
w,h=template.shape[::-1]

res =cv2.matchTemplate(grey_image,template,cv2.TM_CCORR_NORMED)
print(res)
threshold=0.99;#try changing this value to get mininum matching points
loc=np.where(res >= threshold)
for pt in zip(*loc[::-1]): #if there are several number of matched templates v need to iterate over them 
    cv2.rectangle(img,pt,(pt[0] + w,pt[1] + h),(0,0,255),2) #and it also will marks the space on the original image

print(loc)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()