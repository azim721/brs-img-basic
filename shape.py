'''
shape.py : This script uses the things learned about thresholding
and finding contours to detect shapes from an image

Try images of your own and the ones provided in data folder!
'''

import cv2
import numpy as np

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)

# this function takes in a contour and determines the minimum 
# number of straight line segments needed to traverse the contour's
# perimeter. Depening on the size of the shape, you may need to adjust
# the factor multiplied with perimeter. Smaller for smaller shapes
# Play around with shapes of your own!
def detectShape (contour):
    shape = 'unidentified'
    perimeter = cv2.arcLength(contour, True)                          # finding length of countour
    polyApprox = cv2.approxPolyDP ( contour, 0.1*perimeter, True)     # polygonal approximation of countour

    # if 3 lines in polygon, triangle
    if( len(polyApprox) == 3):
        shape = 'triangle'
    elif( len(polyApprox) == 4):
        shape = 'rectangle'
    elif(len(polyApprox) > 10):              # you may need to tune this to your specs
        shape = 'circle'                     # may need to decrease/increase based on size of circle

    return shape, len(polyApprox)


img = cv2.imread('./data/symbols2.jpg')
y,x,ch = img.shape

# resized and converted to grayscale
img2 = cv2.resize(img, (x//2,y//2))
img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# blur to smooth out
blurred = cv2.GaussianBlur(img3, (5,5), 0)

# threshold
ret, thresh = cv2.threshold(blurred,60,255,cv2.THRESH_OTSU)

# erode
eroded = cv2.erode(thresh,None,iterations=3)

show(eroded, name='eroded')

eroded , cnts, hier = cv2.findContours(eroded,  cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )

# assuming that desired shape is largest in the frame
cnts = sorted(cnts, key=cv2.contourArea,reverse=True)

# iterating over detected contours, starting with largest by area
for idx,c in enumerate(cnts):

    shape, verts = detectShape(c)

    if shape =='unidentified':
        continue

    print(shape)
    cv2.drawContours(img2, [c], -1, (0,255,0), 2)

    show(img2)

cv2.destroyAllWindows()
