sexo = str(input('Digite o seu Sexo [F/M]: ')).upper()[0].strip()
while sexo not in 'MF':
    sexo = str(input('ERRO. Digite o seu sexo de forma correta, [F/M]: ')).upper()[0].strip()
print(f'Seu sexo é {sexo}, obrigado pela informação.')

