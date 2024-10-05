import pygame

pygame.init()
relogio = pygame.time.Clock()

tamanho = (1200, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Homeless Walker")
dt = 0

# Carrega a spritesheet para nosso projeto
folhaSpritesIdle = pygame.image.load("assets/Homeless_1/Idle.png").convert_alpha()
folhaSpritesWalk = pygame.image.load("assets/Homeless_1/Walk.png").convert_alpha()

# Define os frames
framesIdle = []

for i in range(6):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128) # A imagem tem 768 largura, e tem 6 imagens que quero dividir
    frame = pygame.transform.scale(frame, (256, 256))
    framesIdle.append(frame)

# Variáveis da animação do personagem parado
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))

    # Atualiza a animação do personagem parado
    tempoAnimacaoIdle += dt

    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        indexFrameIdle = (indexFrameIdle + 1) % len(framesIdle)
        tempoAnimacaoIdle = 0.0

    # Desenha o personagem
    tela.blit(framesIdle[indexFrameIdle], (600, 250))

    pygame.display.update()
    dt = relogio.tick(60) / 1000