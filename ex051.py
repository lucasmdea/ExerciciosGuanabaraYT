valor = int(input('Digite um valor: '))
razao = int(input('Digita um valor para a razão: '))

for c in range(1, 11):
    pa = valor + (c - 1) * razao
    print(pa)