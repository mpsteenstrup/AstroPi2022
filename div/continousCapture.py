from time import sleep
from picamera import PiCamera
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous(dir_path+'/image_{counter:02}.jpg'):
    print('Captured %s' % filename)
    sleep(3) # wait 5 minutes