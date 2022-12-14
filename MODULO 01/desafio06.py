# desafio 06
# Faça um programa que leia um número inteiro e mostre o
# seu dobro, triplo e raiz quadrada.
print('=========== DESAFIO 06 ===========')
num = int(input('Informe um número: '))
print(f'O dobro do numero é {num * 2}')
print(f'O triplo do numero é {pow(num, 3)}')
print(f'A raiz quadrada do numero é {pow(num, 1/2)}')