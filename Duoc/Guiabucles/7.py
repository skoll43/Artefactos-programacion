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
