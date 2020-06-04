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


#img = cv2.imread('CVImage.png',0) # load as gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200)

# show results
plt.figure(1)
plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.figure(2)
plt.imshow(edges,cmap = 'gray'), plt.xticks([]), plt.yticks([])
plt.savefig('edges.png', bbox_inches='tight', pad_inches=0.0)

plt.show()
