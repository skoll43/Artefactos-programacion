
import sys

def emparejanotas():  
    for nota, valornota in zip(listaNota, listaValeNota):
        try: listaResultados.append(float(nota)*valornota)
        except:  atrapaLetras()   
            
listaValeNota = [0.25, 0.20, 0.20, 0.35]
listaNota = []
listaResultados = []

def atrapaLetras():
    print("Pon un numero po aweonao")
    sys.exit(1)

def preguntas():
    secuencia = ["primera","segunda","tercera","cuarta"]
    for palabra in secuencia:
            print("Escriba su", palabra,"nota parcial")
            listaNota.append(input())
    return emparejanotas()

preguntas()
print("Escriba su nota en el examen")
NotaExamen = float(input())
NotaFinal = ((sum(listaResultados))*0.60) + (NotaExamen *0.40)
print("Su nota final es",round(NotaFinal,ndigits=1))

print(listaNota, "notas")
print(listaResultados, "resultados multiplicados")