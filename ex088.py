# Exercicio 088
from random import randint


print('---'*30)
print(' - MEGA SENA - ')
print('---'*30)

def gerarNumeros():
    numeros = []
    # exNum = [1,2,22,39,44,55,57,58,59,60]
    exNum = []
    while len(numeros) < 7:
        numPalpite = randint(1, 60)
        if numPalpite not in exNum:
            if numPalpite not in numeros:
                numeros.append(numPalpite)
    return numeros

cartela = []

while True:
    qntCartelas = int(input('Quantas Cartelas você deseja gerar?: '))
    for c in range(qntCartelas):
        cartela = gerarNumeros()
        cartela.sort()
        print(f'Jogo {c+1}° : {cartela}')
    opc = input('Jogar novamente:').strip().upper()[0]
    if opc == 'S': continue
    else: break