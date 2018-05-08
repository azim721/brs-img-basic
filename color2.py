'''
color2.py : This is the same as color.py except it's been
modified to take a video as input.

Try using a video of your own. You can intiialize you webcam by
passing a 0 to the VideoCapture() function instead of a video path

Check the effect of cleaning the mask by uncommenting lines 28-29

Try cleaning up the mask with different kernels for dilate()
'''

import cv2
import numpy as np

#  doing the same thing to a video
vid = cv2.VideoCapture('./data/ball2.mp4')

# getting read status and frame
s, f = vid.read()

while s:
    lower = np.array([17,200,200])
    upper = np.array([117,255,255])

    mask = cv2.inRange(f,lower,upper)
        
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    # mask = cv2.dilate(mask, kernel, iterations = 2)
    
    out = cv2.bitwise_and(f,f,mask=mask)
    s,f = vid.read()
    show(out,33)

cv2.destroyAllWindows()
