# En algunos casos podemos pasar de un tipo a otro usando funciones
# CUIDADO: si tratamos de convertir datos incompatibles terminará el programa con una excepción

#   pasar a entero
entero1 = int("13")
entero2 = int(1.3)
#   pasar a float
real1 = float(entero1)
real2 = float("2.5")
#   pasar a texto
texto1 = str(entero1)
texto2 = str(real1)
texto3 = str(True)
#   pasar a lógico (booleano)
logic1 = bool(entero1)
logic2 = bool("False")

# Solo los números 0 se convierten como falso, el resto como verdadero
# Solo los textos que contienen cadena vacía convierten como falso, el resto como verdadero