''' desafio 47
    Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50
'''
print('=========== DESAFIO 47 ===========')

# for i in range(1, 51):
for i in range(2, 51, 2):
    if (i % 2 == 0):
        print(f'{i} ', end='')
