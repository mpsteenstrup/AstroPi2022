### opsætning af Astro-Pi til VNC adgang
Opsætningen af en ny Astro-Pi gøres lettest ved at koble den til en HDMI skærm, tastatur og mus.

Det anbefales at købe en wifi-router hvor både elever og RPI kan blive koblet på. Det er ofte problematisk med skolenetværk med sikkerhedprotokoller osv. Køb ikke en for billig router da den skal kunne klarer både elevernes computere og Astro-Pi.


### på Astro-Pi
* Skift kodeord under præferencer.
* I højre logges på wifi.
* Ved siden af styk på VNC symbolet og vælg ```options->Security->Authentication``` vælg ```UNIX password```.
* Vælg ```Troubelshooting``` vælg ```Enable direct capture```, så kan i se preview fra kameraet over VNC.

### Fast IP-addresse
For at få adgang til jeres Astro-Pi skal I kende IP-adressen. I kan se den ved at trykke på VNC. Hvis i ikke har nogen skærm er det rart med en fast IP-adresse.

* Find router adresse (her 192.168.1.1): ```ip r | grep default``` hvilket for mig giver ``` default via 192.168.1.1 dev wlan0 proto dhcp src 192.168.1.4 metric 303 ```
* Updater filen ```dhcpcd.conf```fil ved at skrive ```sudo nano /etc/dhcpcd.conf``` i terminalen.
* Generel skal der indtastes
```
interface wlan0
static ip_address=STATIC_IP/24
static routers=ROUTER_IP
static domain_name_servers=DNS_IP
```
* For min router for Pi nr 7
```
interface wlan0
static ip_address=192.168.1.107/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```
* Gem filen med ```ctrl o```.
* Reboot og tjek om IP-adressen er den rigtige.

### static IP
Statisk IP addresse til informatik2022 router.
* AstroPiRys1 192.168.1.101
* AstroPiRys2 192.168.1.102
* AstroPiRys3 192.168.1.103
* AstroPiRys4 192.168.1.104
* AstroPiRys5 192.168.1.105
* AstroPiRys6 192.168.1.106
* AstroPiRys7 192.168.1.107

Nye Astro pi
* AstroPiRys10 192.168.1.110
* AstroPiRys11 192.168.1.111
* AstroPiRys11 192.168.1.112
* AstroPiRys11 192.168.1.113
* AstroPiRys11 192.168.1.114
* AstroPiRys11 192.168.1.115
* AstroPiRys11 192.168.1.116


### github
Vi kan bruge Github på vores Pi. Det kan bruges til at dele filer og virker godt til at overføre filer til alle elever.

Man kan klone et girhub-bibliotek. Dette har de fleste af de python filer der skal bruges til lærerkurset i Astro-Pi.
```git clone https://github.com/mpsteenstrup/AstroPiPythonFiler.git```

Hvis man skal bruge det selv kan man oprette sig på github og lave en mapps som man synkroniserer.
* ``` git clone http:...```
* ``` git add .; git commit -m "test"; git push origin master ```
* git husker username og token efter denne kmmando, ``` git config --global credential.helper store ```



## opdatering af opencv fra headless
ESA har valgt at insatallerer openCV som headless. Det gør at man ikke kan bruge preview osv. når man arbejder med programmet. Det er ret irriterende og kan omgøres med følgende kommandoer i terminalen,
```
sudo pip3 uninstall opencv-python
sudo pip3 uninstall opencv-contrib-python
sudo pip3 uninstall opencv-contrib-python-headless

sudo pip3 install opencv-python==4.6.0.66
sudo pip3 install opencv-contrib-python==4.6.0.66
```
Den nyeste version at openCV kan findes på [https://pypi.org/project/opencv-python/](https://pypi.org/project/opencv-python/)



### setup wifi
Hvis Man skal sætte
Lav fil i roden, ```wpa_supplicant.conf```

```
country=DK
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```


### Login med realVCN
Med realVNC kan man kun logge ind som root hvilket gør at alle rettigheder til at redigere er til.
Procedure
```
connecting->vnc->kopier nederste kode (proxy51.rt3.io:33517)->paste ind i realVNC.
```

### micro en editor
Editor til terminal med "moderne" arbejdsgange.

### oprette ny bruger og give adgang på RPI
* Tilføj ny bruger, user, ```sudo adduser new_username```
* Skift kodeord,```sudo passwd username```
* skift bruger, ```su - newuser```.
* ny user add to groups, ```sudo gpasswd -a newuser input```. add ```video``` og ```i2c```.
* ny user remove from groups, ```sudo gpasswd -d newuser input```
* Slet user, ```userdel -r username```
* For at kunne bruge SenseHat og kamera skal den nye bruger have adgang til grupperne, ```video```, ```input```, ```i2c ```.
* Liste med usernames ```awk -F':' '{ print $1}' /etc/passwd```


manage users and groups
(howtogeek.com)[https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/]
