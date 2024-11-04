Algoritmo deuda
	Escribir "Introduce el nombre: "
	Leer nombre
	Escribir "Introduce el número de medicamentos fiados: "
	Leer n
	suma = 0
	Mientras n>0 Hacer
		Escribir "Precio del medicamento fiado: "
		Leer precio
		suma = suma + precio
		n = n-1
	FinMientras
	Escribir concatenar(concatenar(nombre,concatenar(" debe ", convertiratexto(suma)))," euros.")
FinAlgoritmo
