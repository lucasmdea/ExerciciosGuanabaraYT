soma = 0
contador = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        contador += 1
print(contador, soma)
