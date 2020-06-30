# billeder i raw kvalitet, hvor der ikke sker en kompression til jpg, det gør processen hurtigere og vi mister ikke information

from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2


with PiCamera() as camera:
	camera.resolution = (1296,972)
	rawCapture = PiRGBArray(camera)
	# giver kameraet tid til at indstille sig
	sleep(1)
	camera.capture(rawCapture, format='bgr') # bemærk at vi gemmer som blå, grøn, rød
	image = rawCapture.array

cv2.imshow("Image", image)

# viser billedet indtil tastaturet trykkes
c = cv2.waitKey(0)

# lukker vinduer
cv2.destroyAllWindows()

# hvis man trykker s så gem billed
if (c==ord('s')):
	cv2.imwrite('CVImage.png', image)
