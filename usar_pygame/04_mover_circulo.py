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

# Configurar el reloj para controlar los FPS
fps = 60
reloj = pygame.time.Clock()

# Posición actual del círculo
radio_x = ancho//2
radio_y = alto//2

# Velocidad de movimiento
velocidad_x = 2
velocidad_y = 0

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Rellenar el fondo
    pantalla.fill(blanco)

    # Dibujar un círculo
    centro = (radio_x, radio_y)
    radio = 50
    pygame.draw.circle(pantalla, naranja, centro, radio)

    # Sumar velocidad
    radio_x += velocidad_x
    radio_y += velocidad_y

    if radio_x > ancho + radio:
        radio_x = 0 - radio

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    reloj.tick(fps)

# Fuera del bucle
# Salir del programa
pygame.quit()
sys.exit()