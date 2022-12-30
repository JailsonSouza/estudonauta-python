''' desafio 41
    A confederacao nacional de natacao precisa de um programa que leia o ano de
    nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    Ate 9 anos - MIRIM
    Ate 14 anos - INFANTIL
    Ate 19 anos - JUNIOR
    Ate 20 anos - SENIOR
    Acima - MASTER
'''
cores = {
    'limpar' : '\033[m',
    'azul' : '\033[34m',
    'vermelho' : '\033[31m',
    'amarelo' : '\033[33m',
    'verde' : '\033[32m',
}
print(f'=========== {cores["vermelho"]}DESAFIO 35 {cores["limpar"]} ===========')
print(f'{cores["limpar"]}{cores["amarelo"]}=-' * 16)
print(f'{cores["limpar"]}{cores["azul"]} Analisar de Triângulos{cores["limpar"]}')
print(f'{cores["limpar"]}{cores["amarelo"]}=-' * 16)
print(f'{cores["limpar"]}')
p1 = float(input('Informe o primeiro segmento: '))
p2 = float(input('Informe o segundo segmento: '))
p3 = float(input('Informe o terceiro segmento: '))

if ((p1 < p2 + p3) and (p2 < p1 + p3) and (p3 < p2 + p1)):
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')

    if (p1 != p2 != p3 != p1):
        print('ESCALENO!')
    elif (p1 == p2 == p3 == p1):
        print('EQUILÁTERO!')
    else:
        print('ISÓCELES!')
        
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
