# Exercicio 096


def area(l,c):
    a = l * c
    return a

largura = float(input('Digite a Largura do Terreno: '))
comprimento = float(input('Digite o Comprimento do Terreno: '))

terreno = area(largura, comprimento)
print(f'A área do terreno de {largura} por {comprimento}, tem {terreno:.2f}m².')