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

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Rellenar el fondo
    pantalla.fill(blanco)

    # Dibujar un círculo
    centro = (ancho // 2, alto // 2)
    radio = 50
    pygame.draw.circle(pantalla, naranja, centro, radio)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    reloj.tick(fps)

# Fuera del bucle
# Salir del programa
pygame.quit()
sys.exit()