lado1 = float(input('Digite o valor de uma 1° reta: '))
lado2 = float(input('Digite o valor de uma 2° reta: '))
lado3 = float(input('Digite o valor de uma 3° reta: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado3:
    print('O lados informados formam um triângulo.')
    if lado1 == lado2 and lado1 == lado3:
        print(f'O triangulo formado pelos lados {lado1}, {lado2} e {lado3} é um triangulo EQUÍLATERO.')
    elif lado1 != lado2 and lado1 != lado3:
        print(f'O triangulo formado pelos lados {lado1}, {lado2} e {lado3} é um triangulo ESCALENO.')
    else:
        print(f'O triangulo formado pelos lados {lado1}, {lado2} e {lado3} é um triangulo ISÓSCELES.')
else:
    print('Os lados informandos não formam um triângulo.')