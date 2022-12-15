# desafio 21
# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
print('=========== DESAFIO 21 ===========')
import pygame

pygame.init()
pygame.mixer.music.load('mus.mp3')
pygame.mixer.music.play()
pygame.event.wait() 
