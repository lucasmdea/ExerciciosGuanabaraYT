# Exerciocio 091


from random import randint

resultado = {
    'Jogador N° 1' : randint(1, 6),
    'Jogador N° 2' : randint(1, 6),
    'Jogador N° 3' : randint(1, 6),
    'Jogador N° 4' : randint(1, 6),
}

for k, v in resultado.items():
    print(f'O {k} tirou {v}')

ordem = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
print(ordem)