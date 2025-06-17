import pygame
import random
import time
from pygame.locals import *

def escolher_cor_aleatoria():
    pisca_vermelho = {'cor': cor_vermelho, 'posicao':(251,282), 'raio': 130}
    pisca_verde = {'cor': cor_verde, 'posicao':(251,282), 'raio': 130}
    pisca_laranja = {'cor': cor_laranja, 'posicao':(251,282), 'raio': 130}
    pisca_azul = {'cor': cor_azul, 'posicao':(251,282), 'raio': 130}

    cores = [pisca_vermelho, pisca_verde, pisca_laranja, pisca_azul]
    return random.choice(cores)

def piscar_cores(lista_cores):
    for cor in lista_cores:
        if cor['cor'] == cor_verde:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_top_right=True)
        elif cor['cor'] == cor_laranja:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_bottom_left=True)
        elif cor['cor'] == cor_vermelho:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_bottom_right=True)
        elif cor['cor'] == cor_azul:
            pygame.draw.circle(interface, cor['cor'], cor['posicao'], cor['raio'], draw_top_left=True)
        pygame.display.update()
        time.sleep(tempo_piscar)
        interface.blit(Fundo, (0, 30))
        pygame.display.update()
        time.sleep(tempo_piscar)

def obter_resposta(quantidade_cores):
    resposta_usuario = []
    while quantidade_cores > 0:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_verde.collidepoint(mouse):
                    resposta_usuario.append(cor_verde)
                    quantidade_cores -= 1
                elif botao_laranja.collidepoint(mouse):
                    resposta_usuario.append(cor_laranja)
                    quantidade_cores -= 1
                elif botao_vermelho.collidepoint(mouse):
                    resposta_usuario.append(cor_vermelho)
                    quantidade_cores -= 1
                elif botao_azul.collidepoint(mouse):
                    resposta_usuario.append(cor_azul)
                    quantidade_cores -= 1
    return resposta_usuario

def restart():
    texto_jogar_novamente = fonte_botoes.render('RESTART', True, cor_preto)
    interface.blit(Fundo, (0, 30))
    botao_jogar_novamente = pygame.draw.rect(interface, cor_branco, (175, 70, 155, 60))
    interface.blit(texto_jogar_novamente, (176, 73))
    pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_jogar_novamente.collidepoint(mouse):
                    interface.blit(Fundo, (0, 30))
                    pygame.display.update()
                    return True

def escolher_dificuldade():
    global dificuldade, tempo_piscar
    escolhendo = True
    while escolhendo:
        interface.fill(cor_preto)
        titulo = fonte_botoes.render('DIFICULDADE', True, cor_branco)
        facil = pygame.draw.rect(interface, cor_branco, (170, 150, 160, 50))
        normal = pygame.draw.rect(interface, cor_branco, (170, 220, 160, 50))
        dificil = pygame.draw.rect(interface, cor_branco, (170, 290, 160, 50))

        interface.blit(titulo, (160, 80))
        interface.blit(fonte_botoes.render('Fácil', True, cor_preto), (210, 155))
        interface.blit(fonte_botoes.render('Normal', True, cor_preto), (195, 225))
        interface.blit(fonte_botoes.render('Difícil', True, cor_preto), (200, 295))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if facil.collidepoint(mouse):
                    dificuldade = 'Fácil'
                    tempo_piscar = 0.6
                    escolhendo = False
                elif normal.collidepoint(mouse):
                    dificuldade = 'Normal'
                    tempo_piscar = 0.4
                    escolhendo = False
                elif dificil.collidepoint(mouse):
                    dificuldade = 'Difícil'
                    tempo_piscar = 0.2
                    escolhendo = False

# Inicialização
pygame.init()
interface = pygame.display.set_mode((500, 530))
fonte_botoes = pygame.font.SysFont('Arial', 40)
fonte_contagem = pygame.font.SysFont('Arial', 30)
barra_status = pygame.Surface((interface.get_width(), 30))

# Fundo do jogo (aparece só quando inicia)
Fundo = pygame.image.load('Imagem.png')

# Cores
cor_preto = (0, 0, 0)
cor_branco = (255, 255, 255)
cor_vermelho = (255, 0, 0)
cor_verde = (0, 255, 0)
cor_azul = (0, 0, 255)
cor_laranja = (255, 127, 0)

# Botões (só precisam ser desenhados uma vez)
botao_azul = pygame.draw.circle(interface, cor_azul, center=(251, 282), radius=130, draw_top_left=True)
botao_verde = pygame.draw.circle(interface, cor_verde, center=(251, 282), radius=130, draw_top_right=True)
botao_vermelho = pygame.draw.circle(interface, cor_vermelho, center=(251, 282), radius=130, draw_bottom_right=True)
botao_laranja = pygame.draw.circle(interface, cor_laranja, center=(251, 282), radius=130, draw_bottom_left=True)

# Variáveis de jogo
dificuldade = 'Normal'
tempo_piscar = 0.4
texto_comeco = fonte_botoes.render('START', True, cor_preto)
texto_dificuldade = fonte_botoes.render('DIFICULDADES', True, cor_preto)

# Tela inicial
jogando = False
while not jogando:
    interface.fill(cor_preto)
    botao_comecar = pygame.draw.rect(interface, cor_branco, (180, 70, 150, 60))
    botao_dificuldade = pygame.draw.rect(interface, cor_branco, (150, 150, 200, 60))

    interface.blit(texto_comeco, (200, 74))
    interface.blit(texto_dificuldade, (160, 154))
    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == QUIT:
            quit()
        if evento.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if botao_comecar.collidepoint(mouse):
                pygame.mixer.init()
                pygame.mixer.music.load('musica_tema.mp3')
                pygame.mixer.music.play(-1)
                jogando = True
            elif botao_dificuldade.collidepoint(mouse):
                escolher_dificuldade()

# Início do jogo
interface.blit(Fundo, (0, 30))
pygame.display.update()
pontos = 0
cores_sequencia = []

# 🌀 Loop principal do jogo
while jogando:
    barra_status.fill(cor_preto)
    pontuacao = fonte_contagem.render('Pontos: ' + str(pontos), True, cor_branco)
    dificuldade_atual = fonte_contagem.render('Dificuldade: ' + dificuldade, True, cor_branco)

    barra_status.blit(pontuacao, (10, 0))
    barra_status.blit(dificuldade_atual, (300, 0))
    interface.blit(barra_status, (0, 0))
    pygame.display.update()
    time.sleep(0.5)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            quit()

    cores_sequencia.append(escolher_cor_aleatoria())
    piscar_cores(cores_sequencia)
    resposta_jogador = obter_resposta(len(cores_sequencia))
    sequencia_cores = [cor['cor'] for cor in cores_sequencia]

    if sequencia_cores == resposta_jogador:
        pontos += 1
    else:
        jogando = restart()
        if jogando:
            pontos = 0
            cores_sequencia = []
