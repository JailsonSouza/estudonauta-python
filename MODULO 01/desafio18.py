# desafio 18
# Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno, 
# cosseno e tangente desse ângulo
from math import radians, cos, sin, tan
print('=========== DESAFIO 18 ===========')
angulo = float(input('Informe o ângulo que você deseja: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'O ângulo de {angulo:.1f} tem o SENO de {sen:.2f}')
print(f'O ângulo de {angulo:.1f} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {angulo:.1f} tem o TANGENTE de {tan:.2f}')
