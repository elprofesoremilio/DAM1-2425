Algoritmo hora_valida3
	Escribir 'Indica hora, minutos y segundos: '
	Leer h, m, s
	Si h>=0 y h<=23 Entonces
		Si m>=0 y m<=59 Entonces
			Si s>=0 y s<=59 Entonces
				Escribir 'Formato correcto'
			SiNo
				Escribir 'Error en los segundos'
			FinSi
		SiNo
			Escribir 'Error en los minutos'
		FinSi
	SiNo
		Escribir 'Error en la hora'
	FinSi
FinAlgoritmo