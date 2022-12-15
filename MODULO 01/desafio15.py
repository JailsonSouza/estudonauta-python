# desafio 15
# Escreva um programa que pergunte a quantidade de km pecorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
# o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
print('=========== DESAFIO 15 ===========')
d = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
valor = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R${valor:.2f}')
