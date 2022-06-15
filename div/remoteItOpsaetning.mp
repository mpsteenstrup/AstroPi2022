

ny bruger
sudo adduser newuser

skift bruger
su newuser

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
