pc_en_stock = input("Introduzca los PC que hay en el almacén: ")
aulas_a_montar = input("Introduzca las aulas que hay que montar: ")
pc_por_aula = input("Introduzca los PC que se necesitan en cada aula: ")

pc_por_aula = int(pc_por_aula)
pc_en_stock = int(pc_en_stock)
aulas_a_montar = int(aulas_a_montar)

aulas_que_puedo_montar = pc_en_stock // pc_por_aula
print(f"Puedo montar {aulas_que_puedo_montar} aulas.")

pc_a_pedir = (aulas_a_montar * pc_por_aula) - pc_en_stock
print(f"Tengo que pedir {pc_a_pedir} ordenadores.")