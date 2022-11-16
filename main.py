print("Hello World!")
import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    cv.imshow('frame',frame)
    if not ret: break

    if cv.waitKey(0) == ord('q'): break

videoCapture.release()
cv.destroyAllWindows()