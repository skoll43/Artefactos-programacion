#Escribir un programa que pida al usuario un número entero y
#muestre por pantalla un triángulo rectángulo como el de más abajo,
#de altura el número introducido.Utilice ciclos y valide que la altura sea mayor a 0
# *
# **
# ***
# ****
# *****
numero = input("ingrese un numero entero: ")
while True:
    numero = str(numero)
    if numero.isalpha():
        numero = input("Debe ser un N entero")
        continue
    if numero.isdigit():
        numero = int(numero)
        a = "*"
        for num in range(1,numero+1):
            print(a*num)
        break