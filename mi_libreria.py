# Uso de parámetros por defecto
def input_int(texto="Introduce un número entero: "):
    lectura_incorrecta = True
    numero = None
    while lectura_incorrecta:
        try:
            numero = int(input(texto))
            lectura_incorrecta = False
        except ValueError:
            print(f"Número introducido incorrecto, pruebe otra vez.")
    return numero

def input_float(texto="Introduce un número flotante: "):
    lectura_incorrecta = True
    numero = None
    while lectura_incorrecta:
        try:
            numero = float(input(texto))
            lectura_incorrecta = False
        except ValueError:
            print(f"Número introducido incorrecto, pruebe otra vez.")

    return numero