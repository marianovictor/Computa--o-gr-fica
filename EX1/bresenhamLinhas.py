#NOME: Victor Mariano Rocha

import pygame
import sys

# Função Principal
def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    erro = dx - dy
    x_incremento = None
    y_incremento = None
    x = x1
    y = y1
    if x1 < x2:
        x_incremento = 1
    else:
        x_incremento = -1
    if y1 < y2:
        y_incremento = 1
    else:
        y_incremento = -1
    screen.set_at((round(x), round(y)), (255, 255, 255))
    while x != x2 or y != y2:
        erro2 = 2 * erro
        if erro2 > -dy:
            erro = erro - dy
            x = x + x_incremento
        if erro2 < dx:
            erro = erro + dx
            y = y + y_incremento
        screen.set_at((round(x), round(y)), (255, 0, 0))

# Inicializando PyGame
pygame.init()

# Definindo a tela
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("DDA")

# Cor de fundo
screen.fill((0, 0, 0))

# Definindo P1 e P2 e desenhando a linha
x1, y1 = 100, 100  # P1
x2, y2 = 700, 500  # P2
bresenham(x1, y1, x2, y2)
#bresenham(700, 500, 100, 100)

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
