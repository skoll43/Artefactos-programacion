Algoritmo sin_titulo
	salir = 0
	// Desarrolle un algoritmo que permita a un usuario ingresar letras hasta que decida salir del
	// programa y finalmente muestre cuantas letras ingreso.
	Escribir "Este programa cuenta letras"
	Escribir "Escriba salir para terminar el programa"
	cuenta = -1
	Repetir
		Si letra = "salir" Entonces
			salir = 1
		SiNo
			cuenta = cuenta + 1
			Leer letra
		FinSi
	Hasta Que salir = 1
	Escribir "Usted ingresó ", cuenta, " letras"
FinAlgoritmo
