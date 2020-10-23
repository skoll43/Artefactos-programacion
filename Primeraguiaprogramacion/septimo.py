from math import pi
radio = int(input("Ingrese el radio: "))
altura = int(input("Ingrese la altura: ")) 
volumen = pi * (radio**2) * altura
area = (2*pi * radio * altura)

print("el volumen es: ",round(volumen,2),"y el area es: ",round(area,2))