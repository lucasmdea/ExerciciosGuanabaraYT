# Exercicio 081


print('---'*30)
print(' - LISTA DETALHADA DE NÚMEROS - ')
print('---'*30)

lista = []
contador = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    lista.sort(reverse=True)
    contador += 1
    opcao =  input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'S':
        continue
    else:
        print(f'A quantidade de números digitados foi: {contador}')    
        print(f'A lista dos números, em ordem decrescente, é: {lista}')
        if 5 in lista:
            print('O número 5, foi digitado e está contido na lista.')
        else:
            print('O número 5, não foi digitado, portanto, não está na lista.')
        break