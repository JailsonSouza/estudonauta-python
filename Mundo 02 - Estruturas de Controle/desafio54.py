''' desafio 54
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
    quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
print('=========== DESAFIO 54 ===========')
from datetime import date

qtd_maiorDeIdade = 0
qtd_menorDeIdade = 0
for i in range(0, 7):
    ano = float(input(f'Em que ano a {i+1}° pessoa nasceu? '))
    idade = date.today().year - ano

    if idade >= 18:
        qtd_maiorDeIdade += 1
    else:
        qtd_menorDeIdade += 1

print(f'Ao todo tivemos {qtd_maiorDeIdade} pessoas maiores de idade')
print(f'E também tivemos {qtd_menorDeIdade} pessoas menores de idade')
