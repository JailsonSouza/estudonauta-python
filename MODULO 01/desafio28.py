# desafio 28
# Faça um programa que faça o computador "pensar" em um número inteiro 
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador, e printar se o usuário ganhou ou perdeu
print('=========== DESAFIO 28 ===========')
myColors = {
    'red' : '\031',
    'yellow' : '\033',
    'blue' : '\034',
    'purple' : '\035',
}
print(myColors['yellow'], '=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=-' * 30)
from random import randint
from time import sleep

comp = randint(1, 5)
usua = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if (usua == comp):
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {comp} e não no {usua}!')