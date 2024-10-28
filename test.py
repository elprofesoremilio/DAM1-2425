from math import ceil

porcentaje_prime = int(input("Porcentaje (número entero) de pienso de calidad: "))
gramos_diarios = int(input("Cantidad de pienso diario que come el gato en gramos: "))

gramos_diarios_prime = (gramos_diarios * porcentaje_prime) / 100
gramos_diarios_normales = gramos_diarios - gramos_diarios_prime

gramos_semana_prime = gramos_diarios_prime * 7
sacos_prime = ceil(gramos_semana_prime / 250)

gramos_sobran_prime = (250 * sacos_prime) - gramos_semana_prime
gramos_prime_domingo = gramos_sobran_prime + gramos_diarios_prime

gramos_semana_normales = gramos_diarios_normales * 7
sacos_normales = ceil(gramos_semana_normales/8000)

gramos_sobran_normales = (8000*sacos_normales) - gramos_semana_normales
print("---------------------------------------")
print(f"Cantidad de calidad el domingo: {gramos_prime_domingo}"
      f"\nGramos normales que sobran: {gramos_sobran_normales}"
      f"\nSacos de calidad: {sacos_prime}"
      f"\nSacos normales: {sacos_normales}")