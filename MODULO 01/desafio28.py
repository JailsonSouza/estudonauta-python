# desafio 28
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza ---- Primeiro: Ana, Último: Souza
print('=========== DESAFIO 28 ===========')
print('-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 20)
from random import randint
from time import sleep

comp = randint(1, 5)
user = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)
if (user == comp):
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {comp} e não no {user}!')
