import cv2
import numpy as np

cap = cv2.VideoCapture('VID2.mp4')

while(1):
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    #sensitivity = 100
    lower_orange = np.array([5, 50, 50])
    upper_orange = np.array([15, 255, 255])
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
      area = cv2.contourArea(contour)
      
      if area > 5000:
        cv2.drawContours(frame, contours, -1, (255,0,0), 5)


    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask) 

    #res = cv2.bitwise_not(frame, frame, mask=mask)
    #cv2.imshow('res', res)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
