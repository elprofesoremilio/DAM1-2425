cantidad_euros = float(input("Introduce el total de euros con decimales: "))

billete500 = cantidad_euros // 500
euros_restantes = cantidad_euros % 500
billete200 = euros_restantes // 200
euros_restantes = euros_restantes % 200
billete100 = euros_restantes // 100
euros_restantes = euros_restantes % 100
billete50 = euros_restantes // 50
euros_restantes = euros_restantes % 50
billete20 = euros_restantes // 20
euros_restantes = euros_restantes % 20
billete10 = euros_restantes // 10
euros_restantes = euros_restantes % 10
billete5 = euros_restantes // 5
euros_restantes = euros_restantes % 5
monedas1 = euros_restantes // 1
euros_restantes = euros_restantes % 1
centimos_restantes = euros_restantes * 100
monedas50c = centimos_restantes // 50
centimos_restantes %= 50
monedas20c = centimos_restantes // 20
centimos_restantes %= 20
monedas10c = centimos_restantes // 10
centimos_restantes %= 10
monedas5c = round(centimos_restantes // 5)
centimos_restantes %= 5
monedas2c = round(centimos_restantes // 2)
centimos_restantes %= 2
monedas1c = round(centimos_restantes)


print(monedas50c,monedas20c,monedas10c,monedas5c,monedas2c,monedas1c)