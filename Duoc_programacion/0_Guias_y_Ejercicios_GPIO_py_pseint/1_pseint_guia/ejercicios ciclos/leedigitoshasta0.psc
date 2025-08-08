Algoritmo sin_titulo
	Escribir 'ingrese digitos, ingrese 0 para salir'
	Repetir
		Leer num
		Si num=0 Entonces
			Escribir 'ingresó ',cpares,' numero(s) par(es)'
			Escribir 'el promedio de los impares es: ',pimpares
			Escribir "el mayor numero de todos los ingresados "
			Escribir "es el numero: ',elmayor
		SiNo
			Escribir 'el siguiente digito'
			Si num>elmayor Entonces
				elmayor <- num
			SiNo
				Escribir lista_de_expresiones
			FinSi
			Si num MOD 2=0 Entonces
				cpares <- cpares+1
			SiNo
				cimpares <- cimpares + 1
				sumaimpares <- sumaimpares + num
				pimpares <- sumaimpares / cimpares
			FinSi
		FinSi
	Hasta Que num=0
FinAlgoritmo
