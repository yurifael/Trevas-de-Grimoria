import asyncio
import pygame
import sys

# Inicia o motor do jogo
pygame.init()

# Cria a janela do jogo (800 de largura por 600 de altura)
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Trevas de Grimória")

# Posição inicial e tamanho do personagem (32x32 pixels)
jogador = pygame.Rect(400, 300, 32, 32)
velocidade = 5

# Função principal que o navegador consegue rodar
async def main():
    rodando = True
    while rodando:
        # 1. Verifica se você clicou para fechar o jogo
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # 2. Lê as teclas pressionadas para mover o personagem
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
            jogador.y -= velocidade
        if teclas[pygame.K_s]:
            jogador.y += velocidade
        if teclas[pygame.K_a]:
            jogador.x -= velocidade
        if teclas[pygame.K_d]:
            jogador.x += velocidade

        # 3. Pinta o fundo de escuro e desenha o personagem na nova posição
        tela.fill((18, 18, 24))
        pygame.draw.rect(tela, (180, 180, 190), jogador)

        # Atualiza a tela e dá uma pausa rápida para o navegador respirar
        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

# Inicia o loop do jogo
asyncio.run(main())