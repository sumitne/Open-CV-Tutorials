import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_range = np.array([110, 50, 50])  # hsv values for blue
    upper_range = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    result1 = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result1)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()