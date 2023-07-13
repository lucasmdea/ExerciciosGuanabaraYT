num = int(input('Digite um número de 0 à 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print(f'Unidade: {uni}')
print(f'Dezena: {dez}')
print(f'Centena: {cent}')
print(f'Milhar: {mil}')
