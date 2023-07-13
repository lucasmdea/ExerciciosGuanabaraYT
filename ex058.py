from random import randint
from time import sleep
computador = randint(0, 10)
print('Vou pensar em um número entre 0 e 10, tente adivinhar qual vai ser...')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite um número inteiro entre 0 e 10: '))
    print('PROCESSANDO...')
    sleep(1)
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um número maior...')
        elif jogador > computador:
            print('Tente um número menor...')
print(f'PARABÉNS, Você venceu! Seu total de tentativas foi: {tentativas}.')
