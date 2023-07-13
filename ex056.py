somaidade = 0
mediaiadade = 0
maioridadehomem = 0
nomevelho = 0
totalmulher20 = 0
for pessoa in range(1, 5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    somaidade += idade
    if pessoa == 1 and sexo == 'M': #if pessoa == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
mediaiadade = somaidade / 4
print(f'A idade média do grupo é {mediaiadade}.')
print(f'O nome do homem mais velho é {nomevelho} e sua idade é {maioridadehomem}.')
print(f'O total de mulheres com idade menores de vinte anos é {totalmulher20}.')