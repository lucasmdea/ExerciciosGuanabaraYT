from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÔES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESROURA''')
jogador = int(input('Qual é sua jogada? '))
print('=-=' * 10)
print(f'O Computador escolheu {itens[computador]}')
print(f'O Jogador escolheu {itens[jogador]}')
print('=-=' * 10)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('ERRO! Jogada INVALIDA.')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('ERRO! Jogada INVALIDA.')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('ERRO! Jogada INVALIDA.')
