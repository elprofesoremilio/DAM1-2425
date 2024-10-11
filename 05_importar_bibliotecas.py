# Importar una biblioteca sirve para usar funciones o variables
# que no aparecen en el Python estándar, por ejemplo,
# que hayamos construido nosotros

# La biblioteca math tiene muchas funciones y constantes útiles
# La puedo importar de 2 formas
otro_numero = 7

# No se debe hacer esto
# from math import pi
# pi = 13

# Si yo no hago el import anterior la siguiente asignación no afecta
pi = 5

from math import floor
import math

# Importo una libreria y la incluyo en mi namespace
from turtle import *

# Si no existe la libreria puedo instalarla desde una terminal con el siguiente comando
# pip install nombre_libreria
# Ojo, las librerias solo se instalan en la versión de python que estemos usando
# por defecto (en el PATH)

print(floor(math.pi))
print(floor(pi))

setup(450, 150, 0, 0)
screensize(300, 150)
goto(100, 0)
exitonclick()

numero = 3

# Para importar bibliotecas propias, ojo con las carpetas
# Se empieza a buscar desde la carpeta en la que está el archivo fuente
import libs.mensajes
print(libs.mensajes.mensaje_oficial)
