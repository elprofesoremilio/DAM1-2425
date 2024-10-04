# En este caso vamos a decirle al usuario que nos de la velocidad y la distancia
# en vez de poner valores fijos. Así es más reutilizable el código.
velocidad = input("Introduzca la velocidad (número sin decimales, por favor): ")
velocidad = int(velocidad)
distancia = int(input("Introduzca el tiempo (número sin decimales, por favor): "))
tiempo = distancia / velocidad

# Escribimos el resultado de varias formas aunque todas muestran por pantalla exactamente lo mismo
print("Tiempo en recorrer", distancia, "km a", velocidad, "Km/h:",tiempo,"horas")
print("Tiempo en recorrer " + str(distancia) + " km a " + str(velocidad) + " Km/h: " + str(tiempo) +" horas")
print(f"Tiempo en recorrer {distancia} Km a {velocidad} Km/h: {tiempo} horas")
