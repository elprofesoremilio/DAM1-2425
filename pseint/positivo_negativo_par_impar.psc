Algoritmo positivo_negativo_par_impar
	Escribir "Escribe un n�mero: "
	Leer dato
	Si dato < 0 Entonces
		Escribir "Es negativo"
	SiNo
		Si dato > 0 Entonces
			Escribir "Positivo"
		SiNo
			Escribir "Cero"
		FinSi
	FinSi
	Si dato mod 2 = 0 Entonces
		Escribir "Par"
	SiNo
		Escribir "Impar"
	FinSi
FinAlgoritmo
