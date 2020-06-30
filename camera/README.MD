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
