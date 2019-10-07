# image resizing or scaling and interpolation
import cv2

img = cv2.imread('leo.jpg')
cv2.imshow('original', img)

cv2.waitKey(0)
# will use cv2.resize function
img_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)  # linear interpolation , converting to 3/4 of the original size
img_scaled1 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)  # doubling using cubic interpolation
img_scaled2 = cv2.resize(img, (700, 500,), interpolation=cv2.INTER_AREA)  # resizing according to our choice
cv2.imshow("Linear interpolation", img_scaled)
cv2.waitKey(0)
cv2.imshow("cubic interpolation", img_scaled1)
cv2.waitKey(0)
cv2.imshow('area interpolation', img_scaled2)
cv2.waitKey(0)

cv2.destroyAllWindows()
