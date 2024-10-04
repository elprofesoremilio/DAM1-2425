
# Existen funciones que además de ejecutar su código, también nos dan un resultado
# Ese resultado se puede asignar a una variable o utilizar como parámetro de otra función
# FUNCIÓN input
# Sirve para obtener datos desde el teclado: input devuelve el texto que escribamos
# hasta que pulsemos ENTER.
input()
# En el caso anterior, por un lado la pantalla se queda esperando pero
# nosotros podemos no saber que hacer porque no se nos dan instrucciones
# Por otro lado el texto se pierde porque no lo guardamos
# Si no queremos que este texto se pierda, lo debemos guardar en una variable
nombre = input("Escribe tu nombre: ")

# Como ves podemos también indicar un texto que se escribirá al solicitar el dato

# Ten en cuenta que input siempre devuelve texto (string)
# Si queremos leer números deberemos convertirlos con las funciones que vimos
edad = input("Escribe tu edad: ")
edad = int(edad) # fíjate cómo cambiamos el tipo de la variable sin problemas

# Para finalizar, lo escribimos junto de una forma nueva, en la que poniendo
# una f al principio del parámetro de print podemos juntar texto y variables como sigue:
print(f"Nombre: {nombre}\nEdad: {edad}")

###########################################################################
###########################################################################
###########################################################################

# Explicación del funcionamiento de input

variable = input("Escribe algo: ")
#   1.  El compilador encuentra una expresión de asignación
#       así que descompone en expresiones más pequeñas:
#       - variable
#       - input("Escribe algo: ")
#   2.  El compilador determina que la primera expresión es una variable
#       válida así que la crea
#   3.  Como es una asignación, el compilador trata de asignarle el valor
#       de input("Escribe algo: ") pero para ello necesita ejecutar esa
#       función por lo que empieza a ejecutarla
#       a. Muestra por pantalla el texto 'Escribe algo: '
#       b. Espera a que el usuario introduzca texto por teclado y pulse ENTER
#   4.  Una vez pulsado ENTER, el compilador sustituye la expresión input("Escribe algo: ")
#       por el valor que el usuario ha introducido por teclado quedando finalmente una
#       expresión del tipo:
#           variable = "lo que has escrito por teclado"
#   5.  Termina de ejecutar esa expresión de asignación dando a variable el valor
#       introducido por teclado.
