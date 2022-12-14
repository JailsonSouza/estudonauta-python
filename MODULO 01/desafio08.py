# desafio 08
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
print('=========== DESAFIO 08 ===========')
medida = float(input('Informe uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10 
dm = medida * 10
cm = medida * 1000
mm = medida * 10000

print(f'A medida de {medida:.1f}m corresponde a\n{km}km\n{hm}hm\n{dam}dam\n{dm:.0f}dm\n{cm:.0f}cm\n{mm:.0f}mm\n')
