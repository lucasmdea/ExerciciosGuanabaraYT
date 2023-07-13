# Exercício 069


print('---'*30)
print(' - Cadastro de Pessoas - ')
print('---'*30)

def cadastro(n, s, i):
    dados = dict()
    chave = dados['nome']
    dados[chave] = {
        'nome': n,
        'sexo': s,
        'idade': i
    }
    return dados

contadorCadastro = 0
while True:
    nome = str(input('Digite o nome da pessoa a ser cadastrada: ')).upper()
    sexo = str(input('Digite o SEXO da pessoa a ser cadastrada [F/M]: ')).strip().upper()[0]
    idade = int(input('Digite a IDADE da pessoa a ser cadastrada: '))
    cadastros = cadastro(nome, sexo, idade)
    contadorCadastro += 1
    opcao = input('Deseja cadastrar outra pessoa? [S/N]').strip().upper()[0]
    if opcao == 'S':
        nome = str(input('Digite o nome da pessoa a ser cadastrada: ')).upper()
        sexo = str(input('Digite o SEXO da pessoa a ser cadastrada [F/M]: ')).strip().upper()[0]
        idade = int(input('Digite a IDADE da pessoa a ser cadastrada: '))
        cadastros = cadastro(nome, sexo, idade)
        contadorCadastro += 1
    else:
        break
    for c in cadastros['idade']:
        idadeTotal = c
        if idade > 18:
            maioresIdade = idadeTotal
    for i in cadastros['sexo']['M']:
        sexoM = i
    for y in cadastros['sexo']['F']:
        sexoF = y
        for x in cadastros['idade']:
            menoresIdade = x            
print(maioresIdade)
print(sexoM)
print(menoresIdade)