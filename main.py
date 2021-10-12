# pip install opencv-python
# pip install opencv-contrib-python
import cv2
import datetime
cap = cv2.VideoCapture(0)

    cv2.imshow('cam star', frame)
    if cv2.waitKey(10) == ord('q'):
        break