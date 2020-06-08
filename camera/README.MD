# Brug af camera

Der er to kameraer på ISS, et som peger ned mod Jorden og et som peger ind i rumstationen.

## programmer
* [takePicture.py](takePicture.py), simpelt program til at gemme fire billeder
* [test_image.py](test_image.py), bruger openCV til at behandle billedet og gemme det.
* [test_video.py](test_image.py), bruger openCV til at behandle og gemme video.



## opgaver
### Fotoautomat
Vores helt egen fotoautomat, tager udgangspunkt i programmet [takePicture.py](takePicture.py). Husk at test hver gang I laver noget om, så fanger I lettere fejl.

* Ret i koden så den venter 3 sekunder mellem hvert billed.
* Brug ```print()``` til at lave en nedtælling.

## open CV
OpenCV er et bibliotek til billedgenkendelse og maskinlæring. I  [test_image.py](test_image.py) bruger vi rådata fra kameraet, ```PiRGBArray```. Det har den fordel, at vores Astro Pi ikke skal bruge ressourcer på at komprimere det til jpg og vi har alt informationen til databehandling. OpenCV bruger formatet ```bgr```, altså Blå, Grøn, Rød, hvilket er specificeret i linje 13

### opgaver
* Peg kameraet mod noget farvet og tag et billed.
* byt nu rundt på ```bgr```til den normale ```rgb```i koden.
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
Data i variablen, ```image ```ligger som ```bgr```værdier. Vi kan udvælge den røde ved
```image = image[:,:,2]```hvor ```[:,:,2]``` tager alle søjler, alle rækker, værdien på plads 2 (den røde i bgr).
* Udvælg den røde farve med, ```image = image[:,:,2]```
