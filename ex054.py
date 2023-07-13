from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nasci = int(input('Digite o seu ano de nascimento: '))
    idade = atual - nasci
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print(f'Ao todo temos {totalmaior} pessoas mairores de idade.')
print(f'Ao todo temos {totalmenor} pessoas menores de idade.')
