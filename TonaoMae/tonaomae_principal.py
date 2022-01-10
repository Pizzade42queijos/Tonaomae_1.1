import pygame
import conseval
from pygame.locals import *
import random
import sys
import time


pygame.init()
conseval.tela

pontuacao = 0
sono = 0
global maeesta
maeesta = False
#contador e variaveis do intervalo de visitas da mãe
contagemterminou = False
play = False #se o jogo principal esta rodando
jogando = False #se o personagem está ganhando pontos
cont = 0
while True:
    nivel = 1
    conseval.tela.blit(conseval.fundomenuprin, (0,0)) #menu do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit(0)
        elif pygame.key.get_pressed()[K_w]:
            play = True
    pygame.display.update()
    while play == True: #jogo principal
        conseval.frames.tick(conseval.taxaframes)
        conseval.tela.fill((0,0,0))
        conseval.tela.blit(conseval.fundojogo, (0,0))
        #texto mutável
        mensagempontos = f'{pontuacao:2.0f}' #mostradores de pontuação
        mensagempontosform = conseval.fonte.render(mensagempontos, True, (255,255,0))
        conseval.tela.blit(mensagempontosform, (496,10))
        mensagemsono = f'{sono:2.0f}'
        mensagemsonoform = conseval.fonte.render(mensagemsono, True, (0,0,255))
        conseval.tela.blit(mensagemsonoform, (113,10))
        
        #dificuldade
        if nivel == 1 and pontuacao >= 200:
            nivel += 1
            conseval.tela.blit(conseval.nivel2,(206,220))
            pygame.display.update()
            time.sleep(5)
            pontuacao = 0
        elif nivel == 2 and pontuacao >= 500:
            nivel += 1
            conseval.tela.blit(conseval.nivel3,(206,220))
            pygame.display.update()
            time.sleep(5)
            pontuacao = 0
        elif nivel == 3 and pontuacao >= 700:
            conseval.tela.blit(conseval.vitoria,(0,0))
            pygame.display.update()
            time.sleep(5)
            pontuacao = 0
            play = False
            break    
        dif = conseval.niveldificuldade(nivel)
        difmin = dif[0]
        difmax = dif[1]
        maeaviso = dif[2]
        
        
        if contagemterminou == True: #contagem maevindo
            cont = random.randint(difmin,difmax)
            contagemterminou = False
            print(cont)
        elif cont <= 0: 
            maeesta = True
            contagemterminou = True
            pygame.display.update()
        elif cont <= maeaviso: #luz da porta
            conseval.tela.blit(conseval.portaluzacesa,(1,225))
        else:
            maeesta = False
        for evento in pygame.event.get(): #eventos do jogo
            if evento.type == pygame.QUIT:
                sys.exit(0)
            elif pygame.key.get_pressed()[K_w]:
                jogando = True
                conseval.tela.blit(conseval.spcriançajogando, (389,403))
                pontuacao += 0.20   #jogando e ganhando pontos
                pygame.display.update()
                if sono > 0.4:
                    sono -= 0.2
                if jogando == True and maeesta == True: #perdeu por mae
                    conseval.tela.blit(conseval.mensagemperdeuform, (310,200))
                    conseval.tela.blit(conseval.portamae,(1,225))
                    conseval.tela.blit(conseval.sptriste,(389,403))
                    pygame.display.update()
                    conseval.barulhoperdeu.play(+3)
                    time.sleep(10)
                    pontuacao = 0
            elif pygame.key.get_pressed()[K_r]:
                play = False
                break
            else:
                jogando = False
        if jogando == False:
            conseval.tela.blit(conseval.spcriançadormindo, (389,403))
            sono += 0.03
            if sono >= 10: #perdeu por sono
                conseval.tela.blit(conseval.mensagemperdeuform, (310,200))
                pygame.display.update()
                time.sleep(10)
                pontuacao = 0
                sono = 0
            pygame.display.update()
                    
        maeesta = False
        cont -= 1



        
        
    


