''' desafio 46
    Faça uma contagem regressiva para o estouro de fogos de artificios, indo de
    10 a 0, com uma pausa de 1 segundo entre eles.
'''
print(f'=========== DESAFIO 46 ===========')
from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)

print('BUM! BUM! POW!')
