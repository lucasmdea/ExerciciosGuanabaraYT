# Exercicio 068
import random
from time import sleep


print('---'*30)
print(' - Jogo do Par ou Ímpar - ')
print('---'*30)

def jogar(valor):
    div = valor // 2
    if div == 0:
        return True
    else:
        return False

ganhou = 0
jogadas = 0
inicio = print('O jogo vai começar!')
print('Fazendo a sua jogada...')
sleep(2)
jogo = jogar(random.randint(1,2))
if jogo == True:
    ganhou += 1
    jogadas += 1
    print('Você GANHOU essa rodada.')
elif jogo == False:
    print('Você PERDEU na primeira rodada... Tente novamente.')

while True:
    contiuar = str(input('Quer continuar a jogar? [S/N]: ')).strip().upper()
    if contiuar == 'S':
        sleep(2)
        jogo = jogar(random.randint(1,2))
        if jogo == True:
            ganhou += 1
            jogadas += 1
            print('Você GANHOU essa rodada.')
        elif jogo == False:
            jogadas += 1
            print('Você PERDEU nessa rodada.')
            print(f'Você fez um total de {jogadas} jogadas e o seu total de vitórias foi: {ganhou}')
            break
    elif contiuar == 'N':
        print(f'Você decidiu parar. Você fez um total de {jogadas} jogadas e o seu total de vitórias foi: {ganhou}')
        break
