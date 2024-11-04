Algoritmo multiplos_entre_numeros
	Escribir "Números de inicio y fin: "
	multi = 9
	Leer inicio, final
	Mientras inicio <= final Hacer
		Si inicio mod multi == 0 Entonces
			Escribir inicio
			inicio = inicio + multi
		SiNo
			inicio = inicio + 1
		FinSi
	FinMientras
FinAlgoritmo
