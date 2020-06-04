import cv2
import numpy as np
from matplotlib import pyplot as plt

import time
from picamera.array import PiRGBArray
from picamera import PiCamera

camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format='rgb')
img = rawCapture.array
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.imread('CVImage.png',0) # load as gray scale

# Computes threshold based on Otsu's method and returns binary mask image
retval, mask = cv2.threshold(img, 0, 1, cv2.THRESH_OTSU)

print("Computed Otsu threshold value = " + str(retval))

# show results
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mask,cmap = 'gray')
plt.title('Binary segmentation'), plt.xticks([]), plt.yticks([])
plt.savefig('segment.png', bbox_inches='tight', pad_inches=0.0)
plt.show()