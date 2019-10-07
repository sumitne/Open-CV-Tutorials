# how to convert RGB into a gray scale image
import cv2
img = cv2.imread('leo.jpg')
cv2.imshow('output', img)


cv2.waitKey(0)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # this is the 1st method through which we can convert  rbg to gray scale image
#  2nd method is to just pass an argument 0 when reading the image eg: cv2.imshow('leo.jpg',0)


cv2.imshow("grayoutput", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
