from random import randint as azar
from time import sleep
from os import system
import winsound 

ambiente=azar(5,18)
horno=ambiente                      #horno ahora es el valor que tomó en al azar el ambiente
s = 0                               #segundos en el programa

txto=["[MANTENIEND🥧]","[CALENTANDO🔥]","[ENFRIANDO❄️ ]."]
plato="╭--------╮"

def pant():
    print(f"╭━━━━━━━━━━━━━━━━━━━━━━━━━━━╮\n┃〮..........{horno:03d}°......{s:02d}⏳.┃\n┃.⠿⠿.....{new}.....┃\n┃║████████████████████████║╖┃")
    print(f"┃║████████████████████████║║┃\n┃║████████████████████████║║┃\n┃║████████████████████████║║┃\n┃║███████{plato}███████║╜┃")
    print("┃...........................┃\n╰━━━━━━━━━━━━━━━━━━━━━━━━━━━╯\n")



while True:
    while horno >= 201:                #valor objetivo, deja de calentar
        horno = horno - azar(1,3)      #Comienza a bajar la temperatura
        sleep(0.5)
        print("off",str(horno)+"°",str(s)+"s","de","cocción")
        s +=1 #pasa un segundo de coccion
        system("cls")
        new=txto[0]
        pant()
        while s >= 90: #cuando llega sobre 90s
            horno=int(horno)-azar(1,5) #empieza a enfriar
            sleep(0.5)
            print(str(horno)+"°",str(s))
            system("cls")
            new=txto[2]
            pant()
            if horno <= 60:
                print("hora de sacar la pizza")
                winsound.Beep(3000,200);winsound.Beep(4400,400);winsound.Beep(4400,800);winsound.Beep(4400,1000)
                exit()
    horno=horno+azar(1,5)           #define horno como el valor actual + un aleatorio entre 1-5 (aumenta)
    sleep(0.5)
    print("on ",str(horno)+"°",str(s)+"s","de","cocciOn")  
    if horno > 199: #empieza a contar s de coccion
        s+=1
        plato="╭🍕🍕🍕🍕╮"
    system("cls")
    new=txto[1]
    pant()
