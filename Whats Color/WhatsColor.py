from pygame.locals import *
from random import randint

import pygame.gfxdraw

#inicia o Pygame e as Fonts
pygame.init()
pygame.font.init()

tamanho = [900, 600]
screen = pygame.display.set_mode(tamanho, 0, 32)
pygame.display.set_caption("What's Color?")

#cores RGB
branco = (255, 255, 255)
azulClaro = (172, 245, 245)
amarelo = (255, 255, 0)
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
roxo = (209, 95, 238)
rosa = (255, 20, 147)
cinza = (169, 169, 169)

#lista das cores e nome das cores
cores = [azul, rosa, roxo, preto, verde, cinza, amarelo, vermelho]
coresNome = ['Azul', 'Rosa', 'Roxo', 'Preto', 'Verde', 'Cinza', 'Amarelo', 'Vermelho']

#escolhe randomicamente uma cor e um nome da cor
corEscolhida = randint(0, 7)
nomeEscolhido = randint(0, 7)

#carrega a imagem do botão 'verde' e faz o seu 'hitbox'
check = pygame.image.load('./assets/images/check.png').convert_alpha()
checkPequeno = pygame.transform.scale(check, (60, 60))
checkPos = [300, 490]
checkRect = Rect(checkPos, (60, 60))

#carrega a imagem do botão 'vermelho' e faz o seu 'hitbox'
negativo = pygame.image.load('./assets/images/negativo.png').convert_alpha()
negativoPequeno = pygame.transform.scale(negativo, (60, 60))
negativoPos = [540, 490]
negativoRect = Rect(negativoPos, (60, 60))

#carrega a imagem do botão 'play' e faz o seu 'hitbox'
play = pygame.image.load('./assets/images/play.png')
playPequeno = pygame.transform.scale(play, (70, 70))
playPos = [420, 480]
playRect = Rect(playPos, (70, 70))

#carrega a imagem do botão de 'ajuda' e faz o seu 'hitbox'
ajuda = pygame.image.load('./assets/images/help.png').convert_alpha()
ajudaPequeno = pygame.transform.scale(ajuda, (40, 40))
ajudaPos = [800, 20]
ajudaRect = Rect(ajudaPos, (40, 40))

#carrega a imagem do botão 'voltar' e faz o seu 'hitbox'
voltar = pygame.image.load('./assets/images/voltar.png').convert_alpha()
voltarPequeno = pygame.transform.scale(voltar, (60, 60))
voltarPos = [20, 20]
voltarRect = Rect(voltarPos, (60, 60))

#carrega a imagem do botão 'som ligado' e faz o seu 'hitbox'
muteOff = pygame.image.load('./assets/images/muteoff.png').convert_alpha()
muteOffPequeno = pygame.transform.scale(muteOff, (40, 40))
muteOffPos = [850, 20]
muteOffRect = Rect(muteOffPos, (40, 40))

#carrega a imagem do botão 'som desligado'
muteOn = pygame.image.load('./assets/images/muteon.png').convert_alpha()
muteOnPequeno = pygame.transform.scale(muteOn, (40, 40))

#carrega a imagem do logo 'What's Color' verde e faz o seu 'hitbox'
logo1 = pygame.image.load('./assets/images/logo1.png').convert_alpha()
logoRect1 = logo1.get_rect()
logoRect1.centerx = tamanho[0] / 2
logoRect1.y = -logoRect1.height

#carrega a imagem do logo com 3 circulos e faz o seu 'hitbox'
logo2 = pygame.image.load('./assets/images/logo2.png').convert_alpha()
logoRect2 = logo2.get_rect()
logoRect2.centerx = tamanho[0] / 2
logoRect2.y = logoRect2.height

#carrega a imagem das instruções e faz o seu 'hitbox'
instrucoes = pygame.image.load('./assets/images/instrucoes.png')

#carrega os SFX e as músicas
somErro = pygame.mixer.Sound('./assets/audio/homer.ogg')
somAcerto = pygame.mixer.Sound('./assets/audio/mario.ogg')
somJogo = pygame.mixer.Sound('./assets/audio/jogo.ogg')
somEspera = pygame.mixer.Sound('./assets/audio/somEspera.ogg')

#informa em quais canais cada som irá rodar e ajusta seus volumes
canalJogo = pygame.mixer.Channel(2)
canalJogo.set_volume(.2)
canalSons = pygame.mixer.Channel(3)
canalSons.set_volume(.2)
canalEspera = pygame.mixer.Channel(1)
canalEspera.set_volume(.2)

