primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da P.A.: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(termo, end='')
    termo += razão
    contador += 1