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