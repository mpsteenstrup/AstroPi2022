# Rpi som hotspot

Nedenstående program klare opsætningen af en wifi-hotspot. Programmet søger efter et wireless net og hvis det ikke finder det, så laver det et wifi-hotspot. Det virker derfor *kun* hvis jeres RPI har et internet kabel.


Ham her han gennemgår det godt, [Easy as Pi Access Point WIFI hotspot,  KM4ACK
](https://www.youtube.com/watch?v=qMT-0mz1lkI)

[github fil, vælg den rigtige](https://github.com/km4ack/pi-scripts)

Med det hele sat op skal I.

* Disable jeres wifi forbindelser ved at rette i ```sudo nano /etc/wpa_supplicant/wpa_supplicant.conf```. Skriv evt som han 1 i navnet, så kan den ikke finde det rigtige.
* Køre programmet sudo /usr/bin/autohotspotN
