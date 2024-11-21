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
azul = (0,0,255)
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

# Configuración del ladrillo

ladrillos = []

ladrillos.append([300,200,50,10,True])
ladrillos.append([355,200,50,10,True])
ladrillos.append([410,200,50,10,True])
ladrillos.append([465,200,50,10,True])
ladrillos.append([245,200,50,10,True])
ladrillos.append([190,200,50,10,True])
ladrillos.append([135,200,50,10,True])
ladrillos.append([80,200,50,10,True])
ladrillos.append([25,200,50,10,True])

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
    barra_posicion = (barra_x, barra_y, barra_ancho, barra_alto)
    pygame.draw.rect(pantalla, negro, barra_posicion)

    for ladrillo in ladrillos:
        # Dibujar ladrillo
        if ladrillo[4]:
            ladrillo_posicion = (ladrillo[0],ladrillo[1],ladrillo[2],ladrillo[3])
            pygame.draw.rect(pantalla, azul, ladrillo_posicion)

    # Actualizar barra
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        barra_x += barra_velocidad
    if keys[pygame.K_LEFT]:
        barra_x -= barra_velocidad

    # Compruebo ladrillo
    for ladrillo in ladrillos:
        # Dibujar ladrillo
        if ladrillo[4]:
            if (pelota_x+pelota_radio >= ladrillo[0]) and (pelota_x-pelota_radio <= ladrillo[0] + ladrillo[2]):
                if ladrillo[1] <= pelota_y + pelota_radio <= ladrillo[1] + ladrillo[3]:
                    ladrillo[4] = False
                    pelota_velocidad_y = -pelota_velocidad_y

    # Actualizar pelota
    pelota_x += pelota_velocidad_x
    pelota_y += pelota_velocidad_y

    if (pelota_x+pelota_radio >= barra_x) and (pelota_x-pelota_radio <= barra_x + barra_ancho):
        if barra_y <= pelota_y + pelota_radio <= barra_y + barra_alto :
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