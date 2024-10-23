# Las estructuras condicionales van a ser el primer tipo de instrucciones
# de control de flujo del programa que vamos a ver
# Las estructuras condicionales permiten elegir entre dos o más
# bloques de código en función de que se cumpla o no una expresión lógica

# Para ejecutar o no una cosa
es_mayor_edad = False
edad = int(input("Introduce tu edad: "))

# Si edad>=18 Entonces
#   mayor_edad = Verdadero

if edad>=18:
    es_mayor_edad = True

# En las líneas anteriores aparece el concepto de bloque
# Un bloque en Python comienza con una instrucción de control de flujo del programa.
# Después es obligatorio incluir un tabulador en las instrucciones del bloque.
# Para terminar el bloque, se elimina la tabulación iniciada con la instrucción de control
print("Valor para mayor de edad:", es_mayor_edad)

# Para elegir entre dos cosas a ejecutar
if es_mayor_edad:
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
if not es_mayor_edad:
    if es_amigo:
        print("Puedes pasar")
    else:
        print("No puedes pasar")
else:
    print("Puedes pasar")

# Otra forma de hacer lo mismo
if es_amigo:
    print("Puedes pasar")
else:
    if es_mayor_edad:
        print("Puedes pasar")
    else:
        print("A tu casa")

# Ten en cuenta que estas construcciones son menos óptimas porque la condición
# es estadísticamente menos probable.
if es_mayor_edad:
    print("Puedes pasar")
else:
    if not es_amigo:
        print("No puedes pasar")
    else:
        print("Puedes pasar")

# Simplificando con condiciones compuestas
if es_mayor_edad or es_amigo:
    print("Puedes pasar")
else:
    print("No puedes pasar")

# Encadenar condiciones mutuamente excluyentes

dia_semana = int(input("Introduzca el día de la semana (1-7)"))

if dia_semana==1:
    print("Lunes")
elif dia_semana==2:
    print("Martes")
elif dia_semana==3:
    print("Miércoles")
elif dia_semana==4:
    print("Jueves")
elif dia_semana==5:
    print("Viernes")
elif dia_semana==6:
    print("Sábado")
elif dia_semana==7:
    print("Domingo")
else:
    print("Día incorrecto")

if dia_semana==6 or dia_semana==7:
    print("Festivo")
elif 1 <= dia_semana <=5:
# elif dia_semana>=1 and dia_semana<=5:
    print("Laborable")
else:
    print("No es un día válido")

# Inicializo una nueva variable para que no de error, puedeo ponerle el valor que sea
invita = False

if es_mayor_edad or (es_amigo and invita):
    print("Puedes pasar")
else:
    print("No puedes pasar")