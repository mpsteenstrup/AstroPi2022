# Brug af camera

Der er to kameraer på ISS, et som peger ned mod Jorden og et som peger ind i rumstationen.

## programmer
Programmerne bruger biblioteket ```PiCamera``` og virker derfor kun på Raspberry Pi. Vi kommer gennem programmerne gennem opgaverne nedenunder.
* [final/takePicture.py](takePicture.py), simpelt program til at gemme fire billeder
* [final/test_image.py](test_image.py), bruger openCV til at behandle billedet og gemme det.
* [final/test_video.py](test_image.py), bruger openCV til at behandle og gemme video.
* [final/saveDateinformation.py](saveDateinformation.py), importer og gem dato og tidspunkt.




## opgaver
### Første billeder

* Kør programmet, [takePicture.py](takePicture.py) og åben folderen og se dine billeder.
* Kør programmet igen og tjek om den overskriver de første billeder.
* Læs kommentarerne i filen.
* Ret ```('img%d.jpg'%i)``` til ```('img%04d.jpg'%i)```. Hvad er forskellen?
* Find ud af hvordan man laver om på opløsningen ved at kigge i dokumentaionen, [picamera](https://picamera.readthedocs.io/en/release-1.13/recipes1.html).


### Fotoautomat
Vores helt egen fotoautomat, tager udgangspunkt i programmet [takePicture.py](takePicture.py). Husk at test hver gang I laver noget om, så fanger I lettere fejl.


* Skriv en besked i konsollen om at billedet tages, ```print('NU')```.
* Ret i koden så pausen på 2 sekunder er efter der bliver skrevet print.
* Nu er det bare at skrive pauser og tekst, så har I lavet en nedtælling.

## open CV
OpenCV er et bibliotek til billedgenkendelse og maskinlæring. I  [test_image.py](test_image.py) bruger vi rådata fra kameraet, ```PiRGBArray```. Det har den fordel, at vores Astro Pi ikke skal bruge ressourcer på at komprimere det til jpg og vi har alt informationen til databehandling. OpenCV bruger formatet ```bgr```, altså Blå, Grøn, Rød, hvilket er specificeret i linje 13

### opgaver
* Peg kameraet mod noget farvet og tag et billed.
* byt nu rundt på ```bgr``` til den normale ```rgb``` i koden.
* Hvad sker der med farverne på billedet?

```c = cv2.waitKey(0)``` venter til en tast er trykket og ```cv2.destroyAllWindows()``` lukker vinduerne.

Vi gemmer billedet til sidst, hvis 's' er trykket

### opgaver
* Print c.
* Print ```ord('s') ```

```ord()```omdanner UNICODE karakterer til tal ( nyttigt hvis man vil lave Cæsar kodning).


### opgave - navngiv billed
* Tilføj
```
navn = input('navn:')
cv2.imwrite(navn + '.png', image)
```
i stedet for
```
cv2.imwrite('CVImage.png', image)
```


### opgave - vælg den røde farve
Data i variablen, ```image ``` ligger som ```bgr```værdier. Vi kan udvælge den røde ved
```image = image[:,:,2]```hvor ```[:,:,2]``` tager alle søjler, alle rækker, værdien på plads 2 (den røde i bgr).
* Udvælg den røde farve med, ```image = image[:,:,2]```




## Slet billeder
Det er desværre ikke muligt at gemme billeder inde fra rumstationen. Hvis programmet skal have lov til at komme i orbit, skal det derfor slette ALLE billederne indefra rumstationen. Det er stadigt muligt at tage billeder og bruge informationen til at undesøge livet om bord, men de skal altså slettes før programmet er kørt færdigt. Denne koden sletter alle filer med endelsen ```.jpg```.

[getFilesWithEnding.py](getFilesWithEnding.py)
PAS PÅ, den sletter faktisk filerne!!!

### opgaver - slet filerne
* Opret et nyt
* Opret en ny mappe, ``˛sletTest```
* Tag et par billeder i mappen eks. Med ```raspistill -o test.jpg```  i konsolen.
* Ret i koden så det kun er den mappes indhold som slettes.
* Udkommenter de nederste 3 linjer, #, og tjek om det er de billeder som skal slettes.
* Kør programmet hvor I sletter billederne, uhuuu.





# Kameraopløsning
Vi bruger billederne på [Flickr](https://www.flickr.com/photos/raspberrypi/albums/with/72157676394992328) fra tidligere missioner.

På billedet [billeder/Bankok14.39052N99.30089N.jpg] kan man rimeligt tydeligt se en ø og koordinaterne er skrevet på billedet. Vi vil prøve at finde størrelsesforholdet af vores billed. Det er ikke muligt at bruge koordinaterne direkte, men hvis man søger lidt på google maps ligner det at det godt kan være øen Mali Kyun på Thailands kyst [google maps](https://www.google.com/maps/place/14%C2%B023'25.9%22N+99%C2%B018'03.2%22E/@13.0156668,98.1246662,54528m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d14.39052!4d99.30089).

## Opgave
Vi vil nu måle afstanden i på google maps og den tilsvarende afstand i pixels på billedet. Vi skal gøre det vandret og vi ved at billedet har en opløsning på (1920x1080) pixels.
* Brug værktøjerne i google maps til finde afstanden fra spidsen af Mali Kyun til Great Western Torres islands ( en lille ø).
* Mål længden i pixels på billedet.
* Beregn lænden per pixe.
* Beregn længden af den synlige fra rumstationen.
* Giv et bud på usikkerheden.
* Vurder om det er muligt at se Emma Mærsk på 397m længde.

min løsning:
* d_Kyun_Torres = 180.63km
* Antal pixels = 851px
* Opløsning = 0.21km/px = 210m/px
* Bredden af billedet er d=1634px=>347km
* Hvis jeg har målt 10px forkert bliver intervallet [210m;215m] per px.
