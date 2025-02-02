Algoritmo sin_titulo
	// 10.	Diseñar un programa que lea N números enteros y
	// determine el promedio de ellos. 	
	Escribir "Ingrese numeros para promediarlos"
	Repetir
		Leer num
		Si num = 0 Entonces
			Escribir "El promedio de los numeros ingresados, es:"
			Escribir promedio
		SiNo
			numsum = numsum + num
			cantidad = cantidad + 1
			Escribir "ingrese 0 para sumar todo y promediar"
			promedio = numsum / cantidad
		FinSi
	Hasta Que num = 0
FinAlgoritmo
