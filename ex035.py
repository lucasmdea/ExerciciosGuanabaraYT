lado1 = float(input('Digite o valor de uma 1° reta: '))
lado2 = float(input('Digite o valor de uma 2° reta: '))
lado3 = float(input('Digite o valor de uma 3° reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
# if (lado1 <= lado2 or lado1 <= lado3) and (lado2 <= lado1 or lado2 <= lado3) and (lado3 <= lado2 or lado3 <= lado1):
# print('ERRO! O valores informados não formam um triângulo...')
# else: print(f'Os valores informados {lado1},{lado2} e {lado3} formam um triângulo')
    print('Os lados informados formam um triângulo.')
else:
    print('Os lados informandos não formam um triângulo.')