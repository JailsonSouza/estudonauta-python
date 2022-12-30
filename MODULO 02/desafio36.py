''' desafio 36
    Desenvolva um programa que leia o comprimento de três retas
    e diga ao usuário se elas podem ou não formar um triângulo
'''
print('=========== DESAFIO 36 ===========')
valor = float(input('Qual o valor da casa: R$'))
salario = float(input('Quanto você ganha por mês: R$'))
qtd_anos = int(input('Quantos anos de financiamento? '))

valor_prest = (valor / (qtd_anos*12))

print(f'para pagar uma casa de R${valor:.2f} em {qtd_anos} anos a prestação será de R${valor_prest:.2f}.')

if (valor_prest <= ((salario * 30) / 100)):
    print(f'Empréstimo pode ser CONCEDIDO!')
else:
    print(f'Empréstimo NEGADO!')
