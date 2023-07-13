# Exercicio 087


print('---'*30)
print(' - MATRIZ 3x3 - ')
print('---'*30)


matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
somarPar = 0
somaTerceira = 0
maiorLinha = 0
for i in range(0,3):
    
    for x in range(0,3):
        matriz[i][x] = int(input(f'Digite um valor para as posições [{i} , {x}]: '))
        if matriz[i][x] % 2 == 0:
            somarPar += matriz[i][x]        

for i in range(0,3):
    for x in range(0,3):
        print(f' | {matriz[i][x]:^5} | ', end='')
    print()

for d in range(0,3):
    somaTerceira += matriz[d][2]

for c in range(0,3):
    if c == 0:
        maiorLinha = matriz[1][c]
    elif matriz[1][c] > maiorLinha:
        maiorLinha = matriz[1][c]

print(f'A SOMA dos valores PERES, foi: {somarPar}')
print(f'A SOMA dos valores da Tercerira Coluna, é: {somaTerceira}')
print(f'O MAIOR valor digitado na Segunda Linha, foi: {maiorLinha}')