Algoritmo hora_valida2
	Escribir 'Indica hora, minutos y segundos: '
	Leer h, m, s
	Si h>=0 y h<=23 y m<=59 y m>=0 y s<=59 y s>=0 Entonces
		Escribir "Correcta"
	SiNo
		Escribir 'Incorrecta'
	FinSi
FinAlgoritmo
