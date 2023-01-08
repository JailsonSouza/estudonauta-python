''' desafio 52
    Faça um programa que leia um número inteiro e diga se ele é ou não primo
'''
print('=========== DESAFIO 52 ===========')
cores = {
    "Amarelo" : "\033[33m",
    "Vermelho" : "\033[31m",
    "Limpar" : "\033[m"
}

num = int(input('Digite um número: '))
qtd_div = 0

for i in range(1, num+1):
    if (num % i == 0):
        print(f'{cores["Vermelho"]} {i} {cores["Limpar"]}', end='')
        qtd_div += 1
    else:
        print(f'{cores["Amarelo"]} {i} {cores["Limpar"]}', end='')
print(f'\nO número {num} foi divisivel {qtd_div} vezes, por isso ele ', end='')

if (qtd_div == 2):
    print('é primo!')
else:
    print('NÃO é primo!')
