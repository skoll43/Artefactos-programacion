#Ejercicios Ciclos
#1. Muestre en pantalla los números del 1 al 100 utilizando ciclo for (Para)

for i in range(1, 101):
    print(i)

#2. Muestre los números del 1 al 100 utilizando while (Mientras)
a=0
while(True):
    if a == 100:
        break
    else:
        a += 1
        print(a)
    
#3. Calcule la sumatoria de los números del 1 al 100
a=0
suma=0
while(True):
    if a == 100:
        break
    else:
        a += 1
        suma = suma + a
        print(suma)

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

#6. Desarrolle un algoritmo que encuentre el mayor de los números ingresados por el usuario,
#el usuario debe decidir cuándo dejar de ingresar números.
grande = 0
num = 0
salir = 0
print("Ingrese numeros\nIngrese espacio vacio para terminar")
while salir != 1:
    num = input("")
    if num == " ":
        break
    else:
        if int(num) > int(grande):
            grande = num
print(grande, "Es el mas grande")

#7. Escribir un programa que muestre todas las potencias de un entero N que sean menores 
# que un valor especificado como límite.  

entero = int(input("Ingrese un entero: "))
limite = int(input("Ingrese un limite para la potencia"))
ele = 1 
while True:
    resultado= entero**ele
    if resultado >= limite:
        break
    print(f"{entero} elevado a {ele}:", resultado)
    ele+=1

#8. Crear un programa que lea un Número 5 dígitos
#  e indique cuantos ceros lo componen.
while True:
    numeros = input("Ingrese un numero:  ")
    if numeros[0]=="0" or len(numeros) < 5:
        print("No puede comenzar por 0 o ser menos a 5 digitos")
    else:
        print("La cantidad de 0 ingresados es: ",numeros.count("0"))
        break
    
#9. Crear un programa para determinar cuántas cifras tiene un número entero N
while True:
    try:
        valor = int(input("Ingrese digitos: "))
        print("su cifra tiene", len(str(valor)), "digitos")
    except ValueError:
        print("debe ingresar digitos")
        continue
        

#10. Diseñar un programa que lea N números enteros y determine el promedio de ellos.
a=0
divisor=0

while True:
    numero=int(input("Ingrese numero (0 para salir): "))
    divisor+=1
    a=a+numero

    if numero==0:
        divisor=divisor-1
        break
print("El promedio de estos números es: ",a/divisor)

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


#14. Crear un programa que Imprima
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWX
#ABCDEFGHIJKLMNOPQRSTUV
#ABCDEFGHIJKLMNOPQRST
#ABCDEFGHIJKLMNOPQR
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(string)
while True:
    string = string[:-1]
    print(string)
    if len(string) == 2:
        break

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


#16. Crear un programa que calcule e imprima la suma de los primeros 100 Números enteros
#positivos. Se debe imprimir resultados parciales después de cada 10 números sumados.
#Por ejemplo, se debe mostrar la primera suma parcial desde 1 hasta 10, la segunda suma
#parcial desde 11 a 20 y así sucesivamente hasta tener la suma total.
contador = 0
a=0
sumador = 0
sumadordesumador = 0
while(True):
    if a == 100:
        break
    else:
        a += 1
        contador += 1
        sumador += a
        if contador == 10:
            sumadordesumador += sumador
            print(sumadordesumador)
        if contador == 20:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)  
        if contador == 30:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)
        if contador == 40:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)
        if contador == 50:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)
        if contador == 60:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)
        if contador == 70:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)  
        if contador == 80:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)
        if contador == 90:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)
        if contador == 100:
            sumadordesumador += (sumador-(sumador-100))
            print(sumadordesumador)
print("Suma final",sumador)



#17. Encontrar, imprimir y contar todos los números de 4 dígitos que cumplen con la
#condición de que la suma de sus dígitos de 9. Hasta 10000.
contador = 0
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if i + j + k + l == 9:
                    print(i,j,k,l)
                    contador = contador + 1
                    print(contador)

#18. Encontrar e imprimir todos los números de 4 dígitos que cumplan con la condición de
#aque la suma de los dígitos pares es igual a la suma de los dígitos impares.
cuentapares = 0
cuentaimpares = 0
for i in range(1,10):
    if i % 2 == 0:
        for j in range(0,10):
            if j % 2 == 0:
                for k in range(10):
                    if k % 2 == 0:
                        for l in range(10):
                            if l % 2 == 0:
                                pares = (i+j+k+l)
#                                dpares = i,j,k,l
                                cuentapares = cuentapares + 1
#                                print(pares)
                                for a in range(10):
                                    if a % 2 != 0:
                                        for b in range(10):
                                            if b % 2 != 0:
                                                for c in range(10):
                                                    if c % 2 != 0:
                                                        for d in range(10):
                                                            if d % 2 != 0:
                                                                impares = (a+b+c+d)
 #                                                               dimpares = a,b,c,d
                                                                cuentaimpares + cuentaimpares + 1
                                                                if pares == impares:
                                                                    print(i,j,k,l,pares,"=",a,b,c,d,impares)
                                                                    

#19. Crear un programa que invierta un número entero cualquiera

num = input("Ingrese un numero: ")
numinvertido = str(num[::-1])
print(numinvertido)


