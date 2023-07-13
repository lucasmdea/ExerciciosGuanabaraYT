# Exercicio 086


print('---'*30)
print(' - MATRIZ 3x3 - ')
print('---'*30)


matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for i in range(0,3):
    for x in range(0,3):
        matriz[i][x] = int(input(f'Digite um valor para as posições [{i} , {x}]: '))
for i in range(0,3):
    for x in range(0,3):
        print(f' | {matriz[i][x]:^5} | ', end='')
    print()