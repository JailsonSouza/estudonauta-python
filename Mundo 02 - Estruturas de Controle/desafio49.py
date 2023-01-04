''' desafio 49
    Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher,
    só que agora utilizando um laço for
'''
print(f'=========== DESAFIO 49 ===========')

num = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
