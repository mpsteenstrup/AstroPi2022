# Projektarbejdet

## Arbejdsmetode ved udvikling af computerprogram
Det er en kompleks proces at lave et computerprogram. Det er vigtigt at bryde denne opgaven op i overkommelige bidder. Det er også vigtigt at starte med at lave simplere versioner af det endelige program. På den måde udvikler projektet sig hele tiden, hvilket er meget motiverende, og man kan fokusere på de simple løsninger.

### Eksempel
Vi vil gerne undersøge om astronauterne har en en fast op/ned i rumstationen, flyver de med fødderne eller hovedet forrest eller helt frit.

Det vil ideelt set kræve en algoritme som tjekker billederne inde fra rumstationen og genkender orienteringen af astronauterne. Dette er en relativt krævende machine learning proces, så lad os starte med noget simplere.

* Simpleste, Tag billeder med et fast interval.
* Næstsimpleste, tag billeder når der er astronauter foran kamearat.

Da vi ikke må hente billeder ned fra rumstationen er der ingen af de to simple programmer som gør os i stand til at besvare det oprindelige spørgmsål. De indeholder begge procedure som skal bruges til det endelige program og er meget simplere at implementere.

Denne arbejdsmetode kaldes iterativ udvikling og inddrager ofte en kommende bruger af systemet i udviklingen.

### Øvelse
* Skitser en meget simpel version af jeres program, jeg mener, meget simpel.
* Skitser en lidt mere avanceret, men stadigt simpel version.

### Overkommelige bidder
Lige som det er vigtigt for hele programmet er det også vigtigt for delelementerne, at starte simpelt. Hvis I skal tage billeder over ørkener kan det brydes ned til
* Kunne tage ét billed og gemme det.
* Kunne tage to billeder og gemme dem, ikke over hinanden.
* Kunne finde placerignen af ISS.
* Finde koordinaterne for ørkner.
* Kunne sammenholde koordinater for ørkner og for ISS.
* Programmere en forgrening baseret på koordinaterne.

Ved gruppearbejde gør en detaljeret opdeling det muligt for alle deltagere at arbejde konstruktivt på projektet.


## Ressourcer
Her kommer en liste med ressourcer, som I kan bruge i jeres arbejde. Det er også muligt at finde hjælp på nettet, men det er ofte mere komplicerede løsninger. Husk at I skal kunne forklare den kode I bruger.
* [https://astro-pi.org/mission-space-lab/resources](https://astro-pi.org/mission-space-lab/resources), samling af ressourcer fra Astro-pi.org.
* [Phase 2, Mission space lab](https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/2), oversigt over python biblioteker og tutorials.
* [Pythonfiler](https://github.com/mpsteenstrup/AstroPi2021/tree/master/pythonFiler), samling af python filer. 
* [Samlet materiale](https://github.com/mpsteenstrup/AstroPi2021/blob/master/AstroPiMateriale.pdf), samlet materiale på dansk. Da udviklingen går hurtigt er materialet ikke helt opdateret.
