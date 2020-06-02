from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1296,972)
camera.start_preview()
i = 0

camera.exif_tags['IFD0.Artist'] = 'MP'

while i<3:
    sleep(2)
    camera.capture('image%04d.jpg' % i)
    print(camera.brightness)
    i+=1
