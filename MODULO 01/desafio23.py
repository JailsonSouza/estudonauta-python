# desafio 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# ex: 'Digite um número: 1834' --- unidade: 4, dezena: 3, centena: 8, milhar: 1
print('=========== DESAFIO 23 ===========')

number = int(input('Informe um número: '))
print(f'Analisando o número{number}')
und = number // 1 % 10
dez = number // 10 % 10
cen = number // 100 % 10
mil = number // 1000 % 10
print(f'Unidade: {und}\nDezena: {dez}\nCentena: {cen}\nMilhar: {mil}')
