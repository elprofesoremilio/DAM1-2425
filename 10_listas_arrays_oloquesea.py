# Declarar una variable como lista/array vacío
array = []
print(array)

# Declarar un array con valores
array = [7,2,8,9,3,1,9]

# Modificar una posición concreta del array
array[2] = 10
array[5] = 10

# Acceder para consultar una posición concreta del array
print(array[2])

# De esto nos vamos a olvidar por ahora
print(array[2:5])

try:
    print(array[9])
except IndexError:
    print("Te has pasado")

i = 0
suma = 0
while i<len(array):   # len me devuelve el tamaño (lenth de longitud) del array
    suma = suma + array[i]
    i += 1

media = suma/6
print(media)

# Añadir elementos a la lista
array.append(0)
array.append(8)

print(array)
print(len(array))

# Llenar un array desde cero hasta que el usuario meta un 0
array_cero = []

# Este bucle introducirá el cero último SIEMPRE
numero = -1
while numero!=0:
    numero = int(input("Dime un número (0 para salir): "))
    array_cero.append(numero)

print(array_cero)

# Solución 1
numero = -1
array_uno = []
while numero!=0:
    numero = int(input("Dime un número (0 para salir): "))
    if numero!=0:
        array_uno.append(numero)

print(array_uno)

# Solución 2 y más efectiva: PRELECTURA
array_dos = []
numero = int(input("Dime un número (0 para salir): "))
while numero!=0:
    array_dos.append(numero)
    numero = int(input("Dime un número (0 para salir): "))

print(array_dos)
# Con conversión de tipos
array_tres = []
numero = input("Dime un número (fin para salir): ")
while numero!="fin":
    array_tres.append(int(numero))
    numero = input("Dime un número (fin para salir): ")

print(array_tres)

