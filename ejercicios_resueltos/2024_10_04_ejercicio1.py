print("Hola, buenas tardes.")
nombre = input("Introduce tu nombre, por favor: ")
apellidos = input("Introduce tus apellidos, por favor: ")
sexo = input("Introduce tu sexo, por favor: ")
edad = input("Introduce tu edad, por favor: ")

# Forma larga
print()
print("Nombre:\t" + apellidos + ", " + nombre)
print("Sexo:\t" + sexo)
print("Edad:\t" + edad)

# Forma corta
print(f"\n\nNombre:\t{apellidos}, {nombre}\nSexo:\t{sexo}\nEdad:\t{edad}")