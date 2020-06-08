import cv2
from time import sleep
import numpy as np
from datetime import datetime
tekst=str(datetime.now())

# define a video capture object
vid = cv2.VideoCapture(0)

# get camera time to adjust before first picture
sleep(1)
ret1, frame = vid.read()
## pytText(image, tekst, (x,y),font,size,(b,g,r),thickness px)
cv2.putText(frame,tekst,(200,200),cv2.FONT_HERSHEY_SIMPLEX ,1,(255, 0, 0), 2 )
cv2.imshow('tekst',frame)

cv2.waitKey(0)

cv2.imwrite(tekst+'.png',frame)
cv2.imwrite('image_'{counter:04d}'.jpg',frame)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
