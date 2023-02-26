''' desafio 58
    Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número
    entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
    mostrando no final quantos palpites foram necessários para vencer. 
'''
print('=========== DESAFIO 58 ===========')
print('-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 20)

from random import randint
from time import sleep

qtd_palpites = 0
comp = randint(0, 5)
while (True):
    user = int(input('Em que número eu pensei? '))
    qtd_palpites += 1
    if (user == comp):
        break
    print('PROCESSANDO...')
    sleep(2)

if (user == comp):
    print(f'Ao todo foram nescessário {qtd_palpites} para você conseguir acertar o número que eu pensei!')
