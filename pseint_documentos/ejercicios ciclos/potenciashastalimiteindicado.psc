Algoritmo sin_titulo
	Escribir 'Ingrese su numero'
	Leer N
	Escribir 'Ingrese un limite'
	Leer limite
	Repetir
		Para i<-1 Hasta limite Hacer
			po <- N^i
			Escribir 'potencia ',i,' de ',N,' = ',po
		FinPara
	Hasta Que po>limite
	Escribir 'No hay mas potencias de ',N
	Escribir 'que superen el limite indicado'
	Escribir ' limite indicado: (',limite,') '
FinAlgoritmo
