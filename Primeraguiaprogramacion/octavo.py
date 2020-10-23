d1 = int(input("Ingrese el primer digito"))
#d2 = int(input("Ingrese el segundo digito"))

unidad =  d1 % 10
decena = int((d1 - unidad) / 10)

suma = unidad + decena

print(suma)