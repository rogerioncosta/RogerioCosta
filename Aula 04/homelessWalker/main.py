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
framesWalk = []

for i in range(6):
    frame = folhaSpritesIdle.subsurface(i * 128, 0, 128, 128) # A imagem tem 768 largura, e tem 6 imagens que quero dividir
    frame = pygame.transform.scale(frame, (256, 256))
    framesIdle.append(frame)

for i in range(8):
    frame = folhaSpritesWalk.subsurface(i * 128, 0, 128, 128) # A imagem tem 768 largura, e tem 6 imagens que quero dividir
    frame = pygame.transform.scale(frame, (256, 256))
    framesWalk.append(frame)

# Variáveis da animação do personagem parado
indexFrameIdle = 0
tempoAnimacaoIdle = 0.0
velocidadeAnimacaoIdle = 10

indexFrameWalk = 0
tempoAnimacaoWalk = 0.0
velocidadeAnimacaoWalk = 10

# Retangulo do personagem
personagemRect = framesIdle[0].get_rect(midbottom=(100, 480))
personagemRectWalk = framesWalk[0].get_rect(midbottom=(100, 480))

gravidade = 1

inverte = False # Controla se a imagem está invertida

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    tela.fill((255, 255, 255))

    # Atualiza a animação do personagem parado
    tempoAnimacaoIdle += dt
    tempoAnimacaoWalk += dt

    # Verifica se o tempo de animação do personagem parado é maior ou igual ao tempo de animação
    if tempoAnimacaoIdle >= 1 / velocidadeAnimacaoIdle:
        # Atualiza o frame do personagem parado
        indexFrameIdle = (indexFrameIdle + 1) % len(framesIdle)
        tempoAnimacaoIdle = 0.0

    if tempoAnimacaoWalk >= 1 / velocidadeAnimacaoWalk:
        # Atualiza o frame do personagem parado
        indexFrameWalk = (indexFrameWalk + 1) % len(framesWalk)
        tempoAnimacaoWalk = 0.0


    # Movimenta o personagem no eixo X
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        personagemRect.x -= 200 * dt # Movimenta pra esquerda   
        personagemRectWalk.x -= 200 * dt # Movimenta pra esquerda
        inverte = True        
    if teclas[pygame.K_RIGHT]:
        personagemRect.x += 200 * dt # Movimenta pra direita
        personagemRectWalk.x += 200 * dt # Movimenta pra direita
        inverte = False
    if teclas[pygame.K_SPACE]:
        if personagemRect.centery == 330:
            gravidade = -30

    # Gravidade aumenta
    gravidade += 3

    personagemRect.y += gravidade
    personagemRectWalk.y += gravidade

    if personagemRect.centery >= 330:
        personagemRect.centery = 330

    if personagemRectWalk.centery >= 330:
        personagemRectWalk.centery = 330

    # Desenha o personagem    
    if teclas[pygame.K_LEFT]:
        # Desenha o personagem  
        pygame.draw.rect(tela, (0, 0, 0), personagemRectWalk, 2)
        # tela.blit(framesWalk[indexFrameWalk], personagemRectWalk)
        frame_atual = pygame.transform.flip(framesWalk[indexFrameWalk], inverte, False)
        tela.blit(frame_atual, personagemRectWalk)
    elif teclas[pygame.K_RIGHT]:
        pygame.draw.rect(tela, (0, 0, 0), personagemRectWalk, 2)
        tela.blit(framesWalk[indexFrameWalk], personagemRectWalk)
    else:
        # Desenha o personagem 
        pygame.draw.rect(tela, (0, 0, 0), personagemRect, 2)
        # Desenha um retangulo em volta do personagem
        tela.blit(framesIdle[indexFrameIdle], personagemRect) 


    pygame.display.update()
    dt = relogio.tick(60) / 1000