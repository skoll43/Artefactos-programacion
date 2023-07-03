from random import shuffle  
a = ["Lukas", "Gerson","Axcel"]
b = [1, 2, 3]
shuffle(b)
uncombinao = list(zip(a, b))
# a[:], b[:] = zip(*uncombinao)
print(uncombinao)
[('Lukas', 3), ('Gerson', 2), ('Axcel', 1)]
