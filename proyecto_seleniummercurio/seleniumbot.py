import trafilatura
import re
import os
import wget
from time import sleep

                                                                #las paginas estan en año/mes/dia/cuerpo
                                                                #CUERPOS: A,B,C,domingo(E)

downloaded = trafilatura.fetch_url("https://digital.elmercurio.com/2020/10/28/A")
trafilatura.extract(downloaded)

print(downloaded.encode("utf8"), file=open('output.txt', 'a'))  #Print hacia un archivo

pagina = open("output.txt","r",encoding="utf-8").read()         #Abre el archivo
encontrar = re.findall(r'data-src-retina="https://merreader.emol.cl/2020/10/28/content/pages/img/big/.*?jpg', pagina)    #regex
print(encontrar)
for encontrado in encontrar:                                           #por cada regex encontrado
    encontrado = encontrado.strip('data-src-retina="')                      #le saca la parte que no funciona en wget
    image_url = encontrado                                            #transforma cada link en link para descargar
    image_filename = wget.download(image_url, out=r'.\A')       #descarga con wget desde link disponible en image_url
    sleep(5)
    print('Se descargo la imagen: ', image_filename)
    print(encontrado)

os.remove("output.txt")
