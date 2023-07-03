from random import shuffle  

a = ["Lukas", "Lukas", "Gerson","Gerson", "Acxel","Acxel", "Javier", "Javier"]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(b)
uncombinao = list(zip(a, b))
a[:], b[:] = zip(*uncombinao)

print(uncombinao)
input()