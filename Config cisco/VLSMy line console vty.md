*ordernar host con mas redes primero* (VLSM)
> 💡 Por lo general, se asigna la **primera IP de la subred al router** como puerta de enlace predeterminada.

### Tabla de Subredes VLSM
200.20.20.0/25
| Red             | IPs (2^b.d.h.) | Bits HOST | Máscara / | Máscara Decimal         | Wildcard             | Subred            | Broadcast         | Gateway/Router     |
|----------------|----------------|-----------|-----------|--------------------------|----------------------|-------------------|-------------------|--------------------|
| ventas         | 51             | 6         | /26       | 255.255.255.192          | 0.0.0.63             | 200.20.20.0       | 200.20.20.63      | 200.20.20.1        |
| rrhh           | 21             | 5         | /27       | 255.255.255.224          | 0.0.0.31             | 200.20.20.64      | 200.20.20.95      | 200.20.20.65       |
| bodega         | 11             | 4         | /28       | 255.255.255.240          | 0.0.0.15             | 200.20.20.96      | 200.20.20.111     | 200.20.20.97       |
| gerencia       | 2              | 2         | /30       | 255.255.255.252          | 0.0.0.3              | 200.20.20.112     | 200.20.20.115     | 200.20.20.113      |
| enlace/troncal | 2              | 2         | /30       | 255.255.255.252          | 0.0.0.3              | 200.20.20.116     | 200.20.20.119     | 200.20.20.117      |

> 🧮 **Bits de host (b.d.h.)**: Cantidad de bits disponibles para hosts en cada subred.

* lo que esta entre parentesis son comentarios (como este) *


# 🧠 Ayudamemoria de comandos - Router acceso SSH

# Configuración completa (usuario local, dominio, RSA, línea VTY, IP)
# Recordar configurar el default gateway para acceso desde otra red

ena
conf t
hostname convision                          # Ejemplo de nombre

ip domain-name convision.cl                 # Nombre inventado, solo es un identificador

crypto key generate rsa modulus 2048        # Generar clave RSA

username profe secret cisco1234             # Crear usuario remoto

line vty 0 2                                 # Configurar línea VTY para SSH
transport input ssh
login local                                  # Usa el usuario del router, en este caso "profe"

ipv6 unicast-routing                         # Activar unicast-routing para IPv6

# 🧪 Prueba de acceso desde PC (terminal):
# C:\> ssh -l profe 200.20.20.1
# Pedirá la contraseña configurada ("cisco1234")
lo mismo de en un solo texto: 
ena
conf t
hostname convision
ip domain-name convision.cl
crypto key generate rsa modulus 2048
username profe secret cisco1234
line vty 0 2
transport input ssh
login local
ipv6 unicast-routing
exit
	
_________________________________
Switch conf :													ena&&conf t && hostname switchio && ena secret una2345 &&interface vlan1 && ip add 200.20.20.2  255.255.255.192 && ip default-gateway 200.20.20.1 && no shut	
Switch enable telnet:								conf t && line vty 3 4 && password cisco1234 && login
	(Login desde pc, terminal C:\>telnet 200.20.20.2 y pedirá contraseña)

Router, config ip y no shut						ena && conf t && int g0/0 && ip add && 200.20.20.1 255.255.255.192 (/26 ) && no shut  && exit
router, cofig interface description   	ena&& conf && int g0/0  && description ejemplo de description
Router,config global:  		 						ena && conf t
Router, contra ena:			 						ena && conf t && enable secret redes123 (contraseña modo hash MD5)
Router, encryptacion:								ena &&  conf t && service password-encryption 
contra consola:  					 						conf t && line console 0 && password conce1234 && login && exit 
Acceso remoto:					 						cof t && line vty 0 4 (5 lineas)  && password qazwsx (la contra) && login && exit
guardar:											    			wr
_____________________________________

! 🔧 SWITCH CONFIGURACIÓN INICIAL
ena
conf t
hostname switchio
enable secret una2345
interface vlan1
ip address 200.20.20.2 255.255.255.192
ip default-gateway 200.20.20.1
no shutdown
exit

! 🔐 SWITCH - HABILITAR TELNET
conf t
line vty 3 4
password cisco1234
login
exit

! 🧪 PRUEBA TELNET DESDE PC
! C:\> telnet 200.20.20.2
! Pedirá la contraseña "cisco1234"

! 🚀 ROUTER - CONFIGURACIÓN DE IP Y ACTIVACIÓN DE INTERFAZ
ena
conf t
interface g0/0
ip address 200.20.20.1 255.255.255.192
no shutdown
exit

! 🏷️ ROUTER - DESCRIPCIÓN DE INTERFAZ
conf t
interface g0/0
description ejemplo de description
exit

! ⚙️ ROUTER - CONFIGURACIÓN GLOBAL
conf t

! 🔐 ROUTER - CONTRASEÑA ENABLE (MD5 HASH)
enable secret redes123

! 🔒 ROUTER - ENCRIPTACIÓN DE CONTRASEÑAS
service password-encryption

! 🔐 ROUTER - CONTRASEÑA DE CONSOLA
line console 0
password conce1234
login
exit

! 🌐 ROUTER - ACCESO REMOTO (VTY 0 A 4)
line vty 0 4
password qazwsx
login
exit

! 💾 GUARDAR CONFIGURACIÓN
wr