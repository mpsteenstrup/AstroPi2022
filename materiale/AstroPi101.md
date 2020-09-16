# Første gang med Astro Pi
Med den virtuelle adgang eller med skærm og tastatur er det nu I skal arbejde med jeres PI. Der er flere editorer til vi bruger Thonny som findes under Programming.


Pas på med at have for mange programmer åbne på samme tid, det er en microcomputer med begrænset regnekraft.

![TonnyEditoren.png](billeder/TonnyEditoren.png)

### Opgave
* Åben Thonny og skriv ```print('Astro Pi')```
* Gem programmet som ```printAstroPi.py```, og lav en mappe som I kan arbejde i. , undgå som altid æøå, mellemrum og mærkelige tegn.
* Find ```printAstroPi.py```, og kør det, .


I har nu jeres egen mappe og skal IKKE ændre i andre mapper, vel?

I princippet har I nu en Linux computer som kan langt det meste som I har brug for. Tag et kig i menuen og se hvor meget gratis open source programmer der er og hvor meget en computer til 500 kr kan!

## Tænd og sluk
Vores Astro Pi kan godt lide at blive slukket rigtigt, hvilket man gør som man forventer, ingen hints. Hvis den er slukket tænder man den ved at tænde for strømmen, bum computere er nemme.

## Første dataopsamling med Astro Pi
Vi kan selvfølgeligt køre programmer på vores Astro Pi ellers var den jo ubrugelig.

### Opgave
* Copy-paste programkoden fra [gemDataKolonner.py](pythonFiler/gemDataKolonner.py) ind i Thonny editoren og kør programmet. ( copy paste er ikke helt stabilt, men prøv et par gange hvis det ikke virker umiddelbart og husk at paste er crtl v, og ikke cmd v i linux, brug evt. musen og højreklik).
* Det kan være rart at se at programmet kører og stopper så skriv print('starter') og print('slutter') fornuftige steder i programmet.
* Åben test.csv filen inde fra Thonny og tjek at I har fået det data I vil.

I har nu samlet data op med jeres Astro Pi og er faktisk ikke så langt fra at kunne lave eksperimenter på ISS.

## Sende data til Astro Pi
Den simpleste måde er nok standard copy-paste, hvor Astro Pi bruger ctrl og ikke cmd tasten.
Hvis det ikke virker kan man bruge VNC viewer programmet.

## VNC viewer
I midten toppen er der en lille menu hvor man kan sende filer til Astro Pi computeren. Den er lidt hemmelig, men man kan godt finde den.

![billeder/VNCDataUd.png](billeder/VNCDataUd.png)


Terminal
Ligesom vi kan få adgang til vores Astro Pi gennem ssh, kan vi også sende filer med scp.

Det kan gøres med scp sådan i en terminal

```scp fil brugernavn@ipadresse:```

eks.

``` scp sort.jpg pi@192.168.1.99:```

Derefter kodeord


### Data ud af RPI
Med VNC kan man overføre filer og mapper, godt for backup, backup er vigtigt!!!

![VNCTransferFile.png](billeder/VNCTransferFile.png)

* Med Raspbian, styresystemet,  klik på VNC symbolet.
* Vælg File Transfer fra drop down menuen i højre hjørne.
* Find filen og overfør den.

Det kan også gøres med terminalen på jeres lokale maskine og scp:

Eks. hvis jeg vil flytte filen test.cvs filen fra Astro Pi til min egen computer
```scp pi@192.168.1.99:/home/pi/mp/test.csv /Users/mpsteenstrup```
altså
```scp pi@ipadresse:/stiTilFil stiTilMappe```
Her har jeg lavet mappen mp og kørt programmet (gemDataKolonner.py) fra denne mappe.

### Opgave
* Overfør datafilen til computren og åben den, eks. i LoggerPro.
* Undersøg hvor meget filen fylder og overvej om det kan give problemer i et 3 timer langt forsøg med maksimal 3Gb til rådighed.
