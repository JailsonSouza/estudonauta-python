''' desafio 40
    Escreva um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
    no final, de acordo com a média atingida:
    - média abaixo de 5.0: REPROVADO
    - média entre 5.0 e 6.9: RECUPERAÇÃO
    - média 7.0 ou superior: APROVADO
'''
print('=========== DESAFIO 40 ===========')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = ((n1 + n2) / 2)

print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media}')

if (media >= 0) and (media < 5):
    print('O aluno está REPROVADO')
elif (media < 7):
    print('O aluno está em RECUPERAÇÃO')
elif (media <= 10):
    print('o aluno está APROVADO')
else:
    print('Valores informados inválidos!')
