# Exercício 70


print('---'*30)
print('\n- LISTA DE PRODUTOS - \n')
print('---'*30)

def listaP(nome, valor):
    lista = []
    dicionario = {
        'produto': nome,
        'preço' : valor
    }
    lista.append(dicionario)
    return lista

totalGasto = 0
produto1000 = 0
menorProduto = 0

while True:
    produto = str(input('Informe o produto: '))
    preço = float(input('Informe o preço do produto: '))
    cadastro = listaP(produto, preço)
    totalGasto += preço
    if preço >= 1000:
        produto1000 += 1
    if menorProduto <= preço:
        menorProduto = preço
    try:
        opcao = str(input('Quer continuar a cadastrar os produtos? [S/N]: ')).strip().upper()[0]
    finally:
        if opcao == 'S':
            continue
        else:
            print(totalGasto)
            print(produto1000)
            print(menorProduto)
            print(cadastro)
            break