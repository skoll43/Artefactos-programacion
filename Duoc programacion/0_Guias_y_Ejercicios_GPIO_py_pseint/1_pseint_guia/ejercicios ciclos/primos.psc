Algoritmo detecta_num_primo
	num <- 1
	Repetir
		Para i<-1 Hasta num Hacer
			resto <- num MOD i
			Si resto=0 Entonces
				diviexacta <- diviexacta+1
			FinSi
		FinPara
		Si diviexacta=2 Entonces
			Escribir num,' esprimo'
		FinSi
		diviexacta <- 0
		num <- num+1
	Hasta Que num=1000
FinAlgoritmo
