''' desafio 27
    Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
    o primeiro e o ultimo nome separadamente.
    Ex: Ana Maria de Souza ---- Primeiro: Ana, Último: Souza
'''
print('=========== DESAFIO 27 ===========')
nome = str(input('Digite seu nome completo: ')).split()

print(f'Seu primeiro nome é {nome[0]}')
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
