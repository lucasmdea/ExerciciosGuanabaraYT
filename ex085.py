# Exercício 085


print('---'*30)
print(' - LISTA PAR E ÍMPAR - ')
print('---'*30)

listaGeral = []
listaPar = []
listaImpar = []

for c in range(0, 7):
    numero = int(input(f'Digite o {c+1}° número: '))
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
    listaPar.sort()
    listaImpar.sort()    
listaGeral.append(listaPar)
listaGeral.append(listaImpar)
print(f'A listagem dos números PARES foi: {listaGeral[0]}')
print(f'A listagem dos números ÍMPARES foi: {listaGeral[1]}')