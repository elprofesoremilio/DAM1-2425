velocidad = input("Introduzca la velocidad (número sin decimales, por favor): ")
velocidad = int(velocidad)
distancia = int(input("Introduzca el tiempo (número sin decimales, por favor): "))
tiempo = distancia / velocidad

# Escribimos de varias formas lo mismo
print("Tiempo en recorrer", distancia, "km a", velocidad, "Km/h:",tiempo,"horas")
print("Tiempo en recorrer " + str(distancia) + " km a " + str(velocidad) + " Km/h: " + str(tiempo) +" horas")
print(f"Tiempo en recorrer {distancia} Km a {velocidad} Km/h: {tiempo} horas")
