#Lamparas con genio E-mazon 100usd x art
#descuentos por  cantidad de productos comprados
#cada 5 = *(-0.10) (descuento de 10%)
#si compra 10 = *(-0.15) (descuento de 15%)
#el programa valida que se compre al menos 1
import os
from time import sleep
desc1 = 0
desc2 = 0
while True:
    os.system("cls")
    print("Pagina de lampara de genio en E-mazon\n100 USD x Lampara de genio DESCUENTOxArticulo: 0.10 sobre 5, 0.15 sobre 10")
    cantidad = input("Ingrese la cantidad de lamparas que quiere comprar:\n")
    os.system("cls")
    try:
        if int(cantidad)<5:
            cantidad = int(cantidad)*100
            os.system("cls")
            print("Debe pagar:",cantidad,"USD")
            exit()
        if int(cantidad)==5 or (int(cantidad)<10 and int(cantidad)>5):
            cantidad = int(cantidad)*100
            desc1 = int(cantidad)*(-0.10)
            cantidad = int(cantidad) + desc1
            os.system("cls")
            print("Debe pagar:",cantidad,"USD")
            exit()
        if int(cantidad)>9:
            cantidad = int(cantidad)*100
            desc2 = int(cantidad)*(-0.15)
            cantidad = int(cantidad) + desc2
            os.system("cls")
            print("Debe pagar:",cantidad,"USD")
            exit()
        if int(cantidad)==0:
            os.system("cls")
            print("Tiene que ser al menos 1")
            sleep(4)
    except ValueError:
        os.system("cls")
        print("Tiene que ser un numero entero")
        sleep(3)
