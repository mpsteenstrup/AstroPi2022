import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

rval, frame = vc.read()

while True:

  if frame is not None:   
     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     Gaussian = cv2.GaussianBlur(frame, (21,21),0)
     cv2.imshow("preview", grayFrame)
     cv2.imshow("Gaus", Gaussian)
  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break
