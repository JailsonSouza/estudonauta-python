''' desafio 51
    Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
    No final, mostre os 10 primeiros termos dessa progressão.
'''
print('=========== DESAFIO 51 ===========')
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
dec_term = primeiro + (10 - 1) * razao

for i in range(primeiro, dec_term + 1, razao):
    print(f'{i} -> ', end='')

print('ACABOU')
