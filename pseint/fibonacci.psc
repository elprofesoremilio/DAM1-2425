Algoritmo fibonacci
	numero0 = 0
	numero1 = 1
	resultado = convertiratexto(numero0)
	resultado = concatenar(resultado,",")
	resultado = concatenar(resultado,convertiratexto(numero1))
	Escribir "N�mero de veces: "
	Leer veces
	Si veces>2 Entonces
		veces = veces - 2
		Mientras veces>0 Hacer
			siguiente = numero0+numero1
			numero0 = numero1
			numero1 = siguiente
			veces = veces - 1
			resultado = concatenar(resultado,concatenar(",",convertiratexto(siguiente)))
		FinMientras
	SiNo
		Escribir "N�mero de ejecuciones bajo, indicamos resultado solo para el paso base"
	FinSi
	Escribir resultado
FinAlgoritmo
