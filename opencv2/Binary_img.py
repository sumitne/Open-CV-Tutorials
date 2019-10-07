# How to convert RGB to a binary image(BlACK AND WHITE)

# binary images are those images in which the value of every pixel is either '0' or '1'
# '1' for white pixel and '0' for black pixel

import cv2
img = cv2.imread('leo.jpg', 0)  # opening as grayscale , for that less complexity occurs while working with image
#                                 colored image data is complex due to multiple layers(3D array)


cv2.imshow("output", img)
cv2.waitKey(0)

# we will use thresholding technique
# we will use range 0-120  for black and >120 for white pixels.
#  If pixel intensity is greater than the set threshold(120-130), value set to 255, else set to 0 (black).
# applying different thresholding
# techniques on the input image
# all pixels value above 120 will
# be set to 255
ret, bw = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

# ret is required because
#                        threshold function return a tuple and it will throw an error     if ret variable is not used
cv2.imshow('binary', bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
