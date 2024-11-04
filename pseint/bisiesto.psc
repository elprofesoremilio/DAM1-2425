Algoritmo bisiesto
	Escribir "Escribe un año: "
	Leer year
	Si year % 4 == 0 Entonces
		Si no (year % 100 == 0) Entonces
			Escribir "Es bisiesto."
		SiNo
			Si year % 400 == 0 Entonces
				Escribir "Es bisiesto"
			SiNo
				Escribir "No es bisiesto"
			FinSi
		FinSi
	SiNo
		Escribir "No es bisiesto"
	FinSi
FinAlgoritmo
