# 13. Crear un programa que lea varios dígitos
#  hasta que se ingrese un cero. Luego imprimir:
# a. La cantidad de pares
# b. Promedio de impares
# c. El mayor de todos los dígitos
par = 0
impar = 0
sumaimpares = 0
mayor = 0
numero = None
uno = ""
dos = ""
tres = ""
print("\n-Ingrese 0 para salir-\nEste programa muestra, de los digitos ingresados: \n1. Cantidad de pares\n2. El promedio de impares\n3. El mayor de todos los digitos")
while numero != 0 or numero < 0:
    try:
        numero = int(input("ingrese numero: "))
        if isinstance(numero, str):
            print("Debe ser un numero")
            continue
        while numero > mayor:
            mayor = numero
            tres = str(["el mayor de todos los numeros es:", mayor])
            continue
        if numero % 2 == 0 and numero > 0:
            par += 1
            uno = str(["La cantidad de pares es de:", par])
            continue
        if numero % 2 != 0 and numero > 0:
            impar += 1
            sumaimpares += numero           
            promedioimpares = sumaimpares/impar
            dos = str(["el promedio de los impares es:", promedioimpares])
            continue
    except ValueError:
        print("Ingrese un numero")
        continue

oracion = str(uno+dos+tres)
oracion = oracion.replace("'", "")
oracion = oracion.replace(",", "")
oracion = oracion.replace("]", "")
oracion = oracion.replace("[", " ")
print(oracion)
