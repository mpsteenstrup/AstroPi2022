# importerer bibliotekerne Picamera og sleep
from picamera import PiCamera
from time import sleep

# åbner PiCamera som camera. På denne måde lukker det rigtigt igen når man er færdig
with PiCamera() as camera:
    for i in range(4):
        sleep(2)
        camera.capture('img%d.jpg'%i)
