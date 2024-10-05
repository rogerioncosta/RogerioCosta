import pygame
# Inicializar o pygame
pygame.init()

tamanho = (900, 500)
# Cria uma tela com tamanho especificado
tela = pygame.display.set_mode(tamanho)

#Define o título da janela
pygame.display.set_caption("Hello Games!")

# Define um relógio para controlar o FPS
relogio = pygame.time.Clock()

while True:
    # Lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() # Fechando o pygame

        # Preenche a tela com uma cor
        tela.fill((40, 200, 100))

        

        # Atualiza a tela
        pygame.display.update()

        relogio.tick(60) # Define a quantidade de FPS