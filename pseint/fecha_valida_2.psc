Algoritmo fecha_valida_2
	Leer day, month, year
	Si year>=0 y month>=1 y month<=12 y day>=1 y day<=31 Entonces
		Si month==1 o month==3 o month==5 o month==7 o month==8 o month==10 o month==12 Entonces
			Escribir "OK"
		SiNo
			Si (month==4 o month==6 o month==9 o month==11) y day<=31 Entonces
				Escribir "OK"
			SiNo
				Si month==2 y day<=28 Entonces
					Escribir "OK"
				SiNo
					Escribir "ERR"
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "ERR"
	FinSi
FinAlgoritmo
