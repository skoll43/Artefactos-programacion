#calculadora de vuelto para una compra 

print("Calcula el vuelto de la compra")

precio = int(input("Ingrese el precio: "))
paga = int(input("Ingrese con cuanto paga: "))


while paga < precio:  # Mientras el pago sea MENOR que el precio
    print("Error: El pago debe ser mayor o igual al precio")
    paga = int(input("Ingrese con cuanto paga: "))

vuelto = paga - precio

print("su vuelto es:", vuelto)