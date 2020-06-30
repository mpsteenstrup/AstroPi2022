= Brug af camera =

Der er to kameraer på ISS, et som peger ned mod Jorden og et som peger ind i rumstationen.

== programmer ==

Programmerne bruger biblioteket <code>PiCamera</code> og virker derfor kun på Raspberry Pi. Vi kommer gennem programmerne gennem opgaverne nedenunder. * takePicture.py, simpelt program til at gemme fire billeder * test_image.py, bruger openCV til at behandle billedet og gemme det. * [[test_image.py|test_video.py]], bruger openCV til at behandle og gemme video. * saveDateinformation.py, importer og gem dato og tidspunkt.

== opgaver ==

=== Første billeder ===

* Kør programmet, takePicture.py og åben folderen og se dine billeder.
* Kør programmet igen og tjek om den overskriver de første billeder.
* Læs kommentarerne i filen.
* Ret <code>('img%d.jpg'%i)</code> til <code>('img%04d.jpg'%i)</code>. Hvad er forskellen?
* Find ud af hvordan man laver om på opløsningen ved at kigge i dokumentaionen, [https://picamera.readthedocs.io/en/release-1.13/recipes1.html picamera].

=== Fotoautomat ===

Vores helt egen fotoautomat, tager udgangspunkt i programmet takePicture.py. Husk at test hver gang I laver noget om, så fanger I lettere fejl.

* Skriv en besked i konsollen om at billedet tages, <code>print('NU')</code>.
* Ret i koden så pausen på 2 sekunder er efter der bliver skrevet print.
* Nu er det bare at skrive pauser og tekst, så har I lavet en nedtælling.

== open CV ==

OpenCV er et bibliotek til billedgenkendelse og maskinlæring. I test_image.py bruger vi rådata fra kameraet, <code>PiRGBArray</code>. Det har den fordel, at vores Astro Pi ikke skal bruge ressourcer på at komprimere det til jpg og vi har alt informationen til databehandling. OpenCV bruger formatet <code>bgr</code>, altså Blå, Grøn, Rød, hvilket er specificeret i linje 13

=== opgaver ===

* Peg kameraet mod noget farvet og tag et billed.
* byt nu rundt på <code>bgr</code> til den normale <code>rgb</code> i koden.
* Hvad sker der med farverne på billedet?

<code>c = cv2.waitKey(0)</code> venter til en tast er trykket og <code>cv2.destroyAllWindows()</code> lukker vinduerne.

Vi gemmer billedet til sidst, hvis 's' er trykket

=== opgaver ===

* Print c.
* Print <code>ord('s')</code>

<code>ord()</code>omdanner UNICODE karakterer til tal ( nyttigt hvis man vil lave Cæsar kodning).

=== opgave - navngiv billed ===

<ul>
<li><p>Tilføj</p>
<pre>navn = input('navn:')
cv2.imwrite(navn + '.png', image)</pre>
<p>i stedet for</p>
<pre>cv2.imwrite('CVImage.png', image)</pre></li></ul>

=== opgave - vælg den røde farve ===

Data i variablen, <code>image</code> ligger som <code>bgr</code>værdier. Vi kan udvælge den røde ved <code>image = image[:,:,2]</code>hvor <code>[:,:,2]</code> tager alle søjler, alle rækker, værdien på plads 2 (den røde i bgr). * Udvælg den røde farve med, <code>image = image[:,:,2]</code>

== Slet billeder ==

Det er desværre ikke muligt at gemme billeder inde fra rumstationen. Hvis programmet skal have lov til at komme i orbit, skal det derfor slette ALLE billederne indefra rumstationen. Det er stadigt muligt at tage billeder og bruge informationen til at undesøge livet om bord, men de skal altså slettes før programmet er kørt færdigt. Denne koden sletter alle filer med endelsen <code>.jpg</code>.

getFilesWithEnding.py PAS PÅ, den sletter faktisk filerne!!!

=== opgaver - slet filerne ===

* Opret et nyt
* Opret en ny mappe, ``˛sletTest```
* Tag et par billeder i mappen eks. Med <code>raspistill -o test.jpg</code> i konsolen.
* Ret i koden så det kun er den mappes indhold som slettes.
* Udkommenter de nederste 3 linjer, #, og tjek om det er de billeder som skal slettes.
* Kør programmet hvor I sletter billederne, uhuuu.
