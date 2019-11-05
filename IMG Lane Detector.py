import cv2
import numpy

# read image
src = cv2.imread('IMG5.jpg', cv2.IMREAD_UNCHANGED)
resized = cv2.resize(src, None, fx=0.2, fy=0.21) 

# apply guassian blur on src image
dst = cv2.GaussianBlur(resized,(5,5),cv2.BORDER_DEFAULT)
 
# display input and output image
cv2.imshow("Gaussian Smoothing",numpy.hstack((resized, dst)))
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image