''' desafio 20
    O mesmo professor do desafio anterior quer sortear a ordem de apresentação
    de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos
    e mostre a ordem sorteada
'''
print('=========== DESAFIO 20 ===========')
from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

vetor = [a1, a2, a3, a4]
shuffle(vetor)

print(f'A ordem sorteada será \n{vetor}')
