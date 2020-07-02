# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

image = []

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
while True:
    frame = camera.capture(rawCapture, format="bgr", use_video_port=True)
    image = frame.array
    cv2.imshow("Frame", image)
    if key == ord("q"):
        break
cv2.destroyAllWindows()
