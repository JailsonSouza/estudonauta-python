''' desafio 44
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal
    e condição de pagamento:
    - A vista dinhreiro/cheque: 10% de desconto     - em até 2x no cartão: preço normal
    - A vista no cartão: 5% de desconto             - 3x ou mais no cartão: 20% de juros 
'''
print('=========== DESAFIO 44 ===========')
print('=========== LOJA JAILSON ===========')
valor = float(input('Informe o valor das compras? R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual é a opção? '))

if (opc == 1):
    novo_valor = valor - (valor * 10 / 100)
elif (opc == 2):
    novo_valor = valor - (valor * 5 / 100)
elif (opc == 3):
    novo_valor = valor
    parc = novo_valor / 2
    print(f'Sua compra será parcelada em 2x de {parc:.2f} SEM JUROS')
elif (opc == 4):
    novo_valor = valor + (valor * 20 / 100)
    qtd_parc = int(input('Infome o quantidade de parcelas? '))
    parc = novo_valor / qtd_parc
    print(f'Sua compra será parcelada em {qtd_parc}x de {parc:.2f} COM JUROS')    
else:
    valor = 0
    novo_valor = 0
    print('Forma de pagamento informada inválida!!!')

print(f'Sua compra de R${valor:.2f} vai custar R${novo_valor:.2f} no final.')
