'''
ocr.py : This is a simple demonstration of how to use tesseract
to perform OCR on an image. Try loading different images of text
of your own.

In real practical applications, if the image is not ideal for OCR,
it must be preprocessed by denoising, thresholding etc. to get an 
accuracte result

Check out the documentation on image_to_string() for its different
parameters. If you installed Bengali support with tessereact, you
can change lang = 'ben' and input an image of bengali text.
'''

import pytesseract as ocr
from PIL import Image
import cv2

# a simple function to display image
def show(img, delay = 0, name = 'Image'):
  
  cv2.imshow(name, img)
  key = cv2.waitKey(delay)
  return key

img = cv2.imread('./data/text1.jpg')
show(img)

# OCR - that simple !
img = Image.fromarray(img)
txt = ocr.image_to_string(img,lang='eng')
print(txt)
