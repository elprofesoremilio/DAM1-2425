jugador_a = int(input("Di un número para elegir: "))

if jugador_a%2 == 0:
    jugador_a = "pares"
else:
    jugador_a = "nones"

suma_de_manos = int(input("Mano 1 jugador A"))
suma_de_manos += int(input("Mano 2 jugador A"))
suma_de_manos += int(input("Mano 1 jugador B"))
suma_de_manos += int(input("Mano 2 jugador B"))

if suma_de_manos%2 == 0:
    suma_de_manos = "pares"
else:
    suma_de_manos = "nones"

if suma_de_manos == jugador_a:
    print("Gana jugador A")
else:
    print("Gana jugador B")