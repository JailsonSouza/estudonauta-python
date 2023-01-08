''' desafio 53
    Faça um programa que leia uma frase diga se ela é um palindromo, desconsiderando os espaços
    Ex: APOS A SOPA
        A SACADA DA CASA
        A TORRE DA DERROTA
        O LOBO AMA O BOLO
        ANOTARAM A DATA DA MARATONA
'''
print('=========== DESAFIO 53 ===========')
frase = str(input('Informe a frase: ').upper().strip())
vetor_palavras = frase.split()
frase_comp = ''.join(vetor_palavras)
frase_inversa = frase_comp[::-1]

'''
    for letra in range(len(junto) -1, -1, -1):
        frase_inversa += frase_comp[letra]
'''
if (frase_comp == frase_inversa):
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')
