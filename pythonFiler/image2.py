from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
from skimage import filters
from skimage.color import rgb2gray

with PiCamera() as camera:
	rawCapture = PiRGBArray(camera)
# giver kameraet tid til at indstille sig
	sleep(1)
	camera.capture(rawCapture, format='rgb')
	image = rawCapture.array
	image = rgb2gray(image)
#	threshold = filters.threshold_otsu(image)  # Calculate threshold
#	image_thresholded = image > threshold  # Apply threshold
#	edges = filters.sobel(image)
	blure = filters.gaussian(image, sigma=10)
plt.imshow(blure)
plt.show()
              
