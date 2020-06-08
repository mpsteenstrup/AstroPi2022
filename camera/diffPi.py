from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
import numpy as np

# define a video capture object

# camera = PiCamera()


with PiCamera() as camera:
    rawCapture = PiRGBArray(camera)    
    # giver kameraet tid til at indstille sig
    sleep(1)
    camera.capture(rawCapture, format='bgr') # bemærk at vi gemmer som blå, grøn, rød
    frame1 = rawCapture.array

    rawCapture = PiRGBArray(camera)    
    # giver kameraet tid til at indstille sig
    sleep(1)
    camera.capture(rawCapture, format='bgr') # bemærk at vi gemmer som blå, grøn, rød
    frame2 = rawCapture.array

# convert to grayscale
frame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
frame2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

# Gaussian filter,  cv2.GaussianBlur(frame1, (h, w), sigma)
frame1 = cv2.GaussianBlur(frame1, (21, 21), 10)
frame2 = cv2.GaussianBlur(frame2, (21, 21), 10)

# make the difference, in rgb
delta_frame=cv2.absdiff(frame1,frame2)

while True:
    frame=np.concatenate((frame1,frame2,delta_frame),axis=1)
    frame = cv2.resize(frame, (1160, 440))
    cv2.imshow('side by side',frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        print('done')


# Destroy all the windows
cv2.destroyAllWindows()
