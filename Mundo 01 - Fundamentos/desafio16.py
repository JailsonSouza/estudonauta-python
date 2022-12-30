''' desafio 16
    Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
    a sua porção inteira
'''
print('=========== DESAFIO 16 ===========')
from math import trunc

valor = float(input('Informe um valor: '))

#print(f'O valor digitado foi {valor} e sua porção inteira é {valor:.0f}')
#print(f'O valor digitado foi {valor} e sua porção inteira é {int(valor)}')
print(f'O valor digitado foi {valor} e sua porção inteira é {trunc(valor)}')
