def contador(i, f, p):
    print(f'{i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print()    

saida = contador(1,10,1)
saida2 = contador(10,0,2)

def contadorP(i, f, p):
    print(f'{i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print()

num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
num3 = int(input('Digite o 3° valor: '))

saida3 = contadorP(num1, num2, num3)