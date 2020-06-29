import numpy as np
import cv2

interval = 100
fps = 1000./interval
camnum = 0
outfilename = 'temp.avi'

threshold=100.

cap = cv2.VideoCapture(camnum)

ret, frame = cap.read()
height, width, nchannels = frame.shape

#fourcc = cv2.VideoWriter_fourcc(*'MJPG')
#out = cv2.VideoWriter( outfilename,fourcc, fps, (width,height))


while(True):

    # previous frame
    frame0 = frame
    # new frame
    ret, frame = cap.read()
    if not ret:
        break

    frame0 = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    frame0 = cv2.GaussianBlur(frame0, (21, 21), 0)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (21, 21), 0)


    # how different is it?
    if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
#        out.write( frame )
        print('change')
    else:
        print( 'no change' )

    # show it
    cv2.imshow('Type "q" to close',frame)

    # check for keystroke
    key = cv2.waitKey(interval) & 0xFF

    # exit if so-commanded
    if key == ord('q'):
        print('received key q' )
        break

# When everything done, release the capture
cap.release()
#out.release()
print('VideoDemo - exit' )
