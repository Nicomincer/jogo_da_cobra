import pygame 
from pygame.locals import *
from random import randint 
from time import sleep

pygame.init()
'''pygame.font.init()'''
largura = 480
altura = 640
tela = pygame.display.set_mode((largura, altura))

x_cobra = 20
y_cobra = 20


x_maçã = 60
y_maçã = 20

velocidade_horizontal = 5
velocidade_vertical = 0

dado = 'Você Perdeu'

tamanho = 5

corpo_cobra = []

def aumentar_tamanho_da_cobra(cabeça):
    global corpo_cobra, cobra
    for xy in corpo_cobra:
        cobra = pygame.draw.rect(tela, (0, 255, 0), (xy[0], xy[1], 20, 20))
    

relogio = pygame.time.Clock()
while True:
    tela.fill((0,0,0))
    relogio.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_RIGHT]:
        if velocidade_horizontal == -5:
            pass
        else:
            velocidade_horizontal = 5
            velocidade_vertical = 0
    if pygame.key.get_pressed()[K_LEFT]:
        if velocidade_horizontal == 5:
            pass
        else:
            velocidade_horizontal = -5
            velocidade_vertical = 0

    if pygame.key.get_pressed()[K_UP]:
        if velocidade_vertical == 5:
            pass
        else:
            velocidade_vertical = -5
            velocidade_horizontal = 0 
    if pygame.key.get_pressed()[K_DOWN]:
        if velocidade_vertical == -5:
            pass 
        else:
            velocidade_vertical = 5
            velocidade_horizontal = 0
    
    x_cobra += velocidade_horizontal
    y_cobra += velocidade_vertical
    cabeça_cobra = []
    cabeça_cobra.append(x_cobra)
    cabeça_cobra.append(y_cobra)
    if cabeça_cobra in corpo_cobra:
        while True:
            cabeça_cobra = []
            corpo_cobra = []
            tamanho = 5
            x_cobra = 20
            y_cobra = 20
            x_maçã = 60
            y_maçã = 20
            tela.fill((255, 255, 255))
            relogio.tick(30)
            fonte = pygame.font.SysFont('arial', 40, True, True)
            texto = fonte.render(dado, False, (0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            tela.blit(texto, (100, altura//2))
            pygame.display.flip()
            
        
    corpo_cobra.append(cabeça_cobra)

    
    if x_cobra == largura:
        x_cobra = 20
    if y_cobra == altura:
        y_cobra = 20
    if x_cobra == 0:
        x_cobra = 460
    if y_cobra == 0:
        y_cobra = 620

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maçã = pygame.draw.rect(tela, (255, 0, 0), (x_maçã, y_maçã, 20, 20))

    if cobra.colliderect(maçã):
            
            x_maçã = randint(20, 460)
            y_maçã = randint(20, 620)
            tamanho+=1

    if len(corpo_cobra) >= tamanho:
       del corpo_cobra[0] 
    aumentar_tamanho_da_cobra(corpo_cobra)
    pygame.display.flip()


