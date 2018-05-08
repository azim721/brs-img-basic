'''
readImg.py : This script demonstrates how read an image from disk
and display it on screen
'''

# importing libraries
import cv2

# reading img
img = cv2.imread('./data/chobi.jpg')

# displaying image, first param is name of window
cv2.imshow('Ekti Chobi', img)

# adding a wait command to make the picture stay until any key is pressed
# the parameter passed is delay in milliseconds; 0 implies infinite delay
cv2.waitKey(0)

# closing window
cv2.destroyAllWindows()

