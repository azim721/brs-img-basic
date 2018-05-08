'''
color.py : This is a demonstration of detecting objects
of a certain color from an image, in this case a green tennis ball.

The script utilizes the inRange() function from cv2 to create
a mask for the image. Only regions with pixel values given to
inRange() are white(255) in the mask; everything else is black (0)

Check the effect of cleaning the mask by uncommenting lines 34-36

Trying cleaning up the mask with different kernels for dilate()
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
#  for object, in this case ball
lower = np.array([17,200,200])
upper = np.array([117,255,255])

# filters pixels according to threshold
mask = cv2.inRange(img,lower,upper)
show(mask, name = 'mask')

# cleaning mask - making it more circular
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
# mask = cv2.dilate(mask, kernel, iterations = 4)
# show(mask, name = 'mask')

# applying mask onto image using bitwise_and()
# you could have simply done out * mask, since 
# mask is only 2D (no channels), you would need
# stack copies of the mask for each channel of the image
# bitwise_and( ) avoids the need to do this
out = cv2.bitwise_and(img,img,mask=mask)
show(out, name  = 'filtered')
cv2.destroyAllWindows()
