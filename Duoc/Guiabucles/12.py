#12. Diseñar un programa
#que lea 10 letras e indique cuántas de ellas son vocales.
while True:
    letras = ""
    try:
        letras = input("Ingrese 10 letras: ")
        if letras.isnumeric():
            print("wtf")
            continue
        if len(letras) == 10:
            contador = letras.count("a") + letras.count("e") + letras.count("i") + letras.count("o")+ letras.count("u")
            contador2 = letras.count("A") + letras.count("E") + letras.count("I") + letras.count("O")+ letras.count("U")
            suma = contador + contador2
            print("vocales en la palabra:", suma)
            break
        
        else:
            print("Ingrese exactamente 10 letras")
            continue
    except ValueError:
        print("deben ser letras")
        continue