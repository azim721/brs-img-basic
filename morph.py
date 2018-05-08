'''
morph.py : This is a demonstration of the different
image morphing functions and kernels available in openCV.

Try different kernels and options by changing the index of
kern[] and opt[] on lines 29 and 31
'''


import cv2
import numpy as np

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)
  return key

img = cv2.imread('./data/ko.png',0)

opt = [cv2.MORPH_CLOSE, 
       cv2.MORPH_OPEN, 
       cv2.MORPH_GRADIENT]

kern = [ cv2.MORPH_RECT, 
         cv2.MORPH_ELLIPSE, 
         cv2.MORPH_CROSS  ]

kernel = cv2.getStructuringElement(kern[0], (5,5))

img1 = cv2.morphologyEx(img, opt[2], kernel )
show(img1)