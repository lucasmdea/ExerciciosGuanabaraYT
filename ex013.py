salario = float(input('Insira o seu salário inicial R$: '))
reajuste = salario + (salario * 15/100)
print('O seu salário inicial de {:.2f}R$, com o reajuste de 15%, ficará {:.2f}R$.'.format(salario, reajuste))
