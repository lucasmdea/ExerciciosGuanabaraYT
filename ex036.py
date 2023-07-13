casa = float(input('Digite o valor da sua casa em R$: '))
salario = float(input('Digite o seu salário em R$: '))
prestacao = float(input('Digite em quantos ano você deseja financiar a casa: '))
parcela = casa / (prestacao * 12)
limite = (salario * 30/100)

if limite >= parcela:
    print('O valor da sua prestação mensal será R$.')
else:
    print('O seu salário atual não te permite financiar a casa com as parcelas desejadas.')