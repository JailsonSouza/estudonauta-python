''' desafio 50
    Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas
    daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
'''
print(f'=========== DESAFIO 50 ===========')
soma = 0
cont = 0

for i in range(1, 7):
    num = int(input('Digite um número para ver sua tabuada: '))
    if (num % 2 == 0):
        soma += num
        cont += 1

print(f'Você informou {cont} números PARES e a soma foi {soma}')
