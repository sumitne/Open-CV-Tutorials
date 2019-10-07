# image transpose
# used to rotate image to 90 degrees without any information loss
import cv2
img = cv2.imread('leo.jpg')
r_img = cv2.transpose(img) # returns the transpose of image given in parameters
cv2.imshow('original', img)
cv2.imshow('rotated', r_img)
cv2.waitKey(0)
cv2.destroyAllWindows()