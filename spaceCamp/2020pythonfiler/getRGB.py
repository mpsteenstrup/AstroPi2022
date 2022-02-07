# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
#import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)

rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    image = frame.array
    #print(image.shape)
    # print(image[100,100])
    r = 0
    g = 0
    b = 0
    for i in range(200,400):
        for j in range(200,400):
            r = r + image[i,j,0]
            g = g + image[i,j,1]
            b = b + image[i,j,2]
    print('rød: {:.2f}'.format(r))
    print('grøn: {:.2f}'.format(g))
    print('blå: {:.2f}'.format(b))
    #print(b/(200*200))
    # laver det om til grayscale
#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # beregner gennemsnit
#    pixAverage = np.average(image)
#    print(pixAverage)
    time.sleep(0.2)
    # show the frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    #if key == ord("q"):
    #    break