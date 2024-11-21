import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Dibujando un círculo con Pygame")

# Colores (RGB)
blanco = (255, 255, 255)
naranja = (255, 150, 0)
turquesa = (0,255,255)
negro = (0, 0, 0)
rojo = (255,0,0)

fondo = blanco

# Configurar el reloj para controlar los FPS
fps = 60
reloj = pygame.time.Clock()

# Configuración pelota
pelota_x = ancho // 2
pelota_y = alto // 2
pelota_velocidad_x = 5
pelota_velocidad_y = -5
pelota_radio = 25

# Configuración de la barra
barra_ancho = 100
barra_alto = 15
barra_x = ancho//2 - barra_ancho//2
barra_y = 550
barra_velocidad = 10

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Rellenar el fondo
    pantalla.fill(fondo)

    # Dibujar pelota
    centro = (pelota_x, pelota_y)
    pygame.draw.circle(pantalla, naranja, centro, pelota_radio)

    # Dibujar barra
    posicion_barra = (barra_x, barra_y, barra_ancho, barra_alto)
    pygame.draw.rect(pantalla,negro,posicion_barra)

    # Actualizar barra
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        barra_x += barra_velocidad
    if keys[pygame.K_LEFT]:
        barra_x -= barra_velocidad

    # Actualizar pelota
    pelota_x += pelota_velocidad_x
    pelota_y += pelota_velocidad_y

    if (pelota_x+pelota_radio >= barra_x) and (pelota_x-pelota_radio <= barra_x + barra_ancho):
        if pelota_y + pelota_radio >= barra_y:
            pelota_velocidad_y = -(abs(pelota_velocidad_y))

    if (pelota_x > ancho - pelota_radio) or (pelota_x - pelota_radio < 1):
        pelota_velocidad_x = -pelota_velocidad_x
    if pelota_y - pelota_radio < 1:
        pelota_velocidad_y = -pelota_velocidad_y
    if pelota_y - pelota_radio > alto:
        fondo = rojo

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    reloj.tick(fps)

# Fuera del bucle
# Salir del programa
pygame.quit()
sys.exit()