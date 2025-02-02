#8. Crear un programa que lea un Número 5 dígitos
#  e indique cuantos ceros lo componen.
while True:
    numeros = input("Ingrese un numero:  ")
    if numeros[0]=="0" or len(numeros) < 5:
        print("No puede comenzar por 0 o ser menos a 5 digitos")
    else:
        print("La cantidad de 0 ingresados es: ",numeros.count("0"))
        break
    
