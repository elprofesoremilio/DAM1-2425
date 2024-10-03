# Una variable es como una caja donde guardamos algo
# A cada caja que creamos debemos darle un nombre

# El formato es: nombre_variable = literal
# Se considera un literal un valor fijo, invariable, escrito de una forma concreta
# y de un tipo concreto --> número, carácter, texto, lógico, ...

numero = 12  # Literal 12, es un número entero
nombre = "Juan"  # Literal "Juan", escrito entre comillas, indica que es un texto

# Para crear una variable hay que escribir su nombre y darle valor con =
# El nombre de una variable debe cumplir:
#   - solo contiene letras, guion bajo y/o números
variable = 1
#   - debe ser lo más significativo y legible posible
asdf = 23       # esto no me dice nada
edad = 23       # ya me da más información
#   - para escribir varias palabras en el nombre de una variable
fechaDeNacimiento = 12       # camel case
fecha_de_nacimiento = 12     # snake case --> así es como se ha decidido que se haga en python
#   - casos excepcionales: primer carácter del nombre
#       * no se debe empezar por mayúscula
#       * no se debe empezar por _
#       * no se puede empezar por número

# Existen 6 tipos de valores posibles que se asignan en función del valor asignado
# A continuación hay ejemplos de cómo declarar los distintos tipos y sus posibles literales
# # ENTERO → int → números enteros
entero = 1
# # REAL -> float -> números reales (con decimales . y exponenciales e10)
real = 1.3
otro_real = 1.3e3   # 1.3 * 10^3  --> 1300
otro_real_mas = 1e10
# # STRING o TEXTO → str -≥ siempre deben estar entre comillas
texto = "Esto es un texto entre comillas dobles"
otro_texto = 'También puede ir entre comillas simples'
# Aquí el valor literal no es 23, es "23", quiere decir que es un texto
# Nunca será tratado como un número a no ser que hagamos algo al respecto
texto_final = "23"
# # BOOLEAN o LÓGICO -> bool -> True o False
logico_verdadero = True
logico_falso = False

# # Existen dos valores especiales más, que son listas y tuplas y que ya veremos posteriormente