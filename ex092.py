# Exercicio 092


import datetime


nome = input('Digite o seu Nome: ').capitalize()
ano = int(input('Digite o seu Ano de Nascimento: '))
carteiraTrabalho = int(input('Digite a sua Carteira de Tabralho [Caso não tenha, digite 0]: '))
hoje = datetime.date.today()
anoAtual = hoje.year
idade = anoAtual - ano

ficha = {
    'nome': nome,
    'idade': idade,
    'ctps': carteiraTrabalho
}

if carteiraTrabalho != 0:
    anoContratacao = int(input('Digite o Ano de Contratação: '))
    salario = float(input('Digite quanto é o seu Salário: '))
    anoAposentadoria = 65 - idade
    ficha.update({
        'contratação': anoContratacao,
        'salário': salario,
        'aposentadoria': anoAposentadoria
    })
print(ficha)
print(f'O Seu NOME é {ficha["nome"]}')
print(f'A Sua IDADE é {ficha["idade"]}')
if ficha["ctps"] == 0:
    print('Você ainda não possui uma Carteira de Trabalho.')
else:
    print(f'O NÚMERO da sua Carteira de Trabalho é: {ficha["ctps"]}')
    print(f'O seu ANO DE CONTRACAÇÃO foi: {ficha["contratação"]}')
    print(f'O seu SALÁRIO é: {ficha["salário"]}')
    print(f'A sua APOSENTADORIA acontecerá em: {ficha["aposentadoria"]} anos.')