total_days = int(input("Introduce el total de días: "))

years = total_days // 365
resto_dias = total_days % 365
meses = resto_dias // 30
dias = resto_dias % 30

print(f"{total_days} días son {years} años, {meses} meses y {dias} días.")
