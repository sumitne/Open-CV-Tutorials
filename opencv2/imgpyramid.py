# image pyramid
# image resizing using image pyramid
import cv2
img = cv2.imread('leo.jpg')
smaller = cv2.pyrDown(img)  # making smaller size image without knowing its dimensions (half)
larger = cv2.pyrUp(img)   # larger image (double)

cv2.imshow('original', img)
cv2.imshow('smaller', smaller)
cv2.imshow('larger', larger)
cv2.waitKey(0)
cv2.destroyAllWindows()