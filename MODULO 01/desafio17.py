# desafio 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
print('=========== DESAFIO 17 ===========')
catO = float(input('Informe o comprimento do cateto oposto: '))
catA = float(input('Informe o comprimento do cateto adjacente: '))
#hip = ((catO**2 + catA ** 2) ** (1/2))
hip = hypot(catO, catA)
print(f'A hipotenusa vai medir {hip:.2f}')
