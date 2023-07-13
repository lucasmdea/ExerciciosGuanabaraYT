v1 = int(input('Digite o 1° Valor: '))
v2 = int(input('Digite o 2° valor: '))
opção = 0
while opção != 5:
    print('''
    [ 1 ] Somar os valores
    [ 2 ] Multiplicar os valores
    [ 3 ] Qual é o maior número
    [ 4 ] Adicionar número
    [ 5 ] Fechar o programa''')
    opção = int(input('Digite uma das opções: '))
    if opção == 1:
        soma = v1 + v2
        print(f'A soma dos valores informados é {soma}.')
    elif opção == 2:
        produto = v1 * v2
        print(f'A multiplicação dos valores informados é {produto}.')
    elif opção == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print(f'O maior valor digitado entre {v1} e {v2}, é {maior}.')
    elif opção == 4:
        print('Digite os novos valores.')
        v1 = int(input('Digite o novo primeiro valor: '))
        v2 = int(input('Digite o novo segundo valor: '))
    elif opção == 5:
        print('Obrigado por utilizar o meu programa.')
print('Volte sempre.')