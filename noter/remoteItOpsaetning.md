
### oprette ny bruger og give adgang på RPI
skift bruger
su - newuser

ny user add to groups
sudo gpasswd -a newuser input

ny user remove to groups
sudo gpasswd -d newuser input

manage users and groups
(howtogeek.com)[https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/]

(remote.it opsætning)[https://magpi.raspberrypi.org/articles/remote-access-your-raspberry-pi-securely]

### Login med realVCN
Med realVNC kan man kun logge ind som root hvilket gør at alle rettigheder til at redigere er til.
Procedure
```
connecting->vnc->kopier nederste kode (proxy51.rt3.io:33517)->paste ind i realVNC.
```

### Login med ssh
Næsten sammen procedure
```
connecting->ssh->kopier relevant linje ind i terminal
```
### scp filoverførsel
Brug SSH interfacet.

Overførsel fra RPI til computer.
```
scp -P 30196 /Users/mpsteenstrup/temp/noter.txt newuser@proxy55.rt3.io:/home/newuser/temp/
```
Koden overfører filen ```test.jpg``` fra biblioteket ```/home/newuser/temp/``` til biblioteket ```/Users/mpsteenstrup/```. 

Overgørsel fra computer til RPI
```
scp -P 30196 newuser@proxy55.rt3.io:/home/newuser/temp/* /Users/mpsteenstrup/temp/
```
Overfører alt fra folderen temp på RPI til computeren i folderen temp
