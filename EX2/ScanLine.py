#Victor Mariano Rocha

import pygame
import sys

# Definindo pontos dos polígonos
poligono1 = [(50, 100), (200, 50), (350, 100)]
poligono2 = [(150, 200), (300, 200), (200, 300)]

# Função para desenhar linha entre dois pontos
def draw_line(surface, cor, x, y):
    pygame.draw.line(surface, cor, x, y)

# Função para preencher polígono
def scanline_fill(surface, cor, poligono):
    # Obter coordenadas y mínimas e máximas
    min_y = min(point[1] for point in poligono)
    max_y = max(point[1] for point in poligono)

    # Percorrer cada linha horizontal
    for y in range(min_y, max_y + 1):
        intersecao = []
        for i in range(len(poligono)):
            p1 = poligono[i]
            p2 = poligono[(i + 1) % len(poligono)]

            if p1[1] <= y < p2[1] or p2[1] <= y < p1[1]:
                # Calcular interseção com a linha
                x = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
                intersecao.append(x)

        # Ordenar interseções
        intersecao.sort()

        # Desenhar segmentos de linha
        for i in range(0, len(intersecao), 2):
            draw_line(surface, cor, (intersecao[i], y), (intersecao[i + 1], y))

# Inicializar PyGame
pygame.init()

# Definir largura e altura da tela
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Algoritmo Scan Line")

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preencher tela com cor branca
    screen.fill((255, 255, 255))

    # Preencher e desenhar polígonos
    scanline_fill(screen, (0, 0, 0), poligono1)
    scanline_fill(screen, (0, 0, 0), poligono2)

    # Atualizar tela
    pygame.display.flip()