import numpy as np
import cv2
import matplotlib.pyplot as plt

count = 0
new = False

threshold=100

img = cv2.VideoCapture(0)
ret, frame = img.read()
height, width, nchannels = frame.shape


gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.GaussianBlur(gray, (21, 21), 0)
myframe = plt.imshow(frame)
plt.show(block=None)
while(True):
    frame0 = frame
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We apply a black & white filter
    frame = cv2.GaussianBlur(gray, (21, 21), 0) # Then we blur the picture
    if not ret:
        break

    # how different is it?
    if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
        print('change')
        change = True
        new = not(new)
    else:
        print( 'no change' )
        change = False
    # show it
    frame=frame-frame0+100
#    plt.imshow(frame)
    myframe.set_data(frame)
    plt.draw()
#    cv2.imshow('Type "q" to close',np.absolute(frame-frame0+100))

    # exit if so-commanded
#    key = cv2.waitKey(1) & 0xFF
#    if key == ord("q"):
#        cv2.destroyAllWindows()
#        break

# When everything done, release the imgture
img.release()
print('Video exit' )
