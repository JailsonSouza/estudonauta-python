# desafio 35
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo
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
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulos!')
