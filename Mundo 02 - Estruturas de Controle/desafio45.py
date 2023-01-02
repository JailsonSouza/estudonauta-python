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

if (user == 0 and comp == 1):
    print('Computador ganhou')
elif (user == 0 and comp == 2):
    print('Usuario ganhou')
elif (user == 1 and comp == 0):
    print('Usuario ganhou')
elif (user == 1 and comp == 2):
    print('Computador ganhou')
elif (user == 2 and comp == 0):
    print('Computador ganhou')
elif (user == 2 and comp == 1):
    print('Usuario ganhou')
