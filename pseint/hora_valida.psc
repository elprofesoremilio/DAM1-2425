Algoritmo hora_valida
	Escribir "Indica hora, minutos y segundos: "
	Leer h,m,s
	Si h>=0 Entonces
		Si h<=23 Entonces
			Si m>=0 Entonces
				Si m<=59 Entonces
					Si s>=0 Entonces
						Si s<=59 Entonces
							Escribir "OK"
						SiNo
							Escribir "Error en los segundos"						
						FinSi
					SiNo
						Escribir "Error en los segundos"						
					FinSi
				SiNo
					Escribir "Error en los minutos"
				FinSi
			SiNo
				Escribir "Error en los minutos"
			FinSi
		SiNo
			Escribir "Error en la hora"
		FinSi
	SiNo
		Escribir "Error en la hora"
	FinSi
FinAlgoritmo
