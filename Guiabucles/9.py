#9. Crear un programa para determinar cuántas cifras tiene un número entero N
while True:
    try:
        valor = int(input("Ingrese digitos: "))
        print("su cifra tiene", len(str(valor)), "digitos")
    except ValueError:
        print("debe ingresar digitos")
    