import cv2
# how to write an image
img = cv2.imread('leo.jpg')
cv2.imwrite('new.jpg',img)   # here we are making a clone of the original image
cv2.imwrite('new1.png',img)  # here we are cloning it and also changing the image format from jpg to png
# it will create clones in the original directory of the image.
img_1 = cv2.imread('new1.png')
cv2.imshow('output',img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
