#  IMAGE TRANSLATION or DISPLACEMENT (LEFT,RIGHT,UP,DOWN)

import cv2
import numpy as np

img = cv2.imread('leo.jpg')
height, width = img.shape[:2]  # getting the height and width of image
print(height)
print(width)

quarter_h, quarter_w = height/4, width/4  # changing the x and y so tha we could observe the translation output
t = np.float32([[1, 0, quarter_w],
                [0, 1, quarter_h]])     # creating a translation matrix [1,0,tx]
#                                                                       [0,1,ty]
# we use warpaffine to shift the image coz it has linear horizontal and vertical lines
t_image = cv2.warpAffine(img, t, (width, height))
cv2.imshow('original ', img)
cv2.waitKey(0)
cv2.imshow('translated', t_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
