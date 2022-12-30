''' desafio 37
    Escreve uma programa que leia um número inteiro qualquer e peça ao usuário escolher qual
    sera a base de conversão:
    1 - para binário
    2 - para octal
    3 - para hexadecimal
'''
print('=========== DESAFIO 37 ===========')
num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:\n
[ 1 ] converter para BINÁRIO\n
[ 2 ] converter para OCTAL\n
[ 3 ] converter para HEXADECIMAL''')

opc = int(input('Qual a sua escolha? '))

if (opc == 1):
    print(f'O número {num} convertida para BINÁRIO é igual a {bin(num)[2:]}')
elif (opc == 2):
    print(f'O número {num} convertida para OCTAL é igual a {oct(num)[2:]}')
elif (opc == 3):
    print(f'O número {num} convertida para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção informada inválida!')
