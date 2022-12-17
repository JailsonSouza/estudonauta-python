# desafio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
print('=========== DESAFIO 24 ===========')

cidade = str(input('Em que cidade você nasceu? ')).strip().upper()
#print('SANTO' in cidade)
print(cidade[:5] == 'SANTO')