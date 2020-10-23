 #programacion orientada a objetos

class Dog: #Clase plantilla-tipo-Dog
    def __init__(self, name, age): #metodo (es una funcion de una clase)
        self.name = name #atributo para Dog que es name
        self.age = age 

    def add_one(self, x): #metodo
        return x + 1

    def get_age(self):
        return self.age

    def bark(self):
        print("bark") 


d = Dog("Tim", 10)
d2 = Dog("Bill", "11")

print (d.name, d.age)

# cada vez que creamos un objeto Dog, se inicia con self y 
# le pasaremos un parametro que contenerá name 
