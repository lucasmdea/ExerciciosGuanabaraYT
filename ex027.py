nome = str(input('Digite o seu nome completo: ')).title().strip()
completo = nome.split()
print(f'O seu primeiro nome é {completo[0]}')
print(f'O seu ultimo nome é {completo[len(completo)-1]}')
