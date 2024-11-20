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
negro = (0, 0, 0)

# Configurar el reloj para controlar los FPS
fps = 60
reloj = pygame.time.Clock()

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

    # Verifica si se ha pulsado una tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        barra_x += barra_velocidad
    if keys[pygame.K_LEFT]:
        barra_x -= barra_velocidad

    # Rellenar el fondo
    pantalla.fill(blanco)

    # Dibujar barra
    posicion_barra = (barra_x, barra_y, barra_ancho, barra_alto)
    pygame.draw.rect(pantalla,negro,posicion_barra)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    reloj.tick(fps)

# Fuera del bucle
# Salir del programa
pygame.quit()
sys.exit()