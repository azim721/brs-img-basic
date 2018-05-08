'''
contour.py : This is a follow upto color.py. Once we
have a mask of the reigion of interest (ROI), we need to
determine the contour of that mask to calculate the center
co-ordinates.

Since the object is a ball, we can use minEnclosingCircle() on the contour
to determine the center co-ordintes and radius of the ball in pixels

However for irregular shapes and contours (see lfr.py), we need to use moments 
to find the centroid of the contour. This is demonstrated from line 62 on wards
'''

import cv2
import numpy as np

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)


img = cv2.imread('./data/ball.jpg')
show(img)

# Min-Max Color threshold (BGR)
# for object, in this case ball
lower = np.array([17,200,200])
upper = np.array([117,255,255])

# filters pixels according to threshold
mask = cv2.inRange(img,lower,upper)

# cleaning mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
mask = cv2.dilate(mask, kernel, iterations = 4)
show(mask, name = 'mask')

# finding contour of mask
# retreival mode = external -> returns largest outer contour
# contour aprox mode = CHAIN_APPROX SIMPLE -> removes points in between st lines 
mask , cnts, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# find contours returns image, contours, and hierarchy
# we only need contours (i.e cnts) for now

# see more about retrieval mode at
# https://docs.opencv.org/3.4.0/d9/d8b/tutorial_py_contours_hierarchy.html


# getting largest contours from list of contours
c = max(cnts, key=cv2.contourArea)

# drawing contour
((x, y), r) = cv2.minEnclosingCircle(c)
x,y,r = int(x), int(y), int(r)
cv2.circle(img, (x, y), r, (0, 0, 255), 2)


# finding momemnts
M = cv2.moments(c)

# centroid of contour (x,y)
x,y = M["m10"] / M["m00"], M["m01"] / M["m00"]
x,y = int(x), int(y)
cv2.circle(img, ( x, y ), 5, (255, 0, 0), -1)

show(img)
cv2.destroyAllWindows()
