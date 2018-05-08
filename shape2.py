'''
shape2.py : This script does the same things as shape.py but for
frames of a video ! It is set to load a simulated video of an object
on a conveyor belt to emulate the scenario in the Industrial Automation
Scenario

Try videos of your own and the ones provided in data folder! It's not perfect.
Try to think of ways to improve the detection ! 
'''

import cv2
import numpy as np

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)

def detectShape (contour):
    shape = 'unidentified'
    perimeter = cv2.arcLength(contour, True)                          # finding length of countour
    polyApprox = cv2.approxPolyDP ( contour, 0.025*perimeter, True)   # polygonal approximation of countour

    # if 3 lines in polygon, triangle
    if( len(polyApprox) == 3):
        shape = 'triangle'
    elif( len(polyApprox) == 4):
        shape = 'rectangle'
    elif( len(polyApprox)>5):
        shape = 'circle'

    return shape, len(polyApprox)


vid = cv2.VideoCapture('./data/iacSquare.mp4')

s, img = vid.read()

while s:

    y,x,ch = img.shape

    # resized and converted to grayscale
    img2 = cv2.resize(img, (x//2,y//2))
    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # blur to smooth out
    blurred = cv2.GaussianBlur(img3, (5,5), 0)

    # threshold
    ret, thresh = cv2.threshold(blurred,60,255,cv2.THRESH_OTSU)

    thresh , cnts, hier = cv2.findContours(thresh,  cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )

    # do if contours have been found in the mage
    if len(cnts) > 0:
        cnts = [min(cnts, key=cv2.contourArea)]

        for idx,c in enumerate(cnts):
            shape, verts = detectShape(c)

            if shape =='unidentified':
                continue

            cv2.drawContours(img2, [c], -1, (0,255,0), 2)

            print ('%s (verts= %d)\n' % (shape,verts))

    # stacking thresholded view and original frame
    thresh = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
    img2 = np.hstack( (img2, thresh))
    show(img2,33)
    s, img = vid.read()

cv2.destroyAllWindows()
