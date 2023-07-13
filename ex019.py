import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto anulo: '))

lista = [aluno1, aluno2, aluno3, aluno4]
sorte = random.choice(lista)
print(f'O aluno sorteado foi: {sorte}')
