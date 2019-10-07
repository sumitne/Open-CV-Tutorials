# how to convert an image into HSV color space
# H-Hue , S=Saturation , V-Value
# Hue is the color portion of the model, expressed as a number from 0 to 360 degrees:
#
# Red falls between 0 and 60 degrees.
# Yellow falls between 61 and 120 degrees.
# Green falls between 121-180 degrees.
# Cyan falls between 181-240 degrees.
# Blue falls between 241-300 degrees.
# Magenta falls between 301-360 degrees.

# SATURATION
# Saturation describes the amount of gray in a particular color, from 0 to 100 percent.
# Reducing this component toward zero introduces more gray and produces a faded effect.
# Sometimes, saturation appears as a range from just 0-1, where 0 is gray, and 1 is a primary color.

# VALUE (BRIGHTNESS) Value works in conjunction with saturation and describes the brightness or intensity of the color
# , from 0-100 percent, where 0 is completely black, and 100 is the brightest and reveals the most color.


# Hue:0-180 , Saturation: 0-255 , value:0-255
import cv2
img = cv2.imread('leo.jpg')
cv2.imshow('output', img)
cv2.waitKey(0)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsvoutput',img_hsv)
cv2.waitKey(0)
cv2.imshow('Huechannel',img_hsv[: , : , 0]) # extracting hue channel as it is present in 0th index
cv2.waitKey(0)
cv2.imshow('Saturatedchannel',img_hsv[: , : , 1]) # extracting saturated channel as it is present in 1st index
cv2.waitKey(0)
cv2.imshow('Valuechannel',img_hsv[: , : , 2]) # extracting value channel as it is present in 2nd index
cv2.waitKey(0)
cv2.destroyAllWindows()

