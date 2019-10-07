import cv2
# how to read an image
# opencv is an image processing and a computer vision library developed by intel
img = cv2.imread('leo.jpg')  # reading the image from same directory
# #for different directory provide full path with '/' instead of \

cv2.imshow('output', img)  # function to display the image
# it has two params one for name of output frame and another is image variavble

cv2.waitKey(0)  # this function make the ouptut get closed after any key is pressed
cv2.destroyAllWindows()  # this function destroys all windows after complete execution.