#carrega as Fonts usadas no jogo
fontAutor = pygame.font.SysFont('verdana', 10, True)
fontLetra = pygame.font.SysFont('arial', 80, True)
fonteCrono = pygame.font.Font('./assets/game_fonts/font.TTF', 30)
fonteHeart = pygame.font.Font('./assets/game_fonts/blacklist.ttf', 30)
fonteFlutuante = pygame.font.Font('./assets/game_fonts/blacklist.ttf', 20)

#variáveis
acertos = 0
erros = 0
cena = 1
iniciaMusica = True
segundos = 60
contFinal = 0
instrucao = False
mute = True
contMute = 0

#looping das telas iniciais
while True:

    screen.fill(azulClaro)

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if (cena == 1) and (logoRect1.y == 142):
            if e.type == MOUSEBUTTONDOWN and playRect.collidepoint(e.pos[0], e.pos[1]):
                iniciaMusica = True
                if mute == True:
                    canalSons.play(somAcerto)
                somEspera.stop()
                pygame.time.wait(2000)
                cena = 2
                segundos = 60
            if e.type == MOUSEBUTTONDOWN and ajudaRect.collidepoint(e.pos[0], e.pos[1]):
                cena = 0
            if e.type == MOUSEBUTTONDOWN and muteOffRect.collidepoint(e.pos[0], e.pos[1]):
                contMute += 1

    if contMute == 1:
        mute = False
        contMute = 1
    if contMute == 2:
        mute = True
        contMute = 0

    #tela de Instruções
    if cena == 0:
        screen.fill(azulClaro)
        pygame.draw.rect(screen, branco, ((145, 115), (660, 360)), 0)

        screen.blit(voltarPequeno, voltarPos)
        screen.blit(fontLetra.render('INSTRUÇÕES', True, azul), (210, 25))
        screen.blit(instrucoes, (149, 130))
        screen.blit(fontAutor.render('Cleber Alessandro © 2017', True, preto), (720, 550))
        if mute == False:
            screen.blit(muteOnPequeno, muteOffPos)
        if mute:
            screen.blit(muteOffPequeno, muteOffPos)

        if e.type == MOUSEBUTTONDOWN and voltarRect.collidepoint(e.pos[0], e.pos[1]):
            cena = 1

    #tela inicial
    if cena == 1:
        if iniciaMusica == True and mute == True:
            canalEspera.play(somEspera, -1)
            iniciaMusica = False
        if iniciaMusica == True and mute == False:
            somEspera.stop()

        if logoRect1.y < 140:
            logoRect1.y += 5
        if logoRect2.y > 130:
            logoRect2.y -= 3
        screen.blit(logo2, logoRect2)
        screen.blit(logo1, logoRect1)
        screen.blit(ajudaPequeno, ajudaPos)
        screen.blit(playPequeno, playPos)
        screen.blit(fontAutor.render('Cleber Alessandro © 2017', True, preto), (720, 550))
        if mute == False:
            screen.blit(muteOnPequeno, muteOffPos)
            iniciaMusica = True
        else:
            screen.blit(muteOffPequeno, muteOffPos)
            iniciaMusica = False
        if e.type == MOUSEMOTION:
            if ajudaRect.collidepoint(e.pos):
                screen.blit(fonteFlutuante.render('Instruções', True, preto), (780, 60))
        pygame.time.wait(int(1000 / 30))
        pygame.display.update()

    #looping do jogo
    while cena == 2:

        screen.fill(azulClaro)

        azul, rosa, roxo, preto, verde, cinza, amarelo, vermelho

        if iniciaMusica and mute == True:
            canalJogo.play(somJogo, -1)
            iniciaMusica = False
        if iniciaMusica == True and mute == False:
            somJogo.stop()

        # define a posição da letra (nome da cor) conforme seu tamanho
        if nomeEscolhido <= 2:  
            pos = (380, 240)
        elif 3 <= nomeEscolhido <= 5:
            pos = (380, 240)
        elif nomeEscolhido == 7:
            pos = (290, 240)
        else:
            pos = (320, 240)

        pygame.draw.rect(screen, branco, ((145, 115), (660, 360)), 10)
        pygame.draw.rect(screen, cores[corEscolhida], ((150, 120), (650, 350)), 0)
        pygame.gfxdraw.aacircle(screen, 570, 520, 27, vermelho)

        segundos = str(segundos)  # tranforma a variavel 'segundos' em string para ser renderizado
        acertos = str(acertos)  # tranforma a variavel 'acertos' em string para ser renderizado
        erros = str(erros)  # tranforma a variavel 'erros' em string para ser renderizado
        
        #fixa na tela as imagens e as letras usadas
        screen.blit(checkPequeno, checkPos) 
        screen.blit(negativoPequeno, negativoPos)
        screen.blit(fontLetra.render(coresNome[nomeEscolhido], True, (255, 255, 255)), pos) 
        screen.blit(fonteCrono.render('Tempo: ' + segundos, True, preto), (5, 30))
        screen.blit(fonteCrono.render('Acertos : ' + acertos, True, preto), (640, 30))
        screen.blit(fonteCrono.render('Erros     : ' + erros, True, preto), (640, 60))
        screen.blit(fonteHeart.render('True', True, preto), (305, 555))
        screen.blit(fonteHeart.render('False', True, preto), (540, 555))
        screen.blit(fontAutor.render('Cleber Alessandro © 2017', True, preto), (720, 550))
        if mute == False:
            screen.blit(muteOnPequeno, muteOffPos)
            iniciaMusica = True
        else:
            screen.blit(muteOffPequeno, muteOffPos)

        if e.type == MOUSEMOTION:
            if muteOffRect.collidepoint(e.pos):
                if mute == True:
                    screen.blit(fonteFlutuante.render('Som On', True, preto), (820, 60))
                else:
                    screen.blit(fonteFlutuante.render('Som Off', True, preto), (820, 60))

        for e in pygame.event.get():  
            if e.type == QUIT:
                exit()
            if e.type == MOUSEBUTTONDOWN:  
                if muteOffRect.collidepoint(e.pos[0], e.pos[1]):
                    contMute += 1
                    if contMute == 1:
                        mute = False
                        contMute = 1
                    elif contMute == 2:
                        mute = True
                        contMute = 0

                elif checkRect.collidepoint(e.pos[0], e.pos[1]):
                    if corEscolhida == nomeEscolhido:  # condição de acerto
                        if mute == True:
                            canalSons.play(somAcerto)
                        acertos = int(acertos)  # t
                        acertos += 1
                        corEscolhida = randint(0, 7)
                        nomeEscolhido = randint(0, 7)
                    else:  # condição de erro
                        if mute == True:
                            canalSons.play(somErro)
                        erros = int(erros)  
                        erros += 1
                        segundos = int(
                            segundos)  
                        segundos -= 3
                        screen.blit(fonteCrono.render('-4', True, vermelho), (130, 30))
                        pygame.display.update()

                        corEscolhida = randint(0, 7)
                        nomeEscolhido = randint(0, 7)

                elif negativoRect.collidepoint(e.pos[0], e.pos[1]):
                    if corEscolhida == nomeEscolhido:
                        if mute == True:    
                            canalSons.play(somErro)
                        erros = int(erros)
                        erros += 1
                        segundos = int(segundos)
                        segundos -= 3
                        screen.blit(fonteCrono.render('-4', True, vermelho), (130, 30))
                        pygame.display.update()
                        corEscolhida = randint(0, 7)
                        nomeEscolhido = randint(0, 7)
                    else: 
                        if mute == True:
                            canalSons.play(somAcerto)
                        acertos = int(acertos)
                        acertos += 1
                        corEscolhida = randint(0, 7)
                        nomeEscolhido = randint(0, 7)

        pygame.display.update()

        segundos = int(segundos)
        if segundos <= 60:
            segundos -= 1
            pygame.time.wait(1000)
            if segundos <= 0:
                cena = 3
                somJogo.stop()
                iniciaMusica = True
    
    #tela final(Game Over)
    if cena == 3:
        iniciaMusica = False
        screen.fill(azulClaro)
        screen.blit(fontLetra.render('GAME OVER', True, cores[corEscolhida]), (180, 250))
        screen.blit(fontAutor.render('Cleber Alessandro © 2017', True, preto), (720, 550))
        contFinal += 1
        
    #volta ao inicia do jogo
    if cena == 3 and contFinal == 5:
        pygame.time.wait(3000)
        cena = 1
        acertos = 0
        erros = 0
        iniciaMusica = True
        mute = True
        contFinal = 0

    if cena != 3:
        if e.type == MOUSEMOTION:
            if muteOffRect.collidepoint(e.pos):
                if mute == True:
                    screen.blit(fonteFlutuante.render('Som On', True, preto), (820, 60))
                else:
                    screen.blit(fonteFlutuante.render('Som Off', True, preto), (820, 60))
    
    pygame.display.flip()
