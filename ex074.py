# Exercício 074
from random import randint


tupla = (
randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
)
listaNumeros = []

for c in tupla:
    listaNumeros.append(c)
print(f'Os números sorteados foram: {listaNumeros}')
print(f'O maior número sorteado foi: {max(tupla)}')
print(f'O menor número sorteado foi: {min(tupla)}')
