import cv2
import numpy as np

# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture('VID2.mp4')
#'C:/Users/nnamd/Desktop/IGVC CV Stack 2020/Datasets/VID2.mp4'

# This drives the program into an infinite loop.
while(1):
    # Captures the live stream frame-by-frame
    _, frame = cap.read()
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of white color in HSV
    # change it according to your need !
    sensitivity = 100
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])

    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # The bitwise and of the frame and mask is done so
    # that only the blue coloured objects are highlighted
    # and stored in res
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # This displays the frame, mask
    # and res which we created in 3 separate windows.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
      break

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
# release the captured frame
cap.release()