''' desafio 45
    Crie um programa que faça o computador jogar jokenpô com você.
'''
print(f'=========== DESAFIO 45 ===========')
from random import randint

opcoes = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)

print('''Suas escolhas
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
user = int(input('Informe sua escolha? '))

print(f'O computador escolheu {opcoes[comp]}')
print(f'O jogador escolheu {opcoes[user]}')

