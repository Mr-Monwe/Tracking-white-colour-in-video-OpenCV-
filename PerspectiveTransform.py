import cv2
import numpy as np 
#'C:/Users/WSURobotics/Desktop/ADS Vision/VID3.avi'
cap = cv2.VideoCapture('C:/Users/WSURobotics/Desktop/ADS Vision/VID3.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
     
    # Calibration points. 
    # Draw four circles on the frame, pass the xy of each circle, the size of the pixel, then the color, then the thickness -1 for fill.  
    cv2.circle(frame, (365, 200), 5, (0, 0, 255), -1) #Red
    cv2.circle(frame, (900, 200), 5, (0, 255, 0), -1) #Green
    cv2.circle(frame, (5, 705), 5, (255, 0, 0), -1) #Blue
    cv2.circle(frame, (1275, 705), 5, (0, 255, 255), -1) #Yellow

    # Put the four calibrated points into an array
    pts1 = np.float32 ([[365, 200], [900, 200], [5, 705], [1275, 705]])
    pts2 = np.float32 ([[0, 0], [1280, 0], [0, 720], [1280, 720]])

     # Remember to move the transform out of the frame so as to not keep recomputing it. 
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    result = cv2.warpPerspective(frame, matrix, (1280, 720))

    blur = cv2.GaussianBlur(result,(5,5),cv2.BORDER_DEFAULT)

        # Converts images from BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # define range of white color in HSV
    # change it according to your need !
    sensitivity = 100
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])

    # Here we are defining range of whitecolor in HSV
    # This creates a mask of white coloured
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # The bitwise and of the frame and mask is done so
    # that only the white coloured objects are highlighted
    # and stored in res
    cv2.imshow('frame', blur)
    cv2.imshow('mask', mask)

    # Show the original frame
    cv2.imshow("Frame", frame)
    # Show the output with perspective transform. 
    #cv2.imshow("Perspective transformation", result)    

    key = cv2.waitKey(1)
    if key == 27:
      break
    
cap.release()
cv2.destroyAllWindows()