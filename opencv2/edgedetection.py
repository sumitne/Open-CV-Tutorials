# edge detection , can be used in order to detect edges of a particular object
import cv2
import numpy as np
img = cv2.imread('leo.jpg', 0)    # to read it as a gray scale image
height, width = img.shape[:2]
cv2.imshow('org', img)
cv2.waitKey(0)


# laplace
img1 = cv2.Laplacian(img, cv2.CV_8U)      # (img, data type) 

cv2.imshow('laplacian', img1)
cv2.waitKey()


# canny edge uses gradient values as thresholds
canny = cv2.Canny(img, 20, 170)  # lower and upper value for threshold

cv2.imshow('canny' , canny)    # best technique
cv2.waitKey(0)
cv2.destroyAllWindows()