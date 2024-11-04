nombre = input("Nombre del cliente: ")
numero = int(input("Número de medicamentos: "))
suma = 0

while numero>0:
    precio = int(input("Precio del medicamento: "))
    suma += precio
    numero -= 1

print(f"{nombre} debe {suma}€")

