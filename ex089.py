# Exercicio 089


print('---'*30)
print(' - BOLETIM - ')
print('---'*30)

boletim = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite a Primeira Nota: '))
    nota2 = float(input('Digite a Segunda Nota: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'N': break

print('---'*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('---'*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    num = int(input('Deseja saber as notas de algum aluno? (Digite o número dele): '))
    if num <= len(boletim) -1:
        print(f'As Notas do aluno N° {boletim[num][0]}, são: {boletim[num][1]}')
    opcao = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if opcao == 'N': break