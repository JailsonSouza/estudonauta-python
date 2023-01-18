''' desafio 56
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
    do programa, mostre: - A média de idade do grupo            - quantas mulheres
                         - Qual é o nome do homem mais velho       tem menos de 20 anos
'''
print('=========== DESAFIO 56 ===========')

soma_das_idades = 0
nome_mais_velho = ''
idade_mais_velho = 0
qtd_mulheres_menosDe20anos = 0

for i in range(0, 4):
    print(f'--------- {i+1}° PESSOA ---------')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip()
    
    soma_das_idades += idade

    if ((sexo == 'M') and (idade >= idade_mais_velho)):
        nome_mais_velho = nome
        idade_mais_velho = idade
    if ((sexo == 'F') and (idade < 20)):
        qtd_mulheres_menosDe20anos += 1

media_das_idades = soma_das_idades / 4

print(f'A media de idade do grupo é de {media_das_idades:.2f} anos')
print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}')
print(f'Ao todo são {qtd_mulheres_menosDe20anos} mulheres com menos de 20 anos')
