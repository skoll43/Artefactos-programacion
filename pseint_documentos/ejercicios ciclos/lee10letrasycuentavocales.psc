Algoritmo sin_titulo
	cantidad = 0
	Escribir "Este programa lee 10 letras"
	Escribir "Ingrese una letra"
	Para i<-1 Hasta 10 Hacer
		Leer letra
		Escribir "ingrese otra letra"
		Segun letra Hacer
			"a" o "A":
				cantidad = cantidad + 1
			"e" o "E":
				cantidad = cantidad + 1
			"i" o "I":
				cantidad = cantidad + 1
			"o" o "O":
				cantidad = cantidad + 1
			"u" o "U":
				cantidad = cantidad + 1
			De Otro Modo:
				cantidad = cantidad + 0
		FinSegun
	FinPara
	Escribir "digitó ", cantidad, " vocales"
FinAlgoritmo
