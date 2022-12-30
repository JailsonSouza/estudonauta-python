''' desafio 12
    Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
'''
print('=========== DESAFIO 12 ===========')
preco = float(input('Qual é o preço do produto? R$'))
new_preco = preco - (preco * 5 / 100)

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${new_preco:.2f}.')
