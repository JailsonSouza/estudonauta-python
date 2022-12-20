# desafio 28
# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça ao usuário tente descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o user ganhou ou perdeu
print('=========== DESAFIO 28 ===========')
print('-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 20)
from random import randint
from time import sleep

comp = randint(0, 5)
user = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)
if (user == comp):
    print(f'PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {comp} e não no {user}!')
