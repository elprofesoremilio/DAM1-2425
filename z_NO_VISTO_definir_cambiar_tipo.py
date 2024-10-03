# En algunos casos podemos pasar de un tipo a otro usando funciones
# CUIDADO: si tratamos de convertir datos incompatibles terminará el programa con una excepción
#   pasar a entero
entero1 = int("13")
entero2 = int(1.3)
#   pasar a float
real1 = float(entero)
real2 = float("2.5")
#   pasar a texto
texto1 = str(entero1)
texto2 = str(real1)
texto3 = str(True)
#   pasar a lógico (booleano)
logico1 = bool(entero)
logico2 = bool("False")