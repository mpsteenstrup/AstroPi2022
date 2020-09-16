# Undersøgelse af ukendt land eller hvad sker der i mit køleskab når døren er lukket?
Selvom målet er at lave forsøg i vægtløs tilstand, ombord på den internationale rumstation, kan vi også bruge vores Astro Pi til at lave forsøg her på Jorden. Det er en central del når eleverne udvikler programmer, at de først udføre test hernede, før koden bliver sendt op. En afprøvning ad måleudstyret er essentiel for et vellykket eksperiment, især når det ikke bare lige kan gøres om.

Nedenstående side indeholder et forsøg hvor temperaturen og trykket bliver målt inde i et køleskab. Eksperimentet vil kunne køre i et modul, 90 minutter, efter at eleverne er blevet fortrolig med at måle og gemme data på Astro Pi computeren.

Vi opbygger det som en klassisk fysikrapport og der er fokus på analyse af fejlkilder, kalibrering af måleudstyr og simpel datebahendling. Projektet er relativt styret, men det er muligt at udvide med elevernes egne forslag til målinger af, magnetfelter, luftfugtighed, længere tid osv.

### Formål
Formålet er at undersøge tryk og temperatur i et køleskab lige efter det er lukket.
### Teori
Vi har observeret at et køleskab binder lige efter det er lukket. Ud fra idealgasligningen ved vi at der er en sammenhæng mellem tryk og temperatur, hvor trykket er proportionalt med temperaturen. Et fald i temperatur vil altså medføre et trykfald. Den varme luft som bliver lukket ind i køleskabet bliver afkølet og trykket falder. Efter et stykke tid vil trykket udligne sig, da køleskabet ikke er helt tæt.
### Apparatur
Raspberry Pi, senseHat, power bank.
Programmet
Hvis vi er heldige så kan wifi signale godt trænge ind i køleskabet og vi har fuld kontrol over vores Astro Pi gennem hele eksperimentet. Programmet vi skal bruge ligner til forveksling programmet, gemDataKolonne.py, med  variablene time, temperature, pressure.
For at holde det adskilt laver vi en ny kodefil.
[koeleskab.py](../pythonFiler/koeleskab.py)
```
import datetime
from time import sleep
from sense_hat import SenseHat
sense = SenseHat()


start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=180)

with open ("test.csv", "w") as file:
    file.write("time , Temperature , pressure \n")

while now_time < start_time + duration:
    t = sense.get_temperature()
    p = sense.get_pressure()
    now_time= datetime.datetime.now()

    with open ("koeleskab.csv", "a") as file:
        file.write("%s, %s, %s  \n" % (now_time, t,p))
    sleep(0.1)

```
### Udførsel
Placer jeres Astro Pi i et køleskab og start programmet. Åben køleskabet og kig efter noget lækkert. Luk det igen og vent til programmet har kørt færdigt, spis eventuelt det lækre I fandt.

### Databehandling
Databehandlingen foregår som altid med at lave grafer her en over temperaturen og en over trykket som funktion af tiden, (t, temp) og (t, tryk). Det kan være en ide at lave tidsmålingern om til antal sekunder efter start i stedet for now_time, se ovenfor hvordan I gør.

### Opgave
* Udfør forsøget og lav databehandlingen.
* Overvej hvorvidt jeres resultater giver mening.

Hvis jere målinger ligner mine så giver jeres trykmåling fine resultater mens temperaturmålingerne er helt ved siden af. Lad os arbejde lidt med temperaturmåleren, selvom det ikke bliver helt godt.

### Kalibrering af måleudstyr
Vores Raspberry Pi computer med senseHat er ret kompakt, hvilket ofte er fedt. Når vi skal måle temperature er det bare ikke så smart, at have sensoren siddenden lige oven på en CPU som de fleste ved bliver varm. Det er snarere reglen end undtagelsens at måleudstyr skal kalibreres så lad os prøve det. Kalibreringen foregå ved at måle den faktiske temperatur og den målte temperatur på vores Astro Pi og lave en graf med de to målinger en ud af hver akse.

### Opgave
* Kør programmet i hhv. køleskabet og i klasselokalet og mål temperaturen med et normalt velfungerende termometer.
* I har nu to datapunkter og kan jo lave en hypotetisk sammenhæng, lineær er den simpleste og simpelt er godt når man ikke ved bedre, vi ved ikke bedre.
* Udtænk en måde at få flere datapunkter så I kan teste den lineære sammenhæng ( lad vær med at putte jeres Astro Pi i ovnen, fryseren, tørretumbleren, vand eller noget andet fjollet).
* Det er ikke sikkert at der er en flot funktionel sammenhæng, lineær, eksponentiel, potens, eller lignende. Som I ved fra matematik kan man bruge polynomier til at komme tæt på. Gør det og vurder inden for hvilket område I er rimeligt sikre på jeres kalibrering.

Når I har kalibreringsfunktionen er det rimeligt let at implementerer den i koden. Her skal I være opmærksomme på at Python bruger ** for potensopløsning, eks er x i anden ```x**2```. Hvis kalibreringskurven eks. er givet ved ```y = 1.2 x-14```, vil den rigtige temperatur kunne findes ved.
```t = 1.2*t-14```.
Implementer jeres kalibrering af temperaturen.

I har nu en fint kalibreret temperaturmåler, men kan I overhovedet måle ændring når køleskabet åbnes og lukkes? Jeg kunne ikke da jeg prøvede, men jeg brugte heller ikke et af de vigtigste redskaber i værktøjskassen, gennemsnit.

Simpel kode til at tage gennemsnittet af temperaturen over ti målinger
```
i = 0
t = 0
while i<10:
 t = t + sense.get_temperature()
 i = i + 1
t = t/10
```

### Opgave
* Implementer gennemsnit og se om I kan få temperaturmålingerne til at blive mere konsistente.
* Overvej hvor lang tid det giver mening at tage gennemsnit over, I har data fra trykket til at hjælpe jer.

### Konklusion
Hvad kan I faktisk konkludere ud fra jeres undersøgelser, om hvad der sker i jeres køleskab?

### Perspektivering
Det er aldrig rart at ens udstyr ikke virker 100% som man gerne vil, men trods alt bedre at finde ud af her på Jorden end på ISS eller Månen eller Mars. Når I skal designe eksperimenter er det vigtigt at undersøge.
* Kan Astro Pi faktisk måle det jeg gerne vil, eks. temperatur.
* Kan den måle det med en præcision som giver mig noget håb om at svare på mit spørgsmål.
Det sidste kan være svært at svare på og I må ikke være for kritiske for så risikerer I at intet kan lade sig gøre. Det er også muligt at lave sit eksperiment om så man bruger andre variable, eks.ved vi at tryk og temperatur er korrelerede, så måske kan en troværdig trykmåling bruges i stedet. Det kan også være at det er ændringer i stedet for absolutte værdier I er interesserede. Hvor meget ændrer det magnetiske felt sig rundt om Jorden er ofte nemmere at måle end hvor stort den absolutte magnetisme om bord på ISS er. Det kræver med andre ord fantasi og forståelse for måleinstrumenter at lave forsøg, hvem havde troet det ;-).
