### Login med realVCN
Med realVNC kan man kun logge ind som root hvilket gør at alle rettigheder til at redigere er til.
Procedure
```
connecting->vnc->kopier nederste kode (proxy51.rt3.io:33517)->paste ind i realVNC.
```


### oprette ny bruger og give adgang på RPI
* skift bruger, ```su - newuser```.
* ny user add to groups, ```sudo gpasswd -a newuser input```
* ny user remove from groups, ```sudo gpasswd -d newuser input```
*Tilføj ny bruger, user, ```sudo useradd new_username```
* Skift kodeord,```sudo passwd username```
* Slet user, ```userdel -r username```
* For at kunne bruge SenseHat og kamera skal den nye bruger have adgang til grupperne, ```video```, ```input```, ```i2c ```.



manage users and groups
(howtogeek.com)[https://www.howtogeek.com/50787/add-a-user-to-a-group-or-second-group-on-linux/]
