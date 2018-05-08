'''
threshold.py : This script introduces some thresholding techniques.
Compare the results of the different algorithms on different images ! 
''' 

import cv2
import numpy as np

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)
  return key


# simple global thresholding
img = cv2.imread('./data/page.jpg',0)

thLevel = 200
maxVal = 255

ret, th = cv2.threshold(img, thLevel, maxVal, cv2.THRESH_BINARY)
print(ret)
show(th)

# using Otsu's Alg to decide threshold
ret, th = cv2.threshold(img, thLevel, maxVal, cv2.THRESH_OTSU)
print(ret)
show(th)

# window size must be odd
ws = 47

# using Adaptive Thresholding (Local Thesholding)
th = cv2.adaptiveThreshold(img, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, ws, 2)
print(ret)
show(th)



