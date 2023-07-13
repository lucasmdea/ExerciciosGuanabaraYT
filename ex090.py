# Exercicio 090


print('---'*30)
print(' - LISTA DE ALUNOS - ')
print('---'*30)

dados = dict()
lista = []
def dicionario(n,m):
    dados = {
        'nome': n,
        'media': m
    }
    return dados

nome = str(input('Digite o nome do aluno: ')).capitalize()
media = float(input('Digite a média das notas do aluno: '))
dados = dicionario(nome, media)
print(dados['nome'])
print(dados['media'])
if dados['media'] > 6:
    print(f'A situação do Aluno(a) {nome}, é APROVADO.')
else:
    print(f'A situação do Aluno(a) {nome}, é REPROVADO.')