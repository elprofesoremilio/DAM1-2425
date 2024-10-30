# TODO poner comentarios en todo el ejercicio

primer_extremo = int(input("Número de un extremo: "))
segundo_extremo = int(input("Número del otro extremo: "))

if primer_extremo > segundo_extremo:
      aux = primer_extremo
      primer_extremo = segundo_extremo
      segundo_extremo = aux

if primer_extremo % 2 == 0 and primer_extremo+1 == segundo_extremo:
      print("SI")
else:
      print("NO")