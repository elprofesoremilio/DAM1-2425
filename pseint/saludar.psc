Algoritmo saludar
	Leer hora
	Si hora>=5 y hora<=12  Entonces
		Escribir "Buenos días"
	SiNo
		Si hora>12 y hora<=20 Entonces
			Escribir "Buenas tardes"
		SiNo
			Si no (hora > 24) Entonces
				Escribir "Buenas noches"
			SiNo
				Escribir "Error"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
