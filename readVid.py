'''
readVid.py : This script demonstrates how to read in a video from disk

If you wish to use your webcam, you can just pass a 0 to the VideoCapture()
function insttead of a path as in line 17. You can comment out line 14 and
uncommnent line 17 to try this,

0 is the camera index number. If you have more than one camera connected to your
computer or raspberry pi, you can change it to access different cameras
'''

# importing libraries
import cv2


# loading in video 'tape'
vid = cv2.VideoCapture('./data/hashi.mp4')

# uncomment to load webcam
# vid = cv2.VideoCapture(0)

# getting read status and frame from video
success, frame = vid.read() 

# looping over the 'tape' as long as 
# able to succesfully read from it
# Will fail to read when at end of tape
while success:

    # displaying frame
    cv2.imshow('myvideo', frame)

    # adding delay(milliseconds)
    # this function waits either for the time to be over
    # or until a key is pressed on the keyboard. If latter
    # it returns the key in unicode format
    k = cv2.waitKey(33)

    # if pressed letter is q, quit
    # ord converts character to unicode
    if k == ord('q'):
        print("Exiting ...\n")
        break

    # trying read next frame
    success, frame = vid.read()

# closing all opened windows to display frames
cv2.destroyAllWindows() 

# closing video file /camera
vid.release()