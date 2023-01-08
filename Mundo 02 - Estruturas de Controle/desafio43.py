''' desafio 43
    Desenvolda uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
    seu status, de acordo com a tabela a baixo:
    - Abaixo de 18.5: Abaixo do peso    - 25 até 30: Sobrepeso    - Acima de 40: Obesidade Mórbida
    - Entre 18.5 e 25: Peso ideal       - 30 até 40: Obesidade
'''
print('=========== DESAFIO 43 ===========')
peso = float(input('Informe seu peso? (kg) '))
altura = float(input('Informe sua altura? (m) '))

imc = peso / (altura * altura)

print(f'O imc dessa pessoa é {imc:.1f}')

if (imc < 18.5):
    print('Categoria: Abaixo do peso')
elif (imc <= 25):
    print('Categoria: Peso ideal')
elif (imc <= 30):
    print('Categoria: Sobrepeso')
elif (imc <= 40):
    print('Categoria: Obesidade')
else:
    print('Categoria: Obesidade mórbida')
