from math import floor

dinero_padre = int(input("Cuánto dinero da el padre: "))
dinero_madre = 5

dinero_total = dinero_madre+dinero_padre
precio_kilo_peras = 5 / 3  # float

kilos_puedo_comprar = floor(dinero_total / precio_kilo_peras)

print("Compra",kilos_puedo_comprar,"kilos")

coste_total = int(kilos_puedo_comprar * precio_kilo_peras)

vuelta = dinero_total - coste_total

print("Devolver",vuelta, "euros.")