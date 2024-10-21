# Las estructuras condicionales van a ser el primer tipo de instrucciones
# de control de flujo del programa que vamos a ver
# Las estructuras condicionales permiten elegir entre dos o más
# bloques de código en función de que se cumpla o no una expresión lógica

# Para ejecutar o no una cosa
mayor_edad = False
edad = int(input("Introduce tu edad: "))

# Si edad>=18 Entonces
#   mayor_edad = Verdadero

if edad>=18:
    mayor_edad = True

# En las líneas anteriores aparece el concepto de bloque
# Un bloque en Python comienza con una instrucción de control de flujo del programa.
# Después es obligatorio incluir un tabulador en las instrucciones del bloque.
# Para terminar el bloque, se elimina la tabulación iniciada con la instrucción de control
print("Valor para mayor de edad:",mayor_edad)

# Para elegir entre dos cosas a ejecutar
if mayor_edad:
    # Por cierto, puedes ver que he usado la variable booleana que hemos creado antes
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")


nombre = input("Introduce tu nombre.")

if nombre=="El trolas" or nombre=="Petete":
    es_amigo = True
else:
    es_amigo = False

# Podemos incluir condiciones dentro de condiciones
# A eso se le llama ANIDAR
if mayor_edad:
    if es_amigo:
        print("Puedes pasar")
    else:
        print("No puedes pasar")
else:
    print("Puedes pasar")

# Otra forma de hacer lo mismo
# Ten en cuenta que esta construcción es menos óptima porque la condición
# es estadísticamente menos probable.
if es_amigo:
    print("Puedes pasar")
else:
    if mayor_edad:
        print("Puedes pasar")
    else:
        print("A tu casa")



