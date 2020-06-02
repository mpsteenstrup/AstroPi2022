from time import sleep
from picamera import PiCamera
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

camera = PiCamera()
camera.resolution = (1296,972)
camera.start_preview()
# Camera warm-up time
sleep(2)
print(dir_path)
camera.exif_tags['kategori'] = "egen exif information xxxxxxxxxx"
camera.capture(dir_path+'/image.jpg')
