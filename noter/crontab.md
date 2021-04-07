# crontab kør program på tid eller ved opstart
Crontab er en del af styresystemet hvor man kan køre programmer på bestemte tidspunkter eller med bestemte intervaller. Det kan også starte et program ved opstart. Pas på med det, da programmet evt. kører og stopper andre processer.

Følgende script er et lille Bash script, ```launcher.sh``` som flytter til folderen ```temp``` og kører programmet ```helloworld.py``` og gemmer hvad programmet nu gør i tekstfilen ```text.txt```.
```
#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/temp
sudo python3 helloworld.py > text.txt
cd /
```
Programmet skal have lov til at køre, execute. Det gøres i terminalen med kommandoen ```chmod 777 launcher.sh```.

Python programmet ```helloworld.py```er meget simpelt,
```
print('hej med dig verden')
```
For at programmet kører ved opstart skal man redigere i ```crontab``` filen ved at skriver
```
sudo crontab -e
```
og tilføje linjen
```
@reboot /home/pi/temp/launcher.sh >/home/pi/logs/cronlog.log 2>&1
```
Hvis man bruger ```nano```som editor gemmes filen med ```ctrl o``` og programmet lukkes med ```ctrl x```.

Hvis der opstår fejl vil en rapport blive gemt i ```cronlog.log``` i mappen ```logs```.

Det er også muligt at køre programmet med et interval, eks. hvert andet minut.
```
*/2 * * * * /home/pi/temp/launcher.sh >/home/pi/logs/cronlog.log 2>&1
```
