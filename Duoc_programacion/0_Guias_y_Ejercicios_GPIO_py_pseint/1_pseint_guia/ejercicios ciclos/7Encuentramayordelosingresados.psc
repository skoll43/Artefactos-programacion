Algoritmo sin_titulo
	Escribir "ingrese numero" 
	Escribir "Para salir, ingrese un espacio vacio"
	Repetir
		Leer num
		Si num = () Entonces
			salir = 1
		FinSi
		Mientras num > grande Hacer
			grande = num
		FinMientras
	Hasta Que salir = 1
	Escribir "su numero mas grande es: ", grande
FinAlgoritmo
