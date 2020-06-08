from picamera import PiCamera
from time import sleep

# åbner PiCamera som camera. På denne måde lukker det rigtigt igen når man er færdig
with PiCamera() as camera:
    for i in range(4):
        print(3)
        sleep(1)
        print(2)
        sleep(1)
        print(1)
        sleep(1)
        print('GO')
        img = camera.capture('img%d.jpg'%i)
        cv2.imshow("Image", img)
