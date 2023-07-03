#2.Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
#y muestre por pantalla el número de veces que aparece laletra en la frase.Utilice ciclos.
import os
contador = 0
while True:
    os.system("cls")
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra: ")
    if frase.isalnum():
        print("Debe contener solo letras")
        os.system("pause")
        continue
    if letra.isalpha():
        for i in frase:
            if i == letra:
                contador +=1
        print("Su frase\n '"+frase+"' \ntiene:", contador, "letras","'"+letra+"'")
        break
