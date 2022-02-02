# billeder i raw kvalitet, hvor der ikke sker en kompression til jpg, det gør processen hurtigere og vi mister ikke information

from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

with PiCamera() as camera:
	rawCapture = PiRGBArray(camera)
	# giver kameraet tid til at indstille sig
	sleep(1)
	camera.capture(rawCapture, format='rgb') 
	image = rawCapture.array
	image = image[:,:,0]

print(np.mean(image))
plt.imshow(image, cmap='gray')
plt.show()
