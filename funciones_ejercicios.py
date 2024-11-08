def es_primo(numero):
    divisor = 2
    while numero % divisor != 0:
        divisor += 1

    if divisor!=numero:
        return False
    else:
        return True

    # return divisor==numero

def suma(a,b):
    return a + b

def es_par(numero):
    if numero%2==0:
        return True
    else:
        return False

def celsius_a_farenheit(grados_celsius):
    resultado = (grados_celsius * (9/5))+32
    return resultado