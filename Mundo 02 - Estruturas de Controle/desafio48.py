''' desafio 48
    Faça um programa que calcule a soma entre todos os números impares que
    são múltiplos de três e que se encontram no intervalo de 1 até 500
'''
print('=========== DESAFIO 48 ===========')

soma = 0
qtd = 0
'''
    for i in range(1, 501):
        if (i % 3 == 0 and i % 2 != 0):

'''
for i in range(1, 501, 2):
    if (i % 3 == 0):
        qtd += 1
        soma += i

print(f'A soma de todos os {qtd} valores solicitados é {soma}')
