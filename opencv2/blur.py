# image blurring used to create a smoothening effect in edges
import cv2
import numpy as np
img = cv2.imread("leo.jpg")
cv2.imshow('img',img)
cv2.waitKey(0)

# creating Kernel matrix 3x3
kernel_3x3 = np.ones((7, 7), np.float32)/49                  # basically a filter matrix
# we use cv2.filter2d to convolve kernel matrix with image
blurred = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('blurred', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

