# image cropping
import cv2
img = cv2.imread('leo.jpg')
cv2.imshow('original', img)
cv2.waitKey(0)
height, width = img.shape[:2]
# lets get the starting rows and columns of cropeed image (top left)
start_row, start_column = int(height*.25), int(width*.25)

# lets get the end rows and columns of cropped image(bottom right)
end_row, end_column = int(height*.75), int(width*.75)

# creating the cropped image using new rows and columns
cropped = img[start_row:end_row, start_column:end_column]

cv2.imshow('cropped', cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()