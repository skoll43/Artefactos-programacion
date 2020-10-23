#4. Desarrolle un algoritmo que muestre en pantalla 1010101, la cantidad de dígitos a mostrar

numero = int(input("Este algoritmo escribe secuencias de 0 y 1,\nIngrese la cantidad de digitos que quiere: "))
while(True):
    numero -= 1 
    if numero < 0:
       print("el numero debe ser mayor a 0")
       break
    else:
        uno = "1"
        cero = "0"
        sumar = (uno + cero)*(int((numero+1)/2)) 
        if numero % 2 != 0: 
            print(sumar) 
        else:
            print(sumar+uno)
        break
