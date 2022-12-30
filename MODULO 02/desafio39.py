''' desafio 39
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
    se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou seja já passou do
    tempo do alistamento. Seu programa também deve mostrar o tempo que falta ou passou do prazo.
'''
print('=========== DESAFIO 39 ===========')
from datetime import date

ano_atual = date.today().year
ano = int(input('Ano de Nascimento: '))

idade = (ano_atual - ano)
ano_alistamento = ano + 18

print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}.')

if (idade > 18):
    print(f'Você já deveria ter se alistado há {ano_atual - ano_alistamento} anos.\nSeu alistamento foi em {ano_alistamento}.')
elif (idade < 18): 
    print(f'Ainda falta {ano_alistamento - ano_atual} anos para o alistamento.\nSeu alistamento será em {ano_alistamento}.')
else:
    print(f'Você tem que se alistar IMEDIATAMENTE!.')
