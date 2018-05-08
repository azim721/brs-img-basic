'''
record.py : This script demonstrates how to record a video from your 
webcam or camera connected to your PC / raspberry
'''

# importing libraries
import cv2


# loading camera - 0 is camera number
cam = cv2.VideoCapture(0)

# loading encoder to encode video
fps = 30                                # frames per second
x,y = 640, 480                          # res
encoder = cv2.VideoWriter('./data/output.avi', -1, fps, (x,y))

# getting read status and frame from camera
success, frame = cam.read() 

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

    # writing frame
    encoder.write(frame)

    # trying read next frame
    success, frame = vid.read()

# closing all opened windows to display frames
cv2.destroyAllWindows() 

# closing camera
cam.release()

# closing encoder
encoder.release()