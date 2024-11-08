def dividir(dividendo, divisor):
    # Probamos que con los datos dados se puede dividir y si no, lo indico por pantalla
    try:
        result = dividendo / divisor
        return result
    except ZeroDivisionError:
        return None

# Solicito por teclado los datos necesarios
operando1 = int(input("Dividendo: "))
operando2 = int(input("Divisor: "))

resultado = dividir(operando1, operando2)

# Si el resultado es None significa que no se ha podido dividir
if resultado is None:
    print("No se pudo calcular el resultado porque no se puede dividir por 0.")
# Se ha podido dividir por lo que escribo el resultado
else:
    print(resultado)