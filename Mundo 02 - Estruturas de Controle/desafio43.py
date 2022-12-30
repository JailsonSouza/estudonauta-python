''' desafio 43
    Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de
    triângulo será formado:
    - Equilátero: todos os lados iguais
    - Isósceles: dois lados iguais
    - Escaleno: todos os lados diferentes
'''
cores = {
    'limpar' : '\033[m',
    'azul' : '\033[34m',
    'vermelho' : '\033[31m',
    'amarelo' : '\033[33m',
    'verde' : '\033[32m',
}
print(f'=========== {cores["vermelho"]}DESAFIO 43{cores["limpar"]} ===========')
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
