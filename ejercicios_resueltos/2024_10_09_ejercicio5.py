IVA = 21/100
base_imponible = float(input("Introduzca la base imponible (precio sin iva)"))
precio_venta = base_imponible + (base_imponible*IVA)
print("El precio total es:",precio_venta)