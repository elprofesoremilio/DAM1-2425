hora = int(input("Introduce la hora: "))
minutos = int(input("Introduce los minutos: "))

# resultado = hora - 8
#
# if resultado<0:
#       resultado += 24
#

resultado = (24 - 8 + hora) % 24

print(f"{resultado}:{minutos}")
