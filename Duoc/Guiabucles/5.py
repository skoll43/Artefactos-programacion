#5. Desarrolle un algoritmo que permita a un usuario ingresar letras hasta que decida salir del
#programa y finalmente muestre cuantas letras ingreso.
letras = ""
while True:
    ingresadas = input("Ingrese una letra (0 para salir): ")
    letras += ingresadas.isnumeric()
    if ingresadas == "0":
        print(ingresadas)
        print("La cantidad de letras ingresadas es:", len(letras)-1)
        break