# desafio 06
# Faça um programa que leia um número inteiro e mostre o
# seu dobro, triplo e raiz quadrada.
print('=========== DESAFIO 06 ===========')
num = int(input('Informe um número: '))
print(f'O dobro de {num} é {num * 2}')
print(f'O triplo de {num} é {num * 3}')
print(f'A raiz quadrada de {num} é {(pow(num, 1/2)):.2f}')