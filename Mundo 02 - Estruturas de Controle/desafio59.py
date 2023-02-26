''' desafio 59
    Crie um programa que leia dois valores e mostre um menu
    na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.
'''
print('=========== DESAFIO 59 ===========')
opc = 0

n1 = int(input('Informe o primeiro número? '))
n2 = int(input('Informe o segundo número? '))

while (opc != 5):

    print('''
    ------------ TABUADA ------------
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA 
    ''')
    opc = int(input('Informe a sua escolha? '))

    if (opc == 1): # SOMAR
        print(f'{n1} + {n2} = {n1+n2}')


