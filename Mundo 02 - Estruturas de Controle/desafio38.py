''' desafio 38
    Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem: 
    - O primeiro valor é maior
    - o segundo valor é maior
    - Não existe valor maior, os dois são iguais
'''
print('=========== DESAFIO 38 ===========')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if (n1 > n2):
    print('O PRIMEIRO valor é maior')
elif (n1 < n2):
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
