# Exercicio 066

soma = contador = 0
num1 = int(input('Digite um número inteiro: '))
while True:
    num = int(input('Digite um número inteiro, Caso queira parar digite 999: '))
    if num == 999:
        break
    contador += 1
    soma += num
    
print(f'Você digitou {contador} números e a soma de todos eles foi: {soma + num1}.')