# Exercicio 084


print('---'*30)
print(' - PESSOA E PESO - ')
print('---'*30)

listaGeral = []
listaPessoa = []

while True:
    nome = str(input('Digite o nome da pessoa: ')).capitalize()
    peso = float(input('Digite o peso da pessoa: '))
    listaPessoa.append(nome)
    listaPessoa.append(peso)
    listaGeral.append(listaPessoa)
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N':
        print(listaGeral)
        break
