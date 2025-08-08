Algoritmo sin_titulo
	num <- 1000
	Repetir
		num <- num+1
		uni <- num MOD 10
		dec <- num MOD 100
		Si dec = 1 Entonces
			dec = 0
		FinSi
		cen <- num MOD 1000
		Si cen = 1 Entonces
			cen = 0
		FinSi
		umi = num mod 10000
		pri = uni
		seg = (dec - uni) / 10
		ter = (cen - dec) / 100
		cua = (umi - cen) / 1000
		suma = pri + seg + ter + cua
		Si suma=9 Entonces
			Escribir num
			cuenta <- cuenta+1
		FinSi
		pri <- 0
		seg <- 0
		ter <- 0
		cua <- 0
		suma <- 0
	Hasta Que num=10000
	Escribir cuenta,' numeros tienen digitos que suman 9'
FinAlgoritmo
