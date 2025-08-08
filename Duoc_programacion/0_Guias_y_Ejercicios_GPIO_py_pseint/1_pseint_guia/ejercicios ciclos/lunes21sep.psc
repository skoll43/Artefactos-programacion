Algoritmo sin_titulo
	Escribir 'Ingrese arancel anual'
	Leer ARANCELORIGINAL
	Escribir 'Forma de pago (1 o 10) '
	Leer FORMA
	// paga completo?
	Si FORMA=1 Entonces
		ARANCEL <- ARANCELORIGINAL-(ARANCELORIGINAL*0.10)
	FinSi
	// cuantos hermanos tiene?
	Escribir 'Tiene hermanos en la institucion? en numeros: ( 1, 2 o 3, etc)'
	Leer HERMANOS
	Si HERMANOS>=1 Entonces
		ARANCEL <- ARANCEL-(ARANCELORIGINAL*(0.05*HERMANOS))
	FinSi
	Escribir 'Su arancel será de ',ARANCEL
FinAlgoritmo
