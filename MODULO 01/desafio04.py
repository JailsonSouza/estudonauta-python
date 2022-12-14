# desafio 04
# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possiveis sobre ele
print('=========== DESAFIO 04 ===========')
var = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(var)}')
print(f'So tem espaços? {var.isspace()}')
print(f'So tem número? {var.isnumeric()}')
print(f'É alfabético? {var.isalpha()}')
print(f'É alfanumérico? {var.isalnum()}')
print(f'Está em maiúsculas? {var.isupper()}')
print(f'Está em mainúsculas? {var.islower()}')
print(f'Está capitalizada? {var.istitle()}')