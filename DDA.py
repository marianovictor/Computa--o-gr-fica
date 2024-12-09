#import pygame
import sys

# Função Principal
def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    x_inc = dx / steps
    y_inc = dy / steps
    x = x1
    y = y1
    screen.set_at((round(x), round(y)), (255, 255, 255))
    for k in range(1, int(steps) + 1):
        x += x_inc
        y += y_inc
        screen.set_at((round(x), round(y)), (255, 255, 255))

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
DDA(x1, y1, x2, y2)

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
