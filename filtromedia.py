import pygame
import numpy as np
import sys

# Inicialização do Pygame
pygame.init()

# Função para aplicar o filtro da média (tons de cinza)
def filtro_media(matriz_original):
    matriz_resultado = np.zeros_like(matriz_original)
    
    for x in range(largura):
        for y in range(altura):
            x_min = max(x - 1, 0)
            x_max = min(x + 2, largura)
            y_min = max(y - 1, 0)
            y_max = min(y + 2, altura)
            
            kernel = matriz_original[x_min:x_max, y_min:y_max]
            valor_medio = np.mean(kernel).astype(np.uint8)
            
            matriz_resultado[x, y] = valor_medio
    
    return matriz_resultado

# Matriz 5x5 em tons de cinza
matriz = np.array([
    [0, 0, 0, 0, 255],
    [0, 0, 0, 255, 0],
    [0, 0, 255, 0, 0],
    [0, 255, 0, 0, 0],
    [255, 0, 0, 0, 0]
], dtype=np.uint8)

# Tamanho da matriz
largura, altura = 5, 5

# Aplicando o filtro da média
matriz_filtrada = filtro_media(matriz)

print("Matriz filtrada:")
print(matriz_filtrada)

screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption('Imagem em Tons de Cinza e Filtrada')

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Desenhando a imagem filtrada pixel por pixel
    for x in range(largura):
        for y in range(altura):
            retangulo = (x * 50, y * 50, 50, 50)  # Cada pixel da matriz será um quadrado de 50x50 na tela
            
            #cor = matriz[x, y]
            cor = matriz_filtrada[x, y]
            
            pygame.draw.rect(screen, (cor, cor, cor), retangulo)
    
    pygame.display.flip()

pygame.quit()
