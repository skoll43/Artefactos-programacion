import pylightxl as xl
from tkinter import *
import tkinter as tk


# root window
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():  
    x1 = entry1.get()
    
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)
    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
""""
root = Tk() #inicia
root.withdraw()  #oculta parte del programa
root.attributes('-topmost', True) #muestra por encima de otros
file = filedialog.askopenfilename() #pide finalmente abrir un archivo 

#db = xl.readxl(fn=file,ws=("Reporte Logistico"))
db = xl.readxl(fn=file,ws=("Sheet1")) #database que se lee de un archivo elegido, con la hoja
hoja = db.ws("Sheet1").col(1) #verifica la primera columna
cont=0 #inicia contador 
for cell in hoja: #cada celda
    cont = cont + 1 #cuenta uno
    if cell == "lukas": 
        print(cont)
        print(db.ws("Sheet1").row(row=cont))

    continue



"""