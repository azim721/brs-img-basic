'''
cnn.py : This script is a demosntration of how to load trained cnn models
through openCV to recognize different objects. The model given in the data folder
has been trained on thousands of several common objects listed in CLASSES below.

You may load any video and see the results !

This is just a basic overview. We will save training your own models for a later workshop!

'''

import cv2
import numpy as np

# classes provided in our pre-trained model; get more at https://github.com/BVLC/caffe/wiki/Model-Zoo
CLASSES = ["background",   "aeroplane",     "bicycle",     "bird",    "boat",
        	"bottle",      "bus",           "car",         "cat",     "chair",
            "cow",         "diningtable",   "dog",         "horse",   "motorbike",
            "person",      "pottedplant",   "sheep",       "sofa",    "train",
            "tvmonitor" ]

# randomly assigning different color values RGB (0-255) to the different classes
COLORS = np.random.uniform(  0, 255, size=( len(CLASSES), 3 )  )


# loading trained network; you can train your own or download trained models
pathToProtoText = './data/CaffeModel/MobileNetSSD_deploy.prototxt.txt'       # model architecture
pathToModel     = './data/CaffeModel/MobileNetSSD_deploy.caffemodel'         # model weights
model = cv2.dnn.readNetFromCaffe( pathToProtoText, pathToModel )


# load image to feed to the model
vid = cv2.VideoCapture('./data/traffic.mp4')

s, img = vid.read()

while s:
    h,w,ch = img.shape

    # resizing to a smaller img (less resources required to process)
    resized = cv2.resize(img, (300,300) )

    # converting image to 'food' for network;
    blob = cv2.dnn.blobFromImage( resized, scalefactor=(1/127.5), size=(300,300), mean=127.5 )

    # putting blob into network's 'mouth'
    model.setInput(blob)

    # telling it to 'eat' and give us detected boxes
    detections = model.forward()

    # checking detections and getting extracting boxes with the highest 'confidence'
    for i in range(0, detections.shape[2] ):
        confidence = detections[ 0, 0, i, 2 ]

        if confidence > 0.70:
            class_index = detections [0, 0, i, 1]
            box_cood    = detections [0, 0, i, 3:7]     # box co-ordinates -> 3: TopLeftX , 4: TopLeftY , 5: BotRightX, 6: BotRightY

            # rescaling boxes to draw on original image
            box_cood = box_cood * np.array( [w, h, w, h] )

            x1, y1, x2, y2 = np.int16(box_cood)        # box cordinates must be integers
            class_index = int(class_index)             # index also needs to be integer

            # drawing box on oringal image
            cv2.rectangle( img, (x1,y1), (x2,y2), COLORS[class_index], 4)

            label = "%s (%2.1f %%)" % (CLASSES[class_index], confidence*100)
            cv2.putText( img, label, (x1+30, y1+30),  cv2.FONT_HERSHEY_SIMPLEX, 1, COLORS[class_index], 4  )

    img = cv2.resize(img, (w//2,h//2))
    cv2.imshow('Dectections', img)
    cv2.waitKey(20)

    s,img = vid.read()

cv2.destroyAllWindows()
