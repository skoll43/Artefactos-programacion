import os
from time import sleep
from colorama import *
from random import randint as azar

luz = "○"
azul = Fore.BLUE
rojo=Fore.RED
verde=Fore.LIGHTGREEN_EX
amarillo=Fore.YELLOW
R=Fore.RESET
rama = R+verde+"#"+R
lista = [azul,rojo,verde,amarillo]
while True:
    sleep(0.5)
    os.system("cls")
    rand = R+lista[azar(0,3)]+"○"
    luz1 = R+lista[azar(0,3)]+"○"
    luz2 = R+lista[azar(0,3)]+"○"
    luz3 = R+lista[azar(0,3)]+"○"
    luz4 = R+lista[azar(0,3)]+"○"
    luz5 = R+lista[azar(0,3)]+"○"
    luz6 = R+lista[azar(0,3)]+"○"
    luz7 = R+lista[azar(0,3)]+"○"
    luz8 = R+lista[azar(0,3)]+"○"
    luz9 = R+lista[azar(0,3)]+"○"
    luz10 = R+lista[azar(0,3)]+"○"
    print(f"     {rama}    \n    {rama}{luz1}{rama}   \n   {rama}{luz2}{rama}{luz3}{rama}    \n  {rama}{luz4}{rama}{luz5}{rama}{luz6}{rama}  \n {rama}{luz7}{rama}{luz8}{rama}{luz9}{rama}{luz10}{rama} \n     {verde+'|'+R}")

    print(luz+"   <-- Esa se cayó")


