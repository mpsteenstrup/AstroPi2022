import numpy as np
import cv2


threshold=100

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
height, width, nchannels = frame.shape


gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.GaussianBlur(gray, (21, 21), 0)

while(True):
    frame0 = frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We apply a black & white filter
    frame = cv2.GaussianBlur(gray, (21, 21), 0) # Then we blur the picture
    if not ret:
        break

    # how different is it?
    if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
        print('change')
    else:
        print( 'no change' )

    # show it
    cv2.imshow('Type "q" to close',frame)

    # exit if so-commanded
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
print('Video exit' )
