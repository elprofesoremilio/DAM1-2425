# Funciones: dos partes --> cabecera y cuerpo

# Cabecera --> puede o no tener parámetros
def fibonacci(repeticiones):
# Cuerpo --> código a ejecutar
    primero = 0
    segundo = 1
    resultado = str(primero) + "," + str(segundo)

    if repeticiones>=2:
        repeticiones -= 2
        while repeticiones>0:
            siguiente = primero + segundo
            primero = segundo
            segundo = siguiente
            repeticiones -= 1
            resultado += "," + str(siguiente)
        print(resultado)
    else:
        print("Se requieren al menos 2 repeticiones.")

# Las funciones pueden o no devolver un valor


