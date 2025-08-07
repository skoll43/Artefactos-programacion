#Se debe crear el código para un horno que cocina “Pizzas Perfectas”.

#El horno que está a temperatura ambiente (entre 5 y 18; Utilice Azar) debe calentarse a 200 grados, para ello tiene un dispositivo que aumenta la temperatura cada 1 segundo (azar entre 1 y 5).
#Una vez alcanzada la temperatura la pizza debe mantenerse por 90 segundos en un rango de 200 ° +/- 5°.
#El horno al no recibir calor se enfría entre 1 y 3 grados cada 1 segundos, por lo tanto, al bajar la temperatura del rango, se acciona el dispositivo que aumenta calor.
#Una vez pasado el tiempo de cocción, el horno tiene un dispositivo de enfriamiento que enfría entre 1 y 5 grados cada segundo. Enfríe el horno hasta 60° para sacar la pizza.
#Desarrolle un algoritmo en Python que realice el proceso cocción y muestre la temperatura durante todo el proceso cada 1 segundo.

#temp normal 5-18°c  // objetivo 200°c // con energia aumenta 
#funcionamiento en 195 - 205°c
#enfriamiento sin energia entre (1 - 3°c)*1seg
#modo enfriamiento (1-5°c)*1seg //Objetivo 60°c


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
