"""frase = 'Lucas tu precisa melhorar'
print(frase.replace('melhorar', 'mudar'))"""

nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é {}'.format(nome.lower()))
print('O seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
completo = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(completo[0], len(completo[0])))

