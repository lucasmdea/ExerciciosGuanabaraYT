# Exercicio 078


print('---'*30)
print(' - ARMAZENADOR DE NÚMEROS - ')
print('---'*30)

listaFin = list()
listaIni = list()
while True:
    for c in range(5):
        num = int(input(f'Digite o {c}° valor: '))
        listaIni.append(num)
        listaFin = listaIni
    listaFin.sort()
    print(f'A lista de números digitados foi: {listaFin}')
    print(f'O MENOR número digitado foi: {listaFin[0]} e sua posição foi {listaIni.index()}')
    print(f'O MAOIR número digitado foi: {listaFin[4]} e sua posição foi {listaIni.index()}')
    opcao = input('Deseja Armazenar novos números? [S/N]: ').strip().upper()[0]
    if opcao == 'S': continue
    else: break
