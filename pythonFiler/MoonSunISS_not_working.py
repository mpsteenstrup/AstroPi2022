import ephem

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   20299.39644679  .00001347  00000-0  32240-4 0  9990"
line2 = "2 25544  51.6450  64.1844 0001663  59.0364 352.4687 15.49332070252203"

iss = ephem.readtle(name, line1, line2)
iss.compute()

sun = ephem.Sun()
sun.compute()

moon = ephem.Moon()
moon.compute()


print('ISS')
print(iss.ra, iss.dec)
print('moon')
print(moon.ra, moon.dec)
print('sun')
print(sun.ra, sun.dec)

# vinkel beregnes ved oversættelse til radian med repr
## nedenstående giver den ækvatoriale vinkel mellem solen og ISS
vinkel = float(repr(iss.ra))-float(repr(sun.ra))
print('vinkel mellem Solen og ISS er {:1.6f} radian.'.format(vinkel))
