# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from matplotlib import pyplot as plt

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.iso = 200
time.sleep(2)
camera.shutter_speed = camera.exposure_speed
camera.shutter_speed = 20000
camera.exposure_compensation = 1
camera.awb_gains = (1,1)
camera.exposure_mode = 'off'
camera.awb_mode = 'off'

rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    image = frame.array
    # laver det om til grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # beregner gennemsnit
    pixAverage = np.average(gray)
    print(pixAverage)
#    show the frame
    plt.imshow(gray)
    plt.pause(0.2)
    rawCapture.truncate(0)
plt.show()
