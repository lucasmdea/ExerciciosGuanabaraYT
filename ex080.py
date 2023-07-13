# Exercicio 080


print('---'*30)
print(' - LISTAGEM DE 5 NÚMEROS - ')
print('---'*30)

lista = list()

for c in range(5):
    num = int(input(f'Digite {(c)+1}° número: '))
    if num not in lista:
        if c == 0 or num > lista[-1]:
            lista.append(num)
        else:
            for posicao, x in enumerate(lista):
                if num <= x:
                    lista.insert(posicao, num)
                    break
print(lista)