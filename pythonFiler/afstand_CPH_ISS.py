import numpy as np
from numpy import sin, cos, arccos, sqrt, arcsin
from skyfield.api import load
from orbit import ISS

t = load.timescale().now()
issLocation = ISS.coordinates()


def distance(lat1, lon1, lat2, lon2):
    lat1 = lat1*np.pi/180
    lon1 = lon1*np.pi/180
    lat2 = lat2*np.pi/180
    lon2 = lon2*np.pi/180

#    return np.arccos(np.sin(lat1)*np.sin(lat2)+np.cos(lat1)*np.cos(lat2)*np.cos(lon1-lon2))
    return 2*arcsin(sqrt((sin((lat1-lat2)/2))**2 + cos(lat1)*cos(lat2)*(sin((lon1-lon2)/2))**2))

# Copenhagen (55.676098, 12.568337)
earthRadius = 6371
d = distance(55.676098, 12.568337,issLocation.latitude.degrees,issLocation.longitude.degrees)*earthRadius
print(f"Afstand fra København til ISS er {d:.0f} km + 400 km op")
