# Exercício 071


print('---'*30)
print(' - CAIXA ELETRÔNICO - ')
print('---'*30)

def caixa(valor):
    valorTotal = valor
    maiorCedula = 50
    contador = 0
    
    while valorTotal > maiorCedula:
        contador += 1
        if valorTotal >= 50:
            c50 = valorTotal // 50
            contador += 50
            valorTotal -= 50
            if c50 != 0:
                return (f'Notas de 50 Reais = {c50}')
        elif valorTotal == 20 or 40:
            c20 = valorTotal // 20
            contador += 20
            if c20 != 0:
                return (f'Notas de 20 Reais = {c20}')
        elif valorTotal == 10:
            c10 = valorTotal // 10
            contador += 10
            if c10 != 0:
                return (f'Notas de 10 Reais= {c10}')
        elif valorTotal < 10:
            c1 = valorTotal
            contador += 1
            if c1 != 0:
                return (f'Notas de 1 Real = {c1}')

while True:
    try:
        sacar = int(input('Digite o valor a ser sacado [O caixa só aceita valores inteiros]: '))
    finally:
        saque = caixa(sacar)
        print(saque)
        break
        