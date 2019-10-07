# to open web cam
import cv2
cap = cv2.VideoCapture(0)

while True:   # infinite loop as webcam require infite amount of shots
    ret, frame = cap.read()
    cv2.imshow('live sketch', frame)
    if cv2.waitKey(1)==13:   # 13 is ASCII of Enter key
        break
cap.release()
cv2.destroyAllWindows()