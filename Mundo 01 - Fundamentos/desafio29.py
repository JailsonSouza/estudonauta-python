''' desafio 29
    Escreva um programa que leia a velocidade de um carro, se ele ultrapassar
    80km/h. mostre uma mensagem dizendo que ele foi multado. A multa vai custar
    R$ 7.00 por cada Km acima do limite
'''
print('=========== DESAFIO 29 ===========')
vel = int(input('Qual é a velocidade do carro? '))

if (vel > 80):
    multa = ((vel - 80) * 7)
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}')

print('Tenha um bom dia! Dirija com segurança!')
