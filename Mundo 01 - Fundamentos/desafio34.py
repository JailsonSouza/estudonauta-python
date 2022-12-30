''' desafio 34
    Escreva um programa que pergunte o salário de um funcionário
    e calcule o valor do seu aumento, para salários superiores a
    R$ 1,250,00, calcule um aumento 10%, para inferiores ou iguais 15%
'''
print('=========== DESAFIO 34 ===========')
sal = float(input('Qual é o salário do funcionário? R$'))

por = 15 if sal <= 1250 else 10
novo_sal = sal + (sal * por / 100)

print(f'Quem ganhava R${sal:.2f} passa a ganhar R${novo_sal:.2f} agora.')
