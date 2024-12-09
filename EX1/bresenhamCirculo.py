#NOME: Victor Mariano Rocha

import pygame
import sys

# Função Principal
def bresenham(x_centro, y_centro, raio):
    x = 0
    y = raio
    delta = 3 - 2 * raio

    while x <= y:
        desenha(x_centro, y_centro, x, y)
        if delta < 0:
            delta = delta + 4 * x + 6
        else:
            delta = delta + 4 * (x-y) + 10
            y = y - 1
        x = x + 1 

def desenha (x_centro, y_centro, x, y):
    for i in range(8):
        if i == 0:
            screen.set_at((x_centro + x, y_centro + y), (255, 255, 255))
        elif i == 1:
            screen.set_at((x_centro - x, y_centro + y), (255, 255, 255))
        elif i == 2:
            screen.set_at((x_centro + x, y_centro - y), (255, 255, 255))
        elif i == 3:
            screen.set_at((x_centro - x, y_centro - y), (255, 255, 255))
        elif i == 4:
            screen.set_at((x_centro + y, y_centro + x), (255, 255, 255))
        elif i == 5:
            screen.set_at((x_centro - y, y_centro + x), (255, 255, 255))
        elif i == 6:
            screen.set_at((x_centro + y, y_centro - x), (255, 255, 255))
        elif i == 7:
            screen.set_at((x_centro - y, y_centro - x), (255, 255, 255))

# Inicializando PyGame(
pygame.init()

# Definindo a tela
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("DDA")

# Cor de fundo
screen.fill((0, 0, 0))

# Definindo P1 e P2 e desenhando a linha
bresenham(250, 250, 125)

# Atualizando a tela
pygame.display.flip()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
