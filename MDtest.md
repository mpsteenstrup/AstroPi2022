# Hvor er ISS

ISS bruger ca 90 minutter til at komme en hel gang rundt om Jorden, ca. et fysikmodul!!!!

Som [http://www.isstracker.com/](http://www.isstracker.com/) viser bevæger ISS sig ikke over samme område hver omgang. Det er ret let at finde den nuværende placering af ISS med koden

(getLocation.py)


```
import ephem
name = "ISS (ZARYA)"

line1 = "1 25544U 98067A   19232.21018519 -.00000921  00000-0 -79298-5 0  9998"
line2 = "2 25544  51.6451  43.6489 0007283 302.9282  36.2258 15.50383510185184"

iss = ephem.readtle(name, line1, line2)
iss.compute()

print(iss.sublat, iss.sublong)
```


Python er et smukt program med rigtigt mange brugbare biblioteker og `ephem` er et af dem. Det kan beregne positionen af himmelske objekter ud fra startposition og tid. De to `linje1` og `linje2` strenge er netop ISS position og tidsdata. Det skal opdateres med de nyeste positiner her, [http://www.celestrak.com/NORAD/elements/stations.txt](http://www.celestrak.com/NORAD/elements/stations.txt).

Resultatet er 51:19:17.7 27:12:19.5 som skal oversættes til 51 19'17.7 27 12'19.5 for at google maps kan forstå det NB I får selvfølgeligt andre resultater da det er en anden dati.

[google maps koordinater](https://www.google.com/maps/place/26%C2%B018'35.6%22S+69%C2%B036'33.7%22W/@-28.4171007,-65.8302951,3z/data=!4m5!3m4!1s0x0:0x0!8m2!3d-26.3098889!4d-69.6093611)

Det kan splittes op med


```
s = str(iss.sublat)
s = s.split(":")
print(s[0])
```



### Opgave



*   Find ISS position og tjek med isstracker og google maps.
*   Skriv et program som kun tager data når ISS er på den sydlige havkugle.
*   Skriv et program som hvor I er sikre på at tage data over Afrika, men ikke vil tage for meget. ˛


# Computer vision med Astro Pi

Computer vision går ud på at lade computeren foretage valg baseret på de billeder den modtager. Der er mange forskellige måder at udvælge og behandle billeder og vil vil kun berøre en meget lille del af det. Vi vil starte med at arbejde med det kamera som vender mod jorden. Her er det muligt at tage billeder på tilfældige tidspunkter i løbet at de tre timer man har til rådighed, men det er også muligt at udvælge hvornår der skal filmes. Billederne kan groft sagt udvælges ud fra motiv eller sted, koordinater. Selv om det er muligt at vide hvor ISS er når billedet bliver taget, kan vi ikke på forhånd vide hvor den vil bevæge sig hen over i de tre timer vi har til rådighed. Nogle muligheder hvis man udvælger efter motiv er, Kystlinje, Bjergkæder, skyformationer eller måske lyserøde solnedgangsskyer. Det afhænger alt sammen af om man kan tage billeder på det helt rigtige tidspunkt.


## Jord, luft, vand og ja rumstation

Programmet, (landSeaDetection.py), er inspireret af 2019 deltageres program, hvor de målte fraktaldimensioner af skyformationer. Programmet inddeler billedet i fire dele, land, skyer, hav og rumstation. Billedet viser ISS på vej ind over Thailands kyst.

Hovedideen er at udvælge efter farve og vi bruger OpenCV biblioteket og HSV farvekoden som er forklaret her, Link til [OpenCv HSV forklaring](https://docs.opencv.org/3.4/da/d97/tutorial_threshold_inRange.html).

Her kan man lege med dem allesammen,

[http://colorizer.org/](http://colorizer.org/)


### Opgave



*   Find et billed eller to og test programmet.

Programmet er en lille smule uoverskueligt men er delt ind i funktioner til at finde de forskellige dele.

Koden nedenfor bliver brugt til at finde hav.


```
def find_sea(img):
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, (90,50,50), (125,255,255))
	output = cv2.bitwise_and(img, img, mask=mask)
	return output
```


I linje 2 bliver billedet oversat fra BGR til HSV. Fordelen ved HSV er at der nu kun er en variabel til at bestemme farven.



*   H, hue, giver farven, [0;180]
*   S, saturation, hvor mættet farven er, eller hvor meget gråt der er i, [0;255]
*   V, value, hvor lys farven er, [0;255]

`mask = cv2.inRange(hsv, (90,50,50), (125,255,255)) \
`Giver et nyt billed med hvid (255) der hvor pixelværdierne er inden for intervallet og sort, (0) ellers.


```
output = cv2.bitwise_and(img, img, mask=mask)
```


Tager det oprindelige billed `img` og viser de steder hvor `mask` er hvid.


### Opgave

Det kan være illustrativt at se mask



*   Ret i linje 16 så det bliver sort/hvid billedet af vand som I ser (I skal bruge `mask` variablen).


### Opgave

Programmet beregner procentdelen af billedet som er hhv. hav, land, skyer og rumstation. Hvis vi vil sige noget om det vi flyver over, er det måske ikke så relevant med rumstationen.



*   Lav om i `calculate_percentage` funktionen så I fjerner den del som hører til rumstationen.


## HSV og BGR

Noget om RGB og BGR

Det kan være lidt forvirrende at arbejde med HSV filtre, hvis man er vant til RGB. I programmerne, (HSVTrackbar.py) og (RGBTrackbar.py), kan I prøve med skydere. Den virker også på jeres bærbare, hvis I har installeret openCV.


### Opgave



*   Find noget med klare farver, måske den sværeste opgave.
*   Eksperimenter med skyderne, så I dedekterer objekterne hver for sig.
*   Eksperimenter med lysforholdene, kan I stadigt dedekterer objekterne?


### Opgave

Her er en lidt større opgave hvor I skal bruge jeres viden om hvordan man tager billeder og gemmer dem, sammen med detektionen.



*   Sammensæt et program som gemmer et billede når et farvet objekt kommer indenfor linsen.


## Life in space

Der er også et kamera inde i rumstationen. Her er den store udfordring at vi ikke må hente billeder ned fra rumstationen. Vi bliver derfor nødt til at udvikle metoder til at lave undersøgelser uden at kunne se dem!!!

Her er forslag til tre undersøgelser.


### Farver på ISS

Når man ser billeder indefra ISS virker det meget sort/hvidt. En af de hindringer for fremtidige rumrejser er også det psykiske miljø. Det kunne være interessant at se undersøge farverne som kameraet kan se. Det kan også være interessant at se om astronauternes tøj er farvet, her skal man så også detektere hvornår astronauterne er i billedet.


### Lysforhold på ISS

Ligesom vi er vant til at se farver er vi også vant til at lyset skifter i løbet af dagen og i overgangen fra dag til nat og tilbage igen. Variationen kan undersøges på Jorden og sammenholdes med forholdene på rumstationen. Det kan komplementeres med variation i tryk, temperatur og luftfugtighed, som vi også observerer på Jorden.


### Bevægelse på ISS

Hvor hurtigt bevæger astronauterne sig og hvor tit er de i det modul hvor AstroPi sidder? Kan man for øvrigt måle tryk-, temperatur- og accelerations-udsving når en astronaut passere? Det kan også være man kan se på orienteringen af astronauter og deres bevægelse. Til det skal vi kunne detektere bevægelse.


## Bevægelsessensor

Vi vil udvikle en algoritme som kan vise om der er bevægelse ved at se på ændringen mellem to billeder. Programmet (motinDetection.py) gør netop det. Vi bruger igen openCV til at behandle video og indlæser det i `frame `.

For at gøre billedet simplere laver vi det først om til gråtoner


```
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
For at minimere støj køre vi også billedet gennem et gaussfilter, hvor hver pixel bliver en vægtet sum at de omkringliggende. Vægtningen er som en normalfordeling eller en gaussfordeling.
frame = cv2.GaussianBlur(gray, (21, 21), 0)
```


(21, 21) angiver (sigmaX, sigmaY) altså hvor bred gaussfordelingen skal være, hvilket i runde træk svarer til at hver pixel er gennemsnit af den 21 til venstre, højre, op og ned. 0 angiver hvordan program gør i kanterne hvor der ikke er 21 pixels. Husk at billedet er (1920x1080) så gennemsnit af 21 pixels er ikke så meget.


### Opgave



*   Prøv at lav gaussfordelingen, `GaussianBlur` , om, husk at der er to steder det står.
*   Hvorfor vil man gerne have billeder som er ufokuserede og gråtonede når man skal detektere bevægelse?

mortionDetection.py


```
import numpy as np
import cv2

threshold=100

img = cv2.VideoCapture(0)
ret, frame = img.read()
height, width, nchannels = frame.shape


gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.GaussianBlur(gray, (21, 21), 0)

while(True):
	frame0 = frame
	ret, frame = img.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We apply a black & white filter
	frame = cv2.GaussianBlur(gray, (21, 21), 0) # Then we blur the picture
	if not ret:
    	    break

	# how different is it?
	if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
    	    print('change')
	else:
    	    print( 'no change' )

	# show it
	cv2.imshow('Type "q" to close',frame)

	# exit if so-commanded
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
    	    break

# When everything done, release the imgture
img.release()
print('Video exit' )
```


Programmet tager to billeder og sammenligner dem med


```
if np.sum( np.absolute(frame-frame0) )/np.size(frame) > threshold:
```


Linjen sammenligner `np.sum( np.absolute(frame-frame0) )/np.size(frame) ` som er summen af den absolutte forskel på de to billeder divideret med størrelsen af billedet, med en tærskelværdi.


### Opgave



*   Prøv programmet af og ret i tærskelværdierne indtil I synes at den detekterer ordentligt.
*   Prøv at skift `cv2.imshow` linjen ud med  `cv2.imshow('Type "q" to close',np.absolute(frame-frame0))`. Hvad ser i nu?
*   Undersøg hvordan billedet ændrer sig når I forøger sigmaX og sigmaY, I kan gå højt op hvis I vil (601 eks) .

Som I kan se i konsollen skriver den det samme mange gange. Det kan gøres smartere!!


### Opgave

I skal lave et program som tæller hvor mange gange I flytter en hånd ind foran kameraet. Det skal I gøre ved at



*   Definer en ny variabel til at tælle, eks. `count=0` og en til at holde styr på om der er sket en ændring eks. `change=True`.
*   Opdater count hvis `change=True`.
*   Prøv det af og bliv nok skuffede, den tæller sikkert for meget.

Det at den tæller for meget kan I klare, enten ved at lave et tidsinterval hvor `count` ikke opdateres eller kun opdatere den hvis den ændrer sig fra `False` til `True`.

Xx eksempelkode for c niveau elever.


### Opgave



*   Find en måde at forbedre det.
*   Overvej hvad du kan bruge det her til, hvis der er andet du vil undersøge enten i ‘life in space’ eller i ‘life on earth’.
*   Hvis du får en ide til noget du vil undersøge på ISS så hvilke eksperimenter du mener, at have brug for at gennemføre hernede på Jorden.
