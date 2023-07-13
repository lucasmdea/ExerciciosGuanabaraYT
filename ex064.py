numero = contador = soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digiou {contador} números e a soma entre eles foi {soma}.')
