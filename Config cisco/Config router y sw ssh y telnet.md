ordernar host con mas redes primero* (VLSM)
Por lo general poner primera ip al router,  gateway/puerta de enlace predeterminada
| RED | IPs (2**b.d.h.) | BitsHOST | mascara | mascara decimal (suma bits de red) | wildcard (255-mascaradecimal) | subred | broadcast (wildcard + subred) | Gateway/router (subred+1) |
|--|--|--|--|--|--|--|--|
| rrh | 21 | 5 | /27 | 255.255.255.224 | 0.0.0.31 | 200.20.20.64 | 200.20.20.95 | 200.20.20.65 |
| gerencia|2 | 2 | /30 | 255.255.255.252 | 0.0.0.3 | 200.20.20.112     200.20.20.115 | 200.20.20.113 |
| enlace/troncal| 2 | 2 | /30 | 255.255.255.252 | 0.0.0.3 | 200.20.20.116     200.20.20.119 | 200.20.20.117 |
| bodega|    11 | 4 | /28 | 255.255.255.240 | 0.0.0.15 | 200.20.20.96 | 200.20.20.111 | 200.20.20.97 |
(B.its d.e h.ost   )

* lo que esta entre parentesis son comentarios (como este) *

Ayudamemoria de comandos:

| Router acceso ssh:  (con usuario local, dominio, rsa, line, ip)  (recordar default gateway para acceder desde otra red) |
|-:|--|--|
| Router dominio (hostname antes):  ena && conf t && ip domain-name convision.cl (inventado ejemplo, solo es un nombre) |
| Router generate key: | conf t &&  crypto key generate rsa modulus 2048 |
| Router usuario remoto | conf t && username profe secret cisco1234 |
| Router line para ssh | conf t && line vty 0 2 && transport input ssh && login local (username del router, en este caso, "profe") |
| Router unicast-routing | conf t && ipv6 unicast-routing |
| (Login desde pc: terminal C:\> ssh -l profe 200.20.20.1 y pedirá la password) |

Switch conf :| ena&&conf t && hostname switchio && ena secret una2345 &&interface vlan1 && ip add 200.20.20.2  255.255.255.192 && ip default-gateway 200.20.20.1 && no shut
Switch enable telnet:|  conf t && line vty 3 4 && password cisco1234 && login
 (Login desde pc, terminal C:\>telnet 200.20.20.2 y pedirá contraseña)

Router, config ip y no shut|ena && conf t && int g0/0 && ip add && 200.20.20.1 255.255.255.192 (/26 ) && no shut  && exit
router, cofig interface description    ena&& conf && int g0/0  && description ejemplo de description
Router,config global:|     ena && conf t
Router, contra ena:|    ena && conf t && enable secret redes123 (contraseña modo hash MD5)
Router, encryptacion:|  ena &&  conf t && service password-encryption
contra consola:||  conf t && line console 0 && password conce1234 && login && exit
Acceso remoto:||cof t && line vty 0 4 (5 lineas)  && password qazwsx (la contra) && login && exit
guardar:|||wr
