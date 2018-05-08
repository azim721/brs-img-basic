'''
lfr.py : This is a follow up to contour.py. This script
reads in a sample video of a black track on white background.
We detect the contour of the track and calculate its center
of mass (COM). 

We can then keep track of the COM through the video and calculate
the dipslacement as the camera moves over the track. You could use
this information to actuate motors on a robot to follow the track by
always trying to keep the COM on the center of the frame.
'''

import cv2
import numpy as np

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)


vid = cv2.VideoCapture('./data/lfr.mp4')

s,f = vid.read()
h,w, _ = f.shape

# keeping track of centroid cood
x0, y0 = 0, 0

while s:

    f = cv2.resize(f, (w//2,h//2))
    # converting frame to gray scale
    fg = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    ret, th = cv2.threshold(fg, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # inverting to make track white
    th = cv2.bitwise_not(th)

    # finding contours like in color detection
    th, cnts, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # if contour found
    if len(cnts) > 0:

        # Assuming the track will be the largest contour by area
        c = max(cnts, key=cv2.contourArea)

        # finding centroid
        m = cv2.moments(c)
        x,y = m['m10']/m['m00'], m['m01']/m['m00']
        x,y = int(x), int(y)

        # drawing COM
        cv2.circle(f, (x,y), 10, (0,255,0),-1)
        
        # drawing contours
        cv2.drawContours(f,cnts,-1, (0,255,0),2 )
        
        # updating displacement
        dx = x-x0
        dy = y-y0
        x0, y0 = x,y

        cv2.putText(f, "dx = %d"%dx, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 4)

        
        # stitching original frame and analyzed frame for pretty preview
        # since th is only one channel, we need to convert to BGR to make it
        # compatiable with output for stitching
        th = cv2.cvtColor(th,cv2.COLOR_GRAY2BGR)
        output = np.hstack((th,f))
  
        show(output,33)

    s,f = vid.read()




