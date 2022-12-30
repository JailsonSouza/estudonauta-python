''' desafio 31
    Desenvolva um programa que pergunte a distância de uma viagem em Km.
    Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de
    até 200km e R$ 0,45 para viagens mais longas 
'''
print('=========== DESAFIO 31 ===========')
dist = float(input('Qual é a distância da viagem? '))

'''
    if (dist <= 200):
        valor = 0.50
    else:
        valor = 0.45
'''
valor = 0.50 if dist <=200 else 0.45

print(f'Você está prestes a começar uma viagem de {dist:.1f}Km.')
print(f'E o preço da sua passagem será de R${(dist*valor):.2f}')
