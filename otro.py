suma = 0
while True:
    num=int(input("Ingrese numeros pares, un impar para terminar"))

    if num%2==0:
        suma += num
        print("la suma va en: ", suma)
    else:
        print("numero impar ingresado, se imprimira la suma de los anteriores sumados: ",suma)
        break
