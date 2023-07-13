tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze',
'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

print('---'*30)
print(' - NÚMERO POR EXTENSO - ')
print('---'*30)

numero = int(input('Digite um número entre 0 e 20: '))
if numero >= 0 and numero <= 20:
    print(f'Você digitou o número: {tupla[numero]}')