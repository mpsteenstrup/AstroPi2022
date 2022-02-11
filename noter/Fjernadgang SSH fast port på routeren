# Fjernadgang til Pi SSH

For at få adgang udefra skal vores Raspberry pi kanaliseres gennem routeren.

Opsætning på PI
* Se portene: ```sudo netstat -tulpen```.
* I ```/etc/ssh/sshd_conf``` rediger ```port 22```til ønsket port (som er fri).

Opsætning af router, yousee
* Log ind på routeren som Admin.
* Vælg Pi fra listen.
* Vælg reserver IP, ikke nødvengigt men rart.
* Vælg omdirigering og porte og angiv ekstern og intern port til den valgte.

### Log på med SSH

* Find routerens IP, søg ```wat is my IP```.
* Log på med ```ssh -p port username@routerIP```.
* Skriv afgangskode.

Routerens IP kan skifte hvilket en DNS beskrevet nedenfor.

VNC har en fast port 5900 og det er derfor svært at sætte flere Raspberry Pi på samme netværk og tilgå dem samtidigt. De bliver nummereret fortløbende, men hvilken som er hvilken er ikke til at sige. Det kan løses med forskellige navne og passwords.





### Her er en god beskrivelse fra [How to remote to Raspberry Pi from outside local network?](https://raspberrypi.stackexchange.com/questions/105080/how-to-remote-to-raspberry-pi-from-outside-local-network)
Assume you have a Raspberry Pi connected to your Router at home. Normally your router will give IP addresses to all devices attached to it.

In my example the Router assigns to the Raspberry Pi the IP of 192.168.0.101 This IP is only visible in your internal Network and not from the World Wild Internet. This means you can connect to your Raspberry, for example via ssh from your Notebook, which is also in the same subnet as your Raspberry.

Subnets: I do not want to get too much into detail about subnets, but to keep it simple, ipv4 addresses from 192.168.0.1 to 192.168.0.254 are in the same subnet of 192.168.0.* which is 255.255.255.0, while 192.168.0.* and 192.168.1.* are not in the same subnet of 255.255.255.0 but 255.255.0.0. You will generally only encounter 255.255.255.0 meaning that the first three ip (192.168.0.) number blocks must be equal, while the fourth block (192.168.0.101) must be unique in your network. Another annotation for ip 192.168.0.101 with subnet 255.255.255.0 is also 192.168.0.101/24

Back to topic So while all your devices attached to your Router are in the same subnet and will be able to directly communicate to each other, they are not directly reachable from the Internet. From a security stand point, that is desireble.

But if your Raspberry Pi should act as a server, for example a cloud-server you might want to connect to it with your smartphone when you are not at home. Now the question is: how do I connect to the IP 192.168.0.101 from the Internet. Here come NAT and Internal/External IP into play.

Your smartphone needs to know the external IP of your router. And your router needs to know, where to route your smartphone request. So if you type into your smartphones ssh app the external ip of your router the request has to be routed to your raspberry. ssh username@88.192.54.75:22 has to be routed to 192.168.0.101.

Portnumbers: Every service that you run on your server and that you want to reach via ipv4 or ipv6 is listening on a port. It is awaiting client requests of a specified format on a specified port. Let's assume you have a webserver installed in your raspberry. The webserver server is running at Port 80 and 443, your ssh-server is running at port 22 and so on. There are a few standard ports for the different services but you are free to change these port numbers to any number you like. For example you could change your ssh port number 22 to port number 45302 by modifying one line in your sshd_conf file on your ssh server. The SSH-Server in that case will expect SSH requests on port 45302. This in turn means that you would have to advice any ssh client to use that specified port when trying to connect to the server( otherwise the client would use the standard port which is 22 ). This is usefull if you want to prevent simple bots from connecting to your ssh server. Or in case you have multiple services of the same type (for example webserver) running, to prevent them from conflicting with each other.

Here is a list of standard ports.

If you like to check what services are actually awaiting a remote connection with their respective port number you can type sudo netstat -tulpen in the console.

Back to topic If you want to make a specific service available to the outside world you need to open or forward that port to the public. That means you need to open your router web-administration and configuration page https://192.168.0.1 and create a port mapping/forwarding/NAT rule for each service that you want to make available. So if your ssh server is running at port 45302 you will need to create a rule that maps external requests (from the internet) at port 45302 to the internal device 192.168.0.101 at port 45302. Now it should be possible to connect to your ssh server using your external ip address.

Static vs dynamic ip A static ip is great but not necessary. If you have a dynamic ip you will in fact encounter the problem that you external ip will change. Therefor your can create an account at a dynamic dns service provider with your own personal dns record / domain name ( in my example my-own-domain.dyndns.org). These dynamic dns provider give you the ability to create a dns record that will point to your router ip. Your router will advert the dyndns provider whenever your router ip changes.

There are a lot or dynamic dns providers available, but only a few will be supported by your router. Somewhere in your router administration and configuration page you should find a category or topic that is named DynamicDNS. There you see which are supported from your router manufacturer. Create an account at one of those providers. Than go back to your router config page and fill out the account login data form your dynamic dns provider. Now your router should automatically notify your dynamic dns provider when your ip changes and you will only need to memorize your domain name. So when connecting to your ssh server you will type the domain instead of your external ip like: ssh username@my-own-domain.dyndns.org:45302

security aspects Every service that is reachable from the outside world might be hacked one day. If some hacker gets into your raspberry because of whatever reason, he will be able to directly communicate to any of your device inside your local network. This allows the hacker to infect even more devices. Therefor a DMZ has been invented. This is an option in your router config that should tell the router to disallow connections from that device inside the dmz to other devices outside the dmz. I am not familiar with this and my router does not even have that option too.

I suggest to you to implement one more layer of security. So instead of opening one or more ports to the public for every service that you might want to use, you could create a vpn server on your raspberry pi (ipsec, openvpn, wireguard). Than you can connect to that from the internet and are able to use any service on that raspberry without the need to open more ports in your router. This reduces the attack surface to only one service - the vpn service itself. In my opinion wireguard is the best option here, because it has very high performance and is no chatty protocol at all. That means, if anybody does a port scan on your router, he will not be able to find out, that there is an open port pointing to the wireguard service.
