# image arithmetic's
# adding another array to image pixels to change the behaviour and properties of pixels

import cv2
import numpy as np
img = cv2.imread('leo.jpg')
cv2.imshow('original', img)
cv2.waitKey(0)
M = np.ones(img.shape, dtype="uint8")*150  # creating ones array exactly as size of the image then multipling with 150
added = cv2.add(img, M)
cv2.imshow('added', added)
cv2.waitKey(0)
subtracted = cv2.subtract(img, M)
cv2.imshow('subtracted', subtracted)
cv2.waitKey(0)
mult = cv2.multiply(img, M)
cv2.imshow('multiplied', mult)
cv2.waitKey(0)
cv2.destroyAllWindows()



