Algoritmo sin_titulo
	// Hacer un programa para calcular el valor
	// de la suma de los N primeros enteros. 
	// Por ejemplo si N es 5 la suma es 15 
	// ( 1 + 2 + 3 + 4 + 5 = 15)    
	// Num pj 5
	Repetir
		Leer num
		suman <- suman+num-(anterior)
		anterior <- anterior-num+1
		Escribir 'Su numero - ','(',anterior,')',' = ',suman
	Hasta Que anterior=0
	Escribir 'la suma de los n° anteriores de su n° resulta en ',suman
FinAlgoritmo
