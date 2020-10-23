#11. Hacer un programa para calcular 
#el valor de la suma de los N primeros enteros. Por
#ejemplo si N es 5 la suma es 15 ( 1 + 2 + 3 + 4 + 5 = 15)
suma = 0
while True: 
    numero = int(input("(Ingrese 0 para salir)Ingrese numero: "))
    if numero <= 0:
        break
    else:
        while True:
            suma += numero
            numero -= 1
            if numero == 0:
                print(suma)
                break