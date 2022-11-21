from skyfield.api import load
import numpy as np
from numpy import sin, cos, arccos, sqrt, arcsin
from orbit import ISS

t = load.timescale().now()

eph = load('de421.bsp')
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

sunPosition = earth.at(t).observe(sun)
sra, sdec, distance = sunPosition.radec()

slon = sra.radians*180/np.pi
slat = sdec.radians*180/np.pi

location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()

Ilon = location.longitude.degrees
Ilat = location.latitude.degrees

print(f'{location.latitude.degrees:.5f}, {location.longitude.degrees:.5f}')
print(f'{slat:.5f}, {(slon-180)%360-180:.5f}')


def vinkel(lat1, lon1, lat2, lon2):
    lat1 = lat1*np.pi/180
    lon1 = lon1*np.pi/180
    lat2 = lat2*np.pi/180
    lon2 = lon2*np.pi/180

#    return np.arccos(np.sin(lat1)*np.sin(lat2)+np.cos(lat1)*np.cos(lat2)*np.cos(lon1-lon2))
    return 2*arcsin(sqrt((sin((lat1-lat2)/2))**2 + cos(lat1)*cos(lat2)*(sin((lon1-lon2)/2))**2))

v = vinkel(slat,slon,Ilat,Ilon)*180/np.pi

print(f"vinkel ISS og Solen {v:.4f} grader")
