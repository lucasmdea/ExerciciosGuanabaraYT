# cateto_op = float(input('Digite o valor do Cateto Oposto: '))
# cateto_adj = float(input('Digite o valor do Cateto Adjacente: '))
# hipo = (cateto_op ** 2 + cateto_adj ** 2) ** (1/2)
# print(f'O valor da Hipotenusa do triângulo retangulo é {hipo)}')

from math import hypot

co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hi = hypot(co, ca)
print(f'A Hipotenusa vai medir {hi:.2f}')
