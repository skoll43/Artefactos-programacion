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

ambiente=azar(5,18)
horno=ambiente                      #horno ahora es el valor que tomó en al azar el ambiente
s = 0
while True:
    
    while horno >= 201:                #valor objetivo, deja de calentar
        
        horno = horno - azar(1,3)      #Comienza a bajar la temperatura
        sleep(0.1)
        print("off",str(horno)+"°",str(s)+"s","de","cocción")
        s +=1
        if horno >= 205:                #si es mayor a lo que se requiere
            horno=int(horno)-azar(1,5)  #enfriaelhorno
            sleep(0.1)
            s+=1
            print("ENF")
        while s >= 90:
            horno=int(horno)-azar(1,5)
            sleep(0.1)
            print(str(horno)+"°",str(s))
            if horno <= 60:
                print("hora de sacar la pizza")
                exit()

    horno=horno+azar(1,5)           #define horno como el valor actual + un aleatorio entre 1-5 (aumenta)
    print("on ",str(horno)+"°",str(s)+"s","de","cocciOn")  
    sleep(0.1)
    if horno >=199:
        s+=1