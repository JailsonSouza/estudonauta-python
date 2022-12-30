''' desafio 33
    Faça um programa que leia três números e mostre qual
    é o maior e qual é o menor
'''
print('=========== DESAFIO 33 ===========')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

# descobrir quem é o maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
    
# descobrir quem é o menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
