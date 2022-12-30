''' desafio 11
    Faça um programa que leia a largura e a altura de uma parede em metros, calcule a área e a
    quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2m²
'''
print('=========== DESAFIO 11 ===========')
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
qtd_tinta = area / 2

print(f'Sua parede tem a dimensão de {largura:.1f}x{altura:.1f} e sua área é de {area:.3f}m².')
print(f'Para pintar essa parede, você precisará de {qtd_tinta:.4f}l de tinta.')
