''' desafio 57
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
    'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um 
    valor correto.
'''
print('=========== DESAFIO 57 ===========')

sexo = ''

while(sexo != 'M' and sexo != 'F'):
    sexo = str(input('Informe seu sexo: '))

msg = 'Masculino' if sexo == 'M' else 'Feminino'

print(f'Seu sexo é {msg}')
