''' desafio 55
    Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
    quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
print('=========== DESAFIO 55 ===========')

maior_peso = 0
menor_peso = 0

for i in range(0, 5):
    peso = float(input(f'Peso da {i+1}° pessoa: '))

    if ((peso > maior_peso) or (i == 0)): maior_peso = peso
    if ((peso < menor_peso) or (i == 0)): menor_peso = peso
    
print(f'O maior peso lido foi de {maior_peso:.1f}kg')
print(f'O menor peso lido foi de {menor_peso:.1f}kg')
