Algoritmo sin_titulo
	Escribir 'cuentaceros en numeros de 5 cifras'
	Escribir 'NO COMENZAR POR 0'
	Escribir 'escriba primer numero'
	cuantos <- 0
	Leer num1
	Escribir 'escriba segundo numero'
	Leer num2
	Si num2=0 Entonces
		cuantos <- cuantos+1
	FinSi
	Escribir 'escriba tercer numero'
	Leer num3
	Si num3=0 Entonces
		cuantos <- cuantos+1
	FinSi
	Escribir 'escriba cuarto numero'
	Leer num4
	Si num4=0 Entonces
		cuantos <- cuantos+1
	FinSi
	Escribir 'escriba quinto numero'
	Leer num5
	Si num5=0 Entonces
		cuantos <- cuantos+1
	FinSi
	Si num1 = 0 Entonces
		Escribir "No puede ser 0 el primer numero"
		Escribir "cambie el primer numero"
		Leer num1
		Mientras num = 0 Hacer
			Escribir ".-."
		FinMientras
	SiNo
		Escribir 'Tiene ',cuantos,' ceros'
	FinSi
FinAlgoritmo

Funcion SinTitulo
	
FinFuncion
