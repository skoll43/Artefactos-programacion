from colorama import *
import os
from time import sleep
rojo=Fore.RED
verde=Fore.LIGHTGREEN_EX
oscuro=Fore.LIGHTBLACK_EX
amarillo=Fore.YELLOW
negro=Fore.LIGHTBLACK_EX
R=Fore.RESET

apagado = negro+"(o)"+R
pasar = verde+"(◙)"+R
parar = rojo+"(◙)"+R
intermedio = amarillo+"(◙)"+R

def pantalla1():
    os.system("cls")
    print(amarillo+"(1)","(2)","(3)","(4)"+R)
    print(parar,apagado,parar,apagado)
    print(apagado,apagado,apagado,apagado)
    print(apagado,pasar,apagado,pasar)
    print("pant1")
def pantalla2():
    os.system("cls")
    print(amarillo+"(1)","(2)","(3)","(4)"+R)
    print(apagado,parar,apagado,parar)
    print(apagado,apagado,apagado,apagado)
    print(pasar,apagado,pasar,apagado)
    print("pant2")
    
def intermedio1():
    os.system("cls")
    print(amarillo+"(1)","(2)","(3)","(4)"+R)
    print(parar,apagado,parar,apagado)
    print(intermedio,apagado,intermedio,apagado)
    print(apagado,apagado,apagado,apagado)
    print("int1")
def intermedio0():
    os.system("cls")
    print(amarillo+"(1)","(2)","(3)","(4)"+R)
    print(apagado,apagado,apagado,apagado)
    print(apagado,intermedio,apagado,intermedio)
    print(apagado,apagado,apagado,apagado)
    print("int0")

while True: #rojo,negro,rojo,negro,amarillo,negro,amarillo,cambia
    #rojo
    print("inicio");sleep(3)
    pantalla1();sleep(3);intermedio0();sleep(0.5);pantalla1();sleep(0.5);intermedio0();sleep(0.5);intermedio1();sleep(0.5);intermedio0();sleep(0.5)
    intermedio1();sleep(1);pantalla2();sleep(3)
    print("se devuelve");sleep(3)
    pantalla2();sleep(1);intermedio1();sleep(0.5);intermedio0();sleep(0.5);intermedio1();sleep(0.5);intermedio0();sleep(0.5);pantalla1();sleep(3);pantalla1();sleep(1)
    #rojo,negro,rojo,negro,amarillo,negro,amarillo,cambia
    print("termina");sleep(3)


