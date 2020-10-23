#18. Encontrar e imprimir todos los números de 4 dígitos que cumplan con la condición de
#aque la suma de los dígitos pares es igual a la suma de los dígitos impares.
cuentapares = 0
cuentaimpares = 0
for i in range(1,10):
    if i % 2 == 0:
        for j in range(0,10):
            if j % 2 == 0:
                for k in range(10):
                    if k % 2 == 0:
                        for l in range(10):
                            if l % 2 == 0:
                                pares = (i+j+k+l)
#                                dpares = i,j,k,l
                                cuentapares = cuentapares + 1
#                                print(pares)
                                for a in range(10):
                                    if a % 2 != 0:
                                        for b in range(10):
                                            if b % 2 != 0:
                                                for c in range(10):
                                                    if c % 2 != 0:
                                                        for d in range(10):
                                                            if d % 2 != 0:
                                                                impares = (a+b+c+d)
 #                                                               dimpares = a,b,c,d
                                                                cuentaimpares + cuentaimpares + 1
                                                                if pares == impares:
                                                                    print(i,j,k,l,pares,"=",a,b,c,d,impares)
                                                                    