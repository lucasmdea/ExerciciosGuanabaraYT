velo = float(input('Digite a velocidade do seu carro em Km/h: '))

if velo > 80:
    multa = velo - 80
    custo = multa * 7
    print(f'O seu carro passou pela lombada eletrônica na velocidade {velo} e o custo da multa é de {custo:.2f}R$')
else:
    print('O seu carro passou pela lombada eletrônica em uma velocidade permitida.')