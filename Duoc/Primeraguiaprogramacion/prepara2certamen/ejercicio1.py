hombres = 10500
mujeres = 8000
socios = 6000
h = 0
m = 0
s = 0
import os
while True:
    os.system("cls")
    print(f"Ingrese entradas que quiere comprar\n            Precios\n--------------------------------\n           Opciones:\n       'ok' para salir\n       1) Hombre(s): ${hombres}\n       2) Mujer(s):  ${mujeres}\n       3) Socio(s):  ${socios}\n--------------------------------\n     TOTAL:{(hombres*h)+(mujeres*m)+(socios*s)} \n{h} hombres: {hombres*h}\n{m} mujeres: {mujeres*m}\n{s} socios: {socios*s}")
    entradas = input("Ingrese opcion: ")
    if entradas == "1":
        os.system("cls")
        h+=1
        continue
    if entradas == "2":
        os.system("cls")
        m+=1
        continue
    if entradas == "3":
        os.system("cls")
        s+=1
        continue
    if entradas == "ok":
        break
    else:
        os.system("cls")
        print("Debe ingresar una opcion valida")
        os.system("pause")
        os.system("cls")
        continue