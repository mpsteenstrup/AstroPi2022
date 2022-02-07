import ephem
from time import sleep
from picamera import PiCamera

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   20326.36850192 -.00001632  00000-0 -21475-4 0  9994"
line2 = "2 25544  51.6459 290.7198 0001511  68.3888  35.2821 15.49023220256380"
iss = ephem.readtle(name, line1, line2)
iss.compute()

s = str(iss.sublat)
s = s.split(":")
print(s[0])

if (int(s[0])>-60) & (int(s[0])<0):
    with PiCamera() as camera:
        camera.capture('lat%s.jpg'%s[0])
