import os
from time import sleep
uno=0;dos=0;tres=0;cuatro=0;cinco=0
puno=3200;pdos=4000;ptres=5000;pcuatro=3500;pcinco=6000
while True:
    total = (uno*puno+dos*pdos+tres*ptres+cuatro*pcuatro+cinco*pcinco)
    os.system("cls")
    print("Pagina de EDGYSUSHI\n     |Ingrese 0 para terminar el pedido|\n                  Menu:\n")
    menu = f"|{uno}|${puno*uno:04d}|1.Pikachu Roll, $3200\n|{dos}|${pdos*dos:04d}|2.MegaRoll, $4000\n|{tres}|${ptres*tres:04d}|3.Otaku Roll, $5000\n|{cuatro}|${pcuatro*cuatro:04d}|4.Pulpo Venenoso Roll $3500\n|{cinco}|${pcinco*cinco:04d}|5.Sashimi de Anguila Eléctrica $6000\n          TOTAL: ${total}\n"
    print(menu);    print("    |Ingrese 0 para terminar el pedido|\n")
    try:
        item = int(input("Ingrese el item del menu que desea agregar:\n"))
        if item == 0:
            os.system("cls")
            print(menu)
            exit()
        if item == 1:
            uno = uno + 1
        if item == 2:
            dos = dos + 1
        if item == 3:
            tres = tres + 1
        if item == 4:
            cuatro = cuatro + 1
        if item == 5:
            cinco = cinco + 1
        
    except ValueError:
        os.system("cls")
        print("Tiene que ser un numero entero")
        sleep(3)