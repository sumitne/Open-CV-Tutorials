# how to rotate an image

import cv2
import numpy as np
img = cv2.imread('leo.jpg')
height , width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((height/2,width/2),70,0.5)  # to ger a rotation matrix (center,angle,scaling factor)
r_img = cv2.warpAffine(img,rotation_matrix,(height,width))
cv2.imshow('original',img)
cv2.imshow('rotated',r_img)
cv2.waitKey(0)
cv2.destroyAllWindows()