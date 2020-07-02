from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

image0 = []
image1 = []

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

"""
interval = 100
fps = 1000./interval
camnum = 0
outfilename = 'temp.avi'

threshold=100.

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
height, width, nchannels = frame.shape


gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.GaussianBlur(gray, (21, 21), 0)

while(True):
    frame0 = frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We apply a black & white filter
    frame = cv2.GaussianBlur(gray, (21, 21), 0) # Then we blur the picture
    if not ret:
        break

    # how different is it?
    if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
        print('change')
    else:
        print( 'no change' )

    # show it
    cv2.imshow('Type "q" to close',frame)

    # check for keystroke
    key = cv2.waitKey(interval) & 0xFF

    # exit if so-commanded
    if key == ord('q'):
        print('received key q' )
        break

# When everything done, release the capture
cap.release()
#out.release()
print('VideoDemo - exit' )

"""
