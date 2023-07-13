# Exercicio 067

print('---'*30)
print(' - Programa da Tábuada - ')
print('---'*30)

def tabuada(valor):
    print('-'*30)
    print(f'{valor} x 1 = {valor*1}')
    print(f'{valor} x 2 = {valor*2}')
    print(f'{valor} x 3 = {valor*3}')
    print(f'{valor} x 4 = {valor*4}')
    print(f'{valor} x 5 = {valor*5}')
    print(f'{valor} x 6 = {valor*6}')
    print(f'{valor} x 7 = {valor*7}')
    print(f'{valor} x 8 = {valor*8}')
    print(f'{valor} x 9 = {valor*9}')
    print(f'{valor} x 10 = {valor*10}')
    print('-'*30)


while True:
    numero = int(input('Digite um número para ver a sua tábuada [Digite um número NEGATIVO para interromper o programa]: '))
    if numero > 0:
        tabu = tabuada(numero)
    else:
        print('O programa foi interrompido.')
        break

    