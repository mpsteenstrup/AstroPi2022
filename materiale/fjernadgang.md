
## remote it
Vi bruger remote.it til at få fjernadgang til vores Astro Pi.

### opsætning af egen Astro Pi med remote it.
Hvis I vil få adgang til jeres egen Astro Pi kan I følge denne vejledning.
[remote.it opsætning](https://magpi.raspberrypi.org/articles/remote-access-your-raspberry-pi-securely). Det behøves ikke hvis skolen har en Astro Pi som I kan få adgang til.

### remote it konto
I skal have en konto på [remote.it](remote.it).

Hvis I deler jeres login mail, kan jeg dele adgang til Astro Pi.

Nu kan jeg give adgang til en Astro Pi jeg har liggende.

### Terminal eller Command Prompt
Terminalen er et interface hvor man kan skrive kommandoer til computeren. Hos Linux og Mac computere hedder det en terminal, mens det i Windows hedder en kommando prompt eller Command Prompt.

Windows: Søg på command prompt.
Mac: Søg på Terminal.

Vi kan bruge terminalen til at køre programmer og flytte filer og meget andet. Her er et [cheat sheet](https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/).

Vi skal bruge terminalen til at få adgang til en Astro Pi som ligger på skolen. I kan køre jeres kode og så resultaterne direkte hjem i stuen.

### Login med ssh
Vi skal bruge protokollen SSH til at få adgang til vores Astro Pi. Jeres remote.it konto vil have adgang til en Astro Pi og I skal
```
connecting->ssh->kopier relevant linje ind i terminal
```
![ssh](/materiale/billeder/ssh.png)
Skriv ```astropi2020_1``` i stedet for ```LOGIN ```.
Password får I.

nu har I adgang!

### Øvelse, Lav jeres egen mappe en fil og kør den
I skal kunne lave mapper, flytte jer rundt i dem, lave og redigere filer og køre python kode.

Kommandoerne i terminalen er
* ```mkdir test```lav en mappen 'test'.
* ```cd test```flyt jer til mappen 'test'.
* ```micro test.py``` laver filen 'test.py' og åbner de i editoren micro.
* skriv en hilsen til jer selv, ```print('sikke dejligt vejr det er')``` og gem den.
* kør python filen med ```python3 test.py```.

I kan nu både skabe mapper og filer og køre programmer. Hvad mere har man brug for?

#### nyttige terminalkommandoer
* ```cd ..``` flyt op.
* ```ls``` vi indhold af mappe.
* ```rmdir``` slet mappe.
* ```rm``` slet fil.

### scp filoverførsel
Filovergørsel, vi har brug at kunne overgøre filer til vores Astro Pi. Copy paste virker ok, men nogen gange er det større mængder kode eller datafiler og billeder.  Vi bruger protokollen SCP.

#### Overgørsel fra computer til RPI
```
scp -P 30196 /Users/mpsteenstrup/temp/noter.txt newuser@proxy55.rt3.io:/home/newuser/temp/
```
Koden overfører filen ```noter.txt``` fra folderen temp på computeren ```/Users/mpsteenstrup/temp/``` til folderen ```/home/newuser/temp/``` op RPI.

scp -P 30180 astropi2020_1@proxy55.rt3.io:/home/astropi2020_1/temp/* /Users/mpsteenstrup/temp/



#### Overførsel fra RPI til computer.
```
scp -P 30196 newuser@proxy55.rt3.io:/home/newuser/temp/* /Users/mpsteenstrup/temp/
```
Overfører alt fra folderen temp på RPI til computeren i folderen temp.
