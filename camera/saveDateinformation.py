# billeder i raw kvalitet, dato og tid bliver gemt på billed og som navn.

from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
from datetime import datetime
import cv2

tid=str(datetime.now())

with PiCamera() as camera:
	rawCapture = PiRGBArray(camera)
	# giver kameraet tid til at indstille sig
	sleep(1)
	camera.capture(rawCapture, format='bgr') # bemærk at vi gemmer som blå, grøn, rød
	image = rawCapture.array

cv2.putText(image,tid,(200,200),cv2.FONT_HERSHEY_SIMPLEX ,1,(255, 0, 0), 2 )
cv2.imshow("Image", image)

# viser  billedet indtil tastaturet trykkes
c = cv2.waitKey(0)

# lukker vinduer
cv2.destroyAllWindows()

# hvis man trykker s så gem billed
if (c==ord('s')):
	cv2.imwrite(tid+'.png', image)
