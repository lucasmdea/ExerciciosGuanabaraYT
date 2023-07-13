# Exercicio 082


print('---'*30)
print(' - LISTA DE NÚMEROS PARES E ÍMPARES - ')
print('---'*30)

listaGeral = []
listaPar = []
listaImpar = []

while True:
    num = int(input('Digite um número: '))
    listaGeral.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'S':
        continue
    else:
        print(f'A lista dos números digitados, é: {listaGeral}')
        print(f'A lista dos números PARES, é: {listaPar}')
        print(f'A lista dos números IMPARES, é: {listaImpar}')
        break