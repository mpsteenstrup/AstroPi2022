import cv2
from time import sleep

# define a video capture object
vid = cv2.VideoCapture(0)

# get camera time to adjust before first picture
sleep(1)
ret1, img = vid.read()
cv2.imshow('tekst',img)
cv2.waitKey(0)

with vid as x:
    ret1, img = x.read()
    cv2.imshow('tekst',img)
    cv2.waitKey(0)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

# åbner PiCamera som camera. På denne måde #lukker det rigtigt igen når man er færdig
#with PiCamera() as camera:
#    for i in range(4):
#        sleep(2)
#        camera.capture('img%d.jpg'%i)
