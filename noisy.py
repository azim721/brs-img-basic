'''
noisy.py : This script demonstrates some denoising processes 
as well as an attempt at OCR using tesseract. If you dont have
tesseract, you may comment out the lines 76-78

We take a very noisy image and try to read the text hidden by
the noise
''' 

import cv2
import numpy as np
import pytesseract as ocr
from PIL import Image

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)
  return key


img = cv2.imread('./data/noisy.jpg',0)
y, x = img.shape
y, x = y//2, x//2

# making size manageable
img = cv2.resize(img, ( x , y ) )

# Fast Non Local Means Denoising Alg.
# h = filtering strength
# ws = window size
# ts = template size
# check the documentation for what these params do
h, ws, ts = 8, 21, 7
img2 = cv2.fastNlMeansDenoising(img, None, h, ws, ts)
show(img2, name = 'Denoised')

# Median Blur ; other blurs also available
img3 = cv2.medianBlur(img2,3)
show(img3, name = 'Blurred')

# Thresholding
thresVal, img4 = cv2.threshold(img3,137,255,cv2.THRESH_BINARY)
show(img3, name = 'Thresholded')

cv2.destroyAllWindows()

# Need to translate left
M = np.float32( [ [1, 0,-20],
                  [0, 1,  0]  ] )

img5 = cv2.warpAffine(img4,M,(x,y))
show(img5, name = "Translated")

# Need to Rotate by about 40 degrees CCW
M = cv2.getRotationMatrix2D( (x//2,y//2), -40, 1 )
img5 = cv2.warpAffine(img5,M,(x,y))
show(img5, name = "Rotated")

# Getting rid of spots (by eroding) & gaps (by dilating)
img5 = cv2.erode(img5,None,iterations=2)
show(img5, name = "Eroded")

img5 = cv2.dilate(img5,None,iterations=3)
show(img5, name = "Dilated")

img5 = cv2.erode(img5,None,iterations=2)
show(img5, name = "Eroded2")

img5 = cv2.dilate(img5,None,iterations=3)
show(img5, name = "Dilated2")


# OCR - that simple !
img5 = Image.fromarray(img5)
txt = ocr.image_to_string(img5,lang='eng')
print(txt)



