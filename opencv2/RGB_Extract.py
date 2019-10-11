# how to extract RGB color space from an image
import cv2
import numpy as np  # for matrix functions

img = cv2.imread('leo.jpg')
cv2.imshow('original ', img)

# we will exract RGB from our image and display the three layers as different images
cv2.waitKey(0)
B, G, R = cv2.split(img)  # splitting into BGR , in image processing the layers are actually in B G R format.
zeros = np.zeros(img.shape[:2],dtype="uint8") # creating a zero matrix of size HxW of our image using shape function
#  uint8 is a 8 bit unsigned integer,     uint8 data type can range from 0-255 exactly what we need ,RGB ranges (0-255)
print(zeros)
cv2.imshow('red',cv2.merge([zeros, zeros, R]))  # displaying red color space by merging it with zero matrix, so that
#                                                                              only red color factor get displayed
cv2.waitKey(0)
cv2.imshow('green',cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)
cv2.imshow('blue',cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()

#colud've done for all the colors
