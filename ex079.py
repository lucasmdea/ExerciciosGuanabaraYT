# Exercicio 079


print('---'*30)
print(' - ARMAZENADOR DE NÚMEROS - ')
print('---'*30)

lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    lista.sort()
    opcao = input('Deseja digitar outro número? [S/N]: ').strip().upper()[0]
    if opcao == 'S': 
        continue
    else:
        print(f'Os números digitados, em ordem crescente, foram: {lista}')
        break
    
        