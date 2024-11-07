from mi_libreria import input_int

def suma(op1, op2):
    return op1 + op2

def dividir(dividendo,divisor):
    # Inicializo la variable a None, por si no obtengo resultado
    resultado = None
    # Probamos que con los datos dados se puede dividir y si no, lo indico por pantalla
    try:
        resultado = dividendo / divisor
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    return resultado

# Solicito por teclado los datos necesarios
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
resultado = dividir(dividendo,divisor)
# Si el resultado es None significa que no se ha podido dividir
if resultado is None:
    print("No se pudo calcular el resultado.")
# Se ha podido dividir por lo que escribo el resultado
else:
    print(resultado)