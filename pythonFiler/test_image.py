# billeder i raw kvalitet, hvor der ikke sker en kompression til jpg, det gør processen hurtigere og vi mister ikke information

from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import matplotlib.pyplot as plt

with PiCamera() as camera:
#	camera.resolution = (2592,1944)
	rawCapture = PiRGBArray(camera)
	# giver kameraet tid til at indstille sig
	sleep(1)
	camera.capture(rawCapture, format='bgr') # bemærk at vi gemmer som blå, grøn, rød
	image = rawCapture.array

plt.imshow(image)
plt.show()
