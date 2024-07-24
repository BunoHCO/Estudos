import pygame
pygame.init()#Inicia a biblioteca pygame

pygame.mixer.music.load('desafio21.mp3')#Carrega a musica

pygame.mixer.music.play()#coloca pra tocar a musica

input()

pygame.event.wait()#Espera a musica acabar pra finalizar o pragrama
