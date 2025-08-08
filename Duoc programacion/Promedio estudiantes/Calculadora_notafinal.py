
import os

input("Calculador de nota final de introduccion a programacion, presione ENTER para empezar")



#separar la operacion de multiplicar y preguntar el pocentaje q vale

print("Escriba su primera nota parcial")
parcialnota1 = float(input())*0.25 #vale 25% de final parciales
print("Escriba su segunda nota parcial")
parcialnota2 = float(input())*0.20
print("Escriba su tercera nota parcial")
parcialnota3 = float(input())*0.20
print("Escriba su cuarta nota parcial")
parcialnota4 = float(input())*0.35
print("Escriba su nota del examen")

#parte de multiplicacion por el porcentaje q vale la nota
#valeNota1 = *0.25
#valeNota2 = *0.20

examennota1 = float(input())


listaNotasParciales = [parcialnota1, parcialnota2, parcialnota3, parcialnota4]
os.system('cls')
#lista con una variable que almacena lista de 0 - 3 (4 floats)
SumaParciales = sum(listaNotasParciales)

#cantidadNotasParciales = len(listaNotasParciales)
#promedioParciales = SumaParciales / cantidadNotasParciales
Notafinal = (SumaParciales * 0.60) + (examennota1 * 0.40)

print("su nota final para el curso es un", round(Notafinal,ndigits=1))
