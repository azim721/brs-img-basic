'''
camScan.py : This is a demonstration of the Persective Transform 
using OpenCV; We try to emulate the function of Cam Scanner.
We read in an image of a page taken at an awkward angle, and 
apply a perspective transform to make the page
face perpendicullary to the screen.

The co-ordinates of the page corners are given below. In a
future exercise, we will detect these corners automatically
'''

import cv2
import numpy as np

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)
  return key

# image path to crappy picture
imgPath = './data/chotha.jpg'

# coordinates (x,y) of page corners
TL = [173,66]
TR = [521,256]
BL = [28,733]
BR = [481,763]

corners = [ TL, TR, BL, BR ] 

# reading in image
img = cv2.imread(imgPath)

show(img)

# Width of A4 page (approx)
W = 700

# length of A4 page root2 times width
L = int(600 * 1.5)

# final position of corners
TL2 = [0,0]
TR2 = [W,0]
BL2 = [0,L]
BR2 = [W,L]

finalPos = [ TL2, TR2, BL2, BR2 ]

# need to enter coordinate list as numpy array because
# getPerspectiveTransform() needs numpy float arrays
corners = np.float32(corners)
finalPos = np.float32(finalPos)

# getting transformation Matrix
M = cv2.getPerspectiveTransform(corners,finalPos)

# applying transform
warped = cv2.warpPerspective(img, M, (W,L)) 

show(warped)

# writing transformed image to disk
cv2.imwrite('./data/chotha2.jpg',warped)

cv2.destroyAllWindows()