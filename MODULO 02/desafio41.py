''' desafio 41
    A confederacao nacional de natacao precisa de um programa que leia o ano de
    nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    Ate 9 anos - MIRIM
    Ate 14 anos - INFANTIL
    Ate 19 anos - JUNIOR
    Ate 20 anos - SENIOR
    Acima - MASTER
'''
print('=========== DESAFIO 41 ===========')
from datetime import date

ano_atual = date.today().year
ano_nasc = int(input('Informe seu ano de nascimento: '))
idade = ano_atual - ano_nasc

print(f'O atleta tem {idade} anos.')

if (idade <= 9):
    print('Classificação: MIRIM')
elif (idade <= 14):
    print('Classificação: INFANTIL')
elif (idade <= 19):
    print('Classificação: JUNIOR')
elif (idade <= 25):
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
