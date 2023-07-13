print('{:=^40}'.format(' LOJAS ALEMIDA '))
valor = float(input('Digite o valor do produto em R$: '))
print('''Formas de PAGAMENTO
[ 1 ] à vista no dinheiro com 10% de desconto
[ 2 ] no cartão com 5% de desconto
[ 3 ] 2x no cartão com o preço normal
[ 4 ] 3x ou mais no cartão com 20% de juros''')
metodo = int(input('Informe o método de pagameto: '))
if metodo == 1:
    print(f'O valor do produto com 10% de desconto, fica por: {valor - (valor * 10/100):.2f}')
elif metodo == 2:
    print(f'O valor do produto com 5% de desconto, fica por: {valor - (valor * 5/100):.2f}')
elif metodo == 3:
    print(f'O valor será parcelada em 2x {valor / 2:.2f}, porém sem desconto no final.')
elif metodo == 4:
    parcela = int(input('Digite o total de parcelas que você deseja fazer: '))
    novopreço = valor + (valor * 20/100)
    totalparcela = novopreço / parcela
    print(f'O valor receberá um acrescimo de 20% de juros, ele sairá por: {totalparcela:.2f} ')