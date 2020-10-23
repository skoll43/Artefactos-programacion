#14. Crear un programa que Imprima
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWX
#ABCDEFGHIJKLMNOPQRSTUV
#ABCDEFGHIJKLMNOPQRST
#ABCDEFGHIJKLMNOPQR
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(string)
while True:
    string = string[:-1]
    print(string)
    if len(string) == 2:
        break