import ephem

name = "ISS (ZARYA)"

line1 = "1 25544U 98067A   19232.21018519 -.00000921  00000-0 -79298-5 0  9998"
line2 = "2 25544  51.6451  43.6489 0007283 302.9282  36.2258 15.50383510185184"


iss = ephem.readtle(name, line1, line2)

iss.compute()

print(iss.sublat, iss.sublong)