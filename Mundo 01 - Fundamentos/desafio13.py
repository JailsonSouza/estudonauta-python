''' desafio 13
    Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
'''
print('=========== DESAFIO 13 ===========')
salario = float(input('Qual o salario do funcionario? R$'))
new_salario = salario + (salario * 15 / 100)

print(f'Um funcionario que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${new_salario:.2f}')
