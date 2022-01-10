import pygame
pygame.init()
#constantes, variaveis e recursos
#tela
largura = 706
altura = 654
nomejogo = 'tonaomae'
taxaframes = 30
nomejogo = 'TonaoMae_1.0'
tela = pygame.display.set_mode((largura,altura))
#seletor de niveis
def niveldificuldade(nivelq):
    niveis = { 1 : (450, 800,45),
     2 : (250, 450,30),
     3 : (80, 250,15)}
    return niveis[nivelq]
#banco de imagens
fundojogo = pygame.image.load('midia/cenario1.png')
fundomenuprin = pygame.image.load('midia/menuprincipal.png')
spcriançajogando = pygame.image.load('midia/meninojogando.png')
spcriançadormindo = pygame.image.load('midia/meninodormindo.png')
sptriste = pygame.image.load('midia/meninojogandotriste.png')
portaluzacesa = pygame.image.load('midia/portaluzacesa.png')
portamae = pygame.image.load('midia/portaabt.png')
nivel2 = pygame.image.load('midia/nivel2.png')
nivel3 = pygame.image.load('midia/nivel3.png')
vitoria = pygame.image.load('midia/telavitoria.png')



#banco de sons
barulhoperdeu = pygame.mixer.Sound('midia\perdeu.wav')

#jogo:
fonte = pygame.font.SysFont('Arial', 30, True, True)
    #mensagem e formatado
mensagemperdeu = 'VOCÊ PERDEU'
mensagemperdeuform = fonte.render(mensagemperdeu, False, (255,0,0))                                  

frames = pygame.time.Clock()
