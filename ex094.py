# Exercicio 094


lista = []
mulheres = []
pessoas = {}
acimaMedia = []
soma = 0
while True:
    pessoas.clear()
    nome = input('Digite o NOME: ').upper()
    sexo = input('Digite o SEXO [F/M]: ').upper()
    idade = int(input('Digite a sua IDADE: '))
    pessoas = {
        'nome' : nome,
        'sexo': sexo,
        'idade': idade
    }
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    if sexo == 'F':
        mulheres.append(pessoas.copy())
    opcao = input('Deseja continuar adicionando pessoas? [S/N]: ').strip().upper()[0]
    if opcao == 'S': continue
    else: 
        print(lista)
        break

media = soma/len(lista)
if pessoas['idade'] > media:
    acimaMedia.append(pessoas)
print(len(lista))
print(media)
print(mulheres)
print(acimaMedia)