import datetime
from time import sleep
import ephem
from picamera import PiCamera
from sense_hat import SenseHat
sense = SenseHat()


start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=20)

n = 0

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   20326.36850192 -.00001632  00000-0 -21475-4 0  9994"
line2 = "2 25544  51.6459 290.7198 0001511  68.3888  35.2821 15.49023220256380"
iss = ephem.readtle(name, line1, line2)



with open ("test.csv", "w") as file:
    file.write("time , latitude, longitude, billed nr  \n")

while now_time < start_time + duration:
    iss.compute()
    now_time= datetime.datetime.now()

    with open ("test.csv", "a") as file:
        file.write("%s, %s, %s, %s  \n" % (now_time, iss.sublat, iss.sublong,n))

    s = str(iss.sublat)
    s = s.split(":")
    print(s[0])

    if (int(s[0])>-60) & (int(s[0])<15):
        with PiCamera() as camera:
            camera.capture('%s.jpg'%n)
    n = n + 1
    sleep(1)
