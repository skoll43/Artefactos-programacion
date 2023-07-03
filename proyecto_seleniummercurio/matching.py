#import re
#pagina = open("output.txt","r",encoding="utf-8").read()


#otrocosa = re.findall(r'data-src-retina=.*?jpg', pagina)#regex arcano q no entiendo pero funciona
#print(otrocosa)
#for mani in otrocosa:
#    mani = mani.strip('data-src-retina="')
#    print(mani)

from datetime import date

''''cuerpo = ["/A","/B","/C","/E"]

n = 0

d=date.today()
d=str(d).replace("-","/")
d=d + cuerpo[n]
print(d)
d=d.strip(cuerpo[(n)])
print(d)
n +=1
d=d + cuerpo[(n)]
print(d)
'''
import trafilatura
import re
import os
import wget
from time import sleep
                                                                #las paginas estan en año/mes/dia/cuerpo
                                                                #CUERPOS: A,B,C,E


n = 0
cuerpo = ["/A","/B","/C","/E"]
d=date.today()
d=str(d).replace("-","/")
d.encode("utf-8")

while n != 4:
    
    d=d + cuerpo[n]
    link=str(r"https://digital.elmercurio.com/"+d)
    
    print(link)
    downloaded = trafilatura.fetch_url(link)
    sleep(1)
    trafilatura.extract(downloaded)
    sleep(1)
    print(downloaded.encode('utf-8'), file=open('output.txt', 'a'))  #Print hacia un archivo
    sleep(1)
    pagina = open("output.txt","r",encoding="utf-8").read()         #Abre el archivo
    sleep(1)
    otrocosa = re.findall(r'data-src-retina=.*?jpg', pagina)
    sleep(1)                                                       #regex arcano q no entiendo pero funciona
    for mani in otrocosa:                                           #por cada regex encontrado
        mani = mani.strip('data-src-retina="')                      #le saca la parte que no funciona en wget
        image_url = mani                                            #transforma cada link en link para descargar
        image_filename = wget.download(image_url, out=r".\A")       #descarga con wget desde link disponible en image_url
        sleep(10)
        print('Image Successfully Downloaded: ', image_filename)
        sleep(1)
        print(mani)
        sleep(1)
    os.remove("output.txt")
    sleep(10)
    d=d.strip(cuerpo[(n)])
    sleep(10)
    n = n + 1
    
    