primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da P.A.: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} => ', end='')
        termo += razão
        contador += 1
    print('Calculado.')
    mais = int(input('Você quer calcular mais termos? Digite a quantidade: '))
(print(f'Total de termos foi {total}.'))