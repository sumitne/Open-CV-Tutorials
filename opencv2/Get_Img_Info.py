# how to get image info
import cv2
img = cv2.imread('leo.jpg')
cv2.imshow('output', img)
print(img.shape)  # prints the no of horizontal and vertical pixels present in image and the layers
print('Height pixel values:', img.shape[0])  # prints the no of pixels in height as it is present in 0th index
print('Width pixel values :', img.shape[1])  # prints the no of Width pixel values as it is present in 1st index
print('no of layers:', img.shape[2])  # prints the no of layers as it is present in 2nd index
cv2.waitKey(0)
cv2.destroyAllWindows()
