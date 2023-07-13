# Exercício 076

tuplaProdutos = tuple()
lista = dict()


while True:
    produto = str(input('Digite o nome do produto: '))
    preco = int(input('Digite o preço do produto: '))
    lista = dict()
    lista = {
        'produto': produto,
        'preço': preco
    }
    tuplaProdutos = lista
    opcao = input('Quer continuar a cadastrar Produtos? [S/N]').strip().upper()[0]
    if opcao == 'S':
        continue
    else:
        print(tuplaProdutos)
        break
    