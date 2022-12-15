# desafio 19
# Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
from random import randint, choice
print('=========== DESAFIO 19 ===========')

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
vetor = [a1, a2, a3, a4]
#esc = randint(0, 3)
#print(f'O aluno escolhido foi {vetor[esc]}')
esc = choice(vetor)
print(f'O aluno escolhido foi {esc}')
