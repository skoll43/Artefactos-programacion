#15. Imprimir los primeros
#N números primos desde 1 en adelante.

#Generar numeros (while)
#Dividir ese numero por otro generador de numeros (For)
#si al dividir, da 0 sobre 2 veces, no es primo, limpiar resto y salir del for
#vuelve al while, genera otro numero
lista = []
num=1
exacta = 0
#Generar numeros (while)
limite = None
while True:
    try:
        limite = int(input("Ingrese cantidad de primos a mostrar: "))
        if (isinstance(limite, str) or limite < 0) or "":
            print("Ingrese un numero y que sea mayor a 0")
        else:
            break
    except ValueError:
        print("Debe ser un numero")
        continue

while num < 1000:  
    for i in range(1, num):
        resto = num%i
        if resto == 0:
            exacta += 1
        else:
            pass
    if exacta == 1:
        lista.append(num)
    else:
        pass
    exacta = 0
    num = num + 1
print(lista[:limite])