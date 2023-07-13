maiorpeso = 0
menorpeso = 0

for pessoa in range(1, 6):
    peso = float(input(f'O peso da {pessoa}° pessoa em Kg é: '))
    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso
print(f'O maior peso registrado foi {maiorpeso}Kg.')
print(f'O menor peso registrado foi {menorpeso}Kg.')
