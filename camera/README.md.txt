+ Brug af camera
Der er to kameraer på ISS, et som peger ned mod Jorden og et som peger ind i rumstationen.

Billeder fra rumstationen på [https://www.flickr.com/photos/raspberrypi/albums Flickr, ]


God beskrivelse på [https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/4 AstroPi-pictures]
Camera documentation, [https://www.raspberrypi.org/documentation/hardware/camera/ Camera dokumentation]

++ programmer

Programmerne bruger biblioteket {{PiCamera}} og virker derfor kun på Raspberry Pi. Vi kommer gennem programmerne gennem opgaverne nedenunder.

[[ul]]
[[li]][[http://iftek.dk/local--files/astropi:kamera/takePicture.py takePicture.py]], simpelt program til at gemme fire billeder
[[/li]][[li]]
[[http://iftek.dk/local--files/astropi:kamera/test_image.py test_image.py ]], bruger openCV til at behandle billedet og gemme det.
[[/li]][[li]]
[[http://iftek.dk/local--files/astropi:kamera/test_image.py test_video.py ]], bruger openCV til at behandle og gemme video.
[[/li]][[li]]
[[http://iftek.dk/local--files/astropi:kamera/saveDateinformation.py saveDateinformation.py]], importer og gem dato og tidspunkt.
[[/li]]
[[/ul]]

++ opgaver

+++ Første billeder


[[ul]]
[[li]]
Kør programmet, [takePicture.py takePicture.py ] og åben folderen og se dine billeder.
[[/li]][[li]]
Kør programmet igen og tjek om den overskriver de første billeder.
[[/li]][[li]]
Læs kommentarerne i filen.
[[/li]][[li]]
Ret {{('img%d.jpg'%i)}} til {{('img%04d.jpg'%i)}}. Hvad er forskellen?
[[/li]][[li]]
Find ud af hvordan man laver om på opløsningen ved at kigge i dokumentaionen, [https://picamera.readthedocs.io/en/release-1.13/recipes1.html picamera ].
[[/li]]
[[/ul]]
+++ Fotoautomat


Vores helt egen fotoautomat, tager udgangspunkt i programmet [takePicture.py takePicture.py ]. Husk at test hver gang I laver noget om, så fanger I lettere fejl.

[[ul]]
[[li]]
Skriv en besked i konsollen om at billedet tages, {{print('NU')}}.
[[/li]][[li]]
Ret i koden så pausen på 2 sekunder er efter der bliver skrevet print.
[[/li]][[li]]
Nu er det bare at skrive pauser og tekst, så har I lavet en nedtælling.
[[/li]]
[[/ul]]
++ open CV

OpenCV er et bibliotek til billedgenkendelse og maskinlæring. I  [test_image.py test_image.py ] bruger vi rådata fra kameraet, {{PiRGBArray}}. Det har den fordel, at vores Astro Pi ikke skal bruge ressourcer på at komprimere det til jpg og vi har alt informationen til databehandling. OpenCV bruger formatet {{bgr}}, altså Blå, Grøn, Rød, hvilket er specificeret i linje 13

+++ opgaver


[[ul]]
[[li]]
Peg kameraet mod noget farvet og tag et billed.
[[/li]][[li]]
byt nu rundt på {{bgr}} til den normale {{rgb}} i koden.
[[/li]][[li]]
Hvad sker der med farverne på billedet?
[[/li]]
[[/ul]]

{{c = cv2.waitKey(0)}} venter til en tast er trykket og {{cv2.destroyAllWindows()}} lukker vinduerne.

Vi gemmer billedet til sidst, hvis 's' er trykket

+++ opgaver


[[ul]]
[[li]]
Print c.
[[/li]][[li]]
Print {{ord('s')}}
[[/li]]
[[/ul]]

{{ord()}}omdanner UNICODE karakterer til tal ( nyttigt hvis man vil lave Cæsar kodning).

+++ opgave - navngiv billed


[[ul]]
[[li]]
Tilføj
[[/li]]
[[/ul]]

[[code]]
navn = input('navn:')
cv2.imwrite(navn + '.png', image)

[[/code]]

i stedet for

[[code]]
cv2.imwrite('CVImage.png', image)

[[/code]]

+++ opgave - vælg den røde farve


Data i variablen, {{image}} ligger som {{bgr}}værdier. Vi kan udvælge den røde ved
{{image = image[:,:,2]}}hvor {{[:,:,2]}} tager alle søjler, alle rækker, værdien på plads 2 (den røde i bgr).

[[ul]]
[[li]]
Udvælg den røde farve med, {{image = image[:,:,2]}}
[[/li]]
[[/ul]]

++ Slet billeder

Det er desværre ikke muligt at gemme billeder inde fra rumstationen. Hvis programmet skal have lov til at komme i orbit, skal det derfor slette ALLE billederne indefra rumstationen. Det er stadigt muligt at tage billeder og bruge informationen til at undesøge livet om bord, men de skal altså slettes før programmet er kørt færdigt. Denne koden sletter alle filer med endelsen {{.jpg}}.

[[http://iftek.dk/local--files/astropi:kamera/getFilesWithEnding.py getFilesWithEnding.py ]]
PAS PÅ, den sletter faktisk filerne!!!

+++ opgaver - slet filerne


[[ul]]
[[li]]
Opret et nyt
[[/li]][[li]]
Opret en ny mappe, ```sletTest```
[[/li]][[li]]
Tag et par billeder i mappen eks. Med {{raspistill -o test.jpg}}  i konsolen.
[[/li]][[li]]
Ret i koden så det kun er den mappes indhold som slettes.
[[/li]][[li]]
Udkommenter de nederste 3 linjer, #, og tjek om det er de billeder som skal slettes.
[[/li]][[li]]
Kør programmet hvor I sletter billederne, uhuuu.
[[/li]]
[[/ul]]

+ Kameraopløsning
Vi bruger billederne på [https://www.flickr.com/photos/raspberrypi/albums/with/72157676394992328 Flickr] fra tidligere missioner.

På billedet [Bankok14.39052N99.30089N.jpg] kan man rimeligt tydeligt se en ø og koordinaterne er skrevet på billedet. Vi vil prøve at finde størrelsesforholdet af vores billed. Det er ikke muligt at bruge koordinaterne direkte, men hvis man søger lidt på google maps ligner det at det godt kan være øen Mali Kyun på Thailands kyst [https://www.google.com/maps/place/14%C2%B023'25.9%22N+99%C2%B018'03.2%22E/@13.0156668,98.1246662,54528m/data=!3m1!1e3!4m5!3m4!1s0x0:0x0!8m2!3d14.39052!4d99.30089 google maps].

++ Opgave
Vi vil nu måle afstanden i på google maps og den tilsvarende afstand i pixels på billedet. Vi skal gøre det vandret og vi ved at billedet har en opløsning på (1920x1080) pixels.
[[ul]]
[[li]] Brug værktøjerne i google maps til finde afstanden fra spidsen af Mali Kyun til Great Western Torres islands ( en lille ø).
[[/li]][[li]]Mål længden i pixels på billedet.
[[/li]][[li]]Beregn lænden per pixe.
[[/li]][[li]]Beregn længden af den synlige fra rumstationen.
[[/li]][[li]]Giv et bud på usikkerheden.
[[/li]][[li]]Vurder om det er muligt at se Emma Mærsk på 397m længde.
[[/li]][[/ul]]
min løsning:
[[ul]]
[[li]]
d_Kyun_Torres = 180.63km
[[/li]]
[[li]]
Antal pixels = 851px
[[/li]]
[[li]]
Opløsning = 0.21km/px = 210m/px
[[/li]]
[[li]]
Bredden af billedet er d=1634px=>347km
[[/li]]
[[li]]
Hvis jeg har målt 10px forkert bliver intervallet [210m;215m] per px.
[[/li]]
[[/ul]]
