import cv2
import numpy as np

cap = cv2.VideoCapture('VID2.mp4')

cv2.imshow('Frame', frame)

#res = cv2.bitwise_not(frame, frame, mask=mask)
#cv2.imshow('res', res)

cv2.destroyAllWindows()
cap.release()
