# Placering af Sol, Måne og ISS
ESA har i 2021 valgt at udskifte ```ephem``` med ```skyfield```. Det nedenstående er til den gamle ```ephem```. Guide til den nye metode ligger her, [Finding the location of the ISS](https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/4).

Nedenstående program giver placeringen af ISS og Solen, samt vinklen mellem dem.
```
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

```







ISS bevæger sig rundt om Jorden med en omløbstid på 90 minutter. Dette giver mulighed for at undersøge de store dele af Jorden ISS passerer. ISS bliver også i sin bane påvirket af Solen og Månen. Banen rundt om Jorden giver på 1,5 time både nat og dag samt passage tættere eller længere fra Månen. For at kunne undersøge det skal vi kende placeringen af himmellegemerne og ISS. Vi bruger biblioteket ```ephem``` som vi brugte til at finde placeringen af ISS over jordoverfladen med programmet [getLocation.py](/pythonFiler/getLocation.py). Her kender vi ISS paceringe med længde og breddegrader i et geocentrisk koordinatsystem, som roterer med Jorden.

For at bestemme Solen og Månens placering bruger vi *Equatorial coordinate system* eller Ækvatoriale koordinatsystem. Det er også et geocentrisk koordinatsystem med centrum i Jordens centrum.

I sfæriske koordinater er det givet ved.
* Vinklen fra ækvator, Declination (Dec), med +&pi;/2 ved nordpolen og -&pi;/2 ved sydpolen, regnet i radianer.
* Vinkel langs ækvator fra højre om eller *right ascension* (Ra), fra Vernal Equinox punktet.

*Vernal Equinox* punkt (VE) er der hvor Ækvator skærer Ekliptika ved forårsjævndøgn. Altså det punkt som peger mod Solen lige over Ækvator ved forårsjævndøgn.
<p float="center">
  <img src="/materiale/billeder/ECS.png" width="250"> <img src="/materiale/billeder/Heliocentric_rectangular_ecliptic.png" width="250">
</p>


Det Ækvatoriale koordinatsystem giver ikke afstanden til himmellegemerne, men positionen, som set indefra en stjerneglobus.


Filen [MoonSunISS.py](/pythonFiler/MoonSunISS.py) giver Månen, Solen og ISS position i det ækvatoriale koordinatsysten.

```
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
```

### Opgave
* Kør programmet og overvej om de tre objekter er på samme side af Jorden.

## Er det nat på ISS?
Hvis Solen og ISS er på hver side må det være nat.

Tegningen viser vinklerne langs ækvator, &alpha; er Solen, &delta; er ISS og &gamma; er forskellen.
![Nat på ISS](/materiale/billeder/nat.png)
Hvis ISS har en større vinkel end Solen gil VE punktet vil der være nat når for den beskrevne ulighed.

### Opgave
* Vis at de skal være en absolute størrelse af &gamma;, hvis man skal tage højde for at Solens vinkel også kan være den største.

### Opgave
* Skriv om i programmet MoonSunISS.py så det giver besked når det er dag på ISS.
