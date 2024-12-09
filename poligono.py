import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela
tela = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Desenho de Polígono")

# Define as cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Preenche o fundo com preto
    tela.fill(preto)

    # Define os pontos (vértices) do polígono
    pontos = [(100, 100), (200, 50), (300, 100), (250, 200), (150, 200)]

    # Desenha um polígono branco nos pontos definidos (sem preenchimento)
    pygame.draw.aalines(tela, branco, True, pontos)

    # Define os pontos (vértices) do polígono
    pontos = [(50, 250), (150, 300), (50, 350), (100, 300)]
    
    # Desenha e preenche um polígono
    pygame.draw.polygon(tela, branco, pontos)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
