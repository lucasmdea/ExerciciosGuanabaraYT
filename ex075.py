# Exercicío 075


print('---'*30)
print(' - ARMAZENADOR DE NÚMERO - ')
print('---'*30)

tupla = tuple()
numero1 = int(input('Digite o 1° número: '))
numero2 = int(input('Digite o 2° número: '))
numero3 = int(input('Digite o 3° número: '))
numero4 = int(input('Digite o 4° número: '))
tuplaFinal = (*tupla, numero1, numero2, numero3, numero4)

if 9 in tuplaFinal:
    n9 = tuplaFinal.count(9)
    if n9 == 1:
        print(f'O número 9, apareceu {n9} vez')
    else: 
        print(f'O número 9, apareceu {n9} vezes')
if 3 in tuplaFinal:
    print(f'O número 3 apareceu pela 1° na posição {tuplaFinal.index(3)+1}')
for c in tuplaFinal:
    num = c 
    if num % 2 == 0:
        print(f'{num} é Par')
    else:
        print(f'{c} é Impar')