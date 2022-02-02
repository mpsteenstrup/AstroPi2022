### github
Vi kan bruge Github på vores Pi.

* ``` git clone http:...```
* ``` git add .; git commit -m "test"; git push origin master ```
* git husker username og token efter denne kmmando, ``` git config --global credential.helper store ```

### static IP
Statisk IP addresse til Informatik router.
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

Sæt på UNIX for at kunne indtaste username

https://www.makeuseof.com/raspberry-pi-set-static-ip/

nuværende ip addresse: ```ip r | grep default```
default via 192.168.1.1 dev wlan0 proto dhcp src 192.168.1.4 metric 303

static router: ```hostname -I```
192.168.1.4

static domain_name_servers: ```sudo nano /etc/resolv.conf```
nameserver 192.168.1.1

edit
```sudo nano /etc/dhcpcd.conf```

Generel skal der indtastes
```
interface NETWORK
static ip_address=STATIC_IP/24
static routers=ROUTER_IP
static domain_name_servers=DNS_IP
```
For min router for Pi nr 7
```
interface wlan0
static ip_address=192.168.1.107/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

informatik2 reouter ip_addresse: ```192.168.1.171```

### setup wifi

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
