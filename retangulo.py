import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configura a tela
tela = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Desenho de Retângulo")

# Define as cores
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Preenche o fundo com preto
    tela.fill(preto)

    # Define as coordenadas e dimensões do retângulo: (X, Y, Largura, Altura)
    coordenadas_retangulo = (100, 100, 200, 100)

    # Desenha um retângulo vermelho usando as coordenadas definidas
    pygame.draw.rect(tela, vermelho, coordenadas_retangulo, 2)

    # Atualiza a tela
    pygame.display.flip()

# Encerra o Pygame
pygame.quit()
sys.exit()
