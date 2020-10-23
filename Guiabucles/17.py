#17. Encontrar, imprimir y contar todos los números de 4 dígitos que cumplen con la
#condición de que la suma de sus dígitos de 9. Hasta 10000.
contador = 0
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if i + j + k + l == 9:
                    print(i,j,k,l)
                    contador = contador + 1
                    print(contador)