''' desafio 45
    Crie um programa que faça o computador jogar jokenpô com você.
'''
print(f'=========== DESAFIO 45 ===========')
from random import randint
from time import sleep

opcoes = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)

print('''Suas escolhas
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
user = int(input('Informe sua escolha? '))

if (user != 0 and user != 1 and user != 2):
    print('Jogada informada inválida!!!')
else:  
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('-=' * 20)
    print(f'O computador jogou {opcoes[comp]}')
    print(f'O jogador jogou {opcoes[user]}')
    print('-=' * 20)

    if (user == 0 and comp == 1):
        print('COMPUTADOR GANHOU')
    elif (user == 0 and comp == 2):
        print('JOGADOR GANHOU')
    elif (user == 1 and comp == 0):
        print('JOGADOR GANHOU')
    elif (user == 1 and comp == 2):
        print('COMPUTADOR GANHOU')
    elif (user == 2 and comp == 0):
        print('COMPUTADOR GANHOU')
    elif (user == 2 and comp == 1):
        print('JOGADOR GANHOU')
    elif (user == 0 and comp == 0):
        print('EMPATE!!!')
    elif (user == 1 and comp == 1):
        print('EMPATE!!!')
    elif (user == 2 and comp == 2):
        print('EMPATE!!!')
    else:
        print('Escolha informada inválida!!!')
