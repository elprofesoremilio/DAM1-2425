largo = int(input("Introduzca la cantidad de baldosas para el largo de la habitación: "))
ancho = int(input("Introduzca la cantidad de baldosas para el ancho de la habitación: "))

total_baldosas = ancho * largo

negras = total_baldosas//2
if total_baldosas%2==0:
    blancas = negras
else:
    blancas = negras + 1

print(blancas, negras)

############################
negras = total_baldosas//2
blancas = negras + (total_baldosas%2)
print(blancas, negras)

############################
negras = total_baldosas//2
blancas = total_baldosas-negras
print(blancas, negras)
