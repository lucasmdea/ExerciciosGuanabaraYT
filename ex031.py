distancia = float(input('Digite a distância da viagem que você deseja fazer em Km: '))
if distancia <= 200:
    valor = distancia * 0.50
    print(f'O valor da sua viagem sairá por R$ {valor:.2f}')
else:
    promo = distancia * 0.45
    print(f'O valor da sua viagem, com desconto, sairá por R$ {promo:.2f}')

# valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45