import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('CVImage.png',0) # load as gray scale
edges = cv2.Canny(img,100,200)

# show results
plt.figure(1)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.figure(2)
plt.imshow(edges,cmap = 'gray'), plt.xticks([]), plt.yticks([])
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.savefig('edges.png', bbox_inches='tight', pad_inches=0.0)

plt.show()
