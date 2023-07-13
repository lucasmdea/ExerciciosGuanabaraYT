from random import randint
from time import sleep
sort = randint(0, 5)
print('~=~' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar qual vai ser...')
print('~=~' * 20)
numb = int(input('Digite um número inteiro entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if numb == sort:
    print('PARABÉNS! Você venceu, consegui adivinhar o número corretamente.')
else:
    print('Você perdeu! Você não conseguiu adivinhar o número...')