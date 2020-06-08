# https://levelup.gitconnected.com/build-your-own-motion-detector-using-webcam-and-opencv-in-python-ff5bdb78a55e
import cv2, pandas
from datetime import datetime
from time import sleep

first_frame=None
status_list=[None,None]
time_stamp=[]
df=pandas.DataFrame(columns=['Start','End'])

video=cv2.VideoCapture(0)
print('sleeping')
sleep(3)
print('waking')
while True:
        check,color_frame=video.read()
        status=0
        gray=cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY)
        gray=cv2.GaussianBlur(gray,(21,21),0)

        if first_frame is None:
            first_frame=gray
            continue
        delta_frame=cv2.absdiff(first_frame,gray)
        thresh_frame=cv2.threshold(delta_frame,25,255,cv2.THRESH_BINARY)[1]
        thresh_frame=cv2.dilate(thresh_frame,None,iterations=3)
        (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour)<10000:
                continue
            status=1
            (x,y,w,h)=cv2.boundingRect(contour)
            cv2.rectangle(color_frame,(x,y),(x+w,y+h),(0,0,255),2)

        status_list.append(status)

        if status_list[-1]==1 and status_list[-2]==0:
            time_stamp.append(datetime.now())
        if status_list[-1]==0 and status_list[-2]==1:
                time_stamp.append(datetime.now())

        cv2.imshow('Gray',gray)
        cv2.imshow('Delta_frame',delta_frame)
        cv2.imshow('Threshold',thresh_frame)
        cv2.imshow('color',color_frame)
        cv2.resizeWindow('image', 600,600)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print(status_list)
print(time_stamp)

for i in range(0,len(time_stamp)-2,2):
#    df=df.append({'start':i,'End':i+1},ignore_index=True)
    df=df.append({'Start':time_stamp[i],'End':time_stamp[i+1]},ignore_index=True)

df.to_csv('All_Time_Stamp.csv')

video.release()
cv2.destroyAllWindows()
