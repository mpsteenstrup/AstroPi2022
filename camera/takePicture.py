from picamera import PiCamera
from time import sleep

camera = PiCamera()

# tager fire billeder og navngiver dem img0.jpg osv.
#for i in range(4):
   # giv tid til at kameraet kan indstille sig
#   sleep(2)
#   camera.capture('img%d.jpg'%i)




with PiCamera() as camera:
    for i in range(4):
        sleep(2)
        camera.capture('img%d.jpg'%i)
