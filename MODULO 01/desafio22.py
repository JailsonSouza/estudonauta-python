# desafio 22
# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras em maiúsculas
# o nome com todas minúsculas, quantas letras ao todo(sem considerar espaços), quantas letras tem o primeiro nome
print('=========== DESAFIO 22 ===========')

nome = str(input('Informe seu nome completo: '))
print('Analisando seu nome...')
nomeMaiusc = nome.upper()
nomeMinusc = nome.lower()
qtd_n = len(nome.strip())
primeiro_nome = nome.split()[0]
qtd_pn = len(primeiro_nome)
print(f'Nome completo: {nome}')
print(f'Seu nome em maiúsculas é {nomeMaiusc}')
print(f'Seu nome em minúsculas é {nomeMinusc}')
print(f'Seu nome tem ao todo {qtd_n} letras')
print(f'Seu primeiro nome é {primeiro_nome} e ele tem {qtd_pn} letras')
