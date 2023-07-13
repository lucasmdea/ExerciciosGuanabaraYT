p = float(input('Informe a Quilômetragem porcorrida pelo carro Km: '))
d = int(input('Informe a quantidade de dias de alugel do carro: '))

kmdcd = (p * 0.15) + (d * 60)

print('O valor que deverá ser pago pelo alugel e quilometragem do carro é {:.2f} R$ '.format(kmdcd))
