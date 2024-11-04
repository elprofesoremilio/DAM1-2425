Algoritmo sin_titulo
	Escribir "Introduzca día, mes y año: "
	Leer day, month, year
	Si day >= 1 Entonces
		Si month == 1 Entonces
			Si day <= 31 Entonces
				Escribir "OK"
			SiNo
				Escribir "ERR"
			FinSi
		SiNo
			Si month == 2 Entonces
				Si day <= 28 Entonces
					Escribir "OK"
				SiNo
					Escribir "ERR"
				FinSi
			SiNo
				Si month == 3 Entonces
					Si day <= 31 Entonces
						Escribir "OK"
					SiNo
						Escribir "ERR"
					FinSi
				SiNo
					Si month == 4 Entonces
						Si day <= 30 Entonces
							Escribir "OK"
						SiNo
							Escribir "ERR"
						FinSi
					SiNo
						Si month == 5 Entonces
							Si day <= 31 Entonces
								Escribir "OK"
							SiNo
								Escribir "ERR"
							FinSi
						SiNo
							Si month == 6 Entonces
								Si day <= 30 Entonces
									Escribir "OK"
								SiNo
									Escribir "ERR"
								FinSi
							SiNo
								Si month == 7 Entonces
									Si day <= 31 Entonces
										Escribir "OK"
									SiNo
										Escribir "ERR"
									FinSi
								SiNo
									Si month == 8 Entonces
									
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
