# Exercicio 097


def escreva(txt):
    tamanho = len(txt) +2
    print('-'*tamanho)
    print(f' {txt}')
    print('-'*tamanho)


texto = str(input('Digite um Texto [Palavra/Frase]: '))

saida = escreva(texto)
print(saida)