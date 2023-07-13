salario = float(input('Informe o seu salário em R$: '))

if salario >= 1.250:
    reajuste10 = salario + (salario * 10/100)
    print(f'O seu salário de {salario:.2f} R$, será reajustado em 10% e ficará em {reajuste10:.2f} R$.')
else:
    reajuste15 = salario + (salario * 15/100)
    print(f'O seu salário de {salario:.2f} R$, será reajustado em 15% e será {reajuste15:.2f} R$.')