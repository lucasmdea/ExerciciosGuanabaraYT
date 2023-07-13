# Ecercício 069


totalMaioresIdade = totalH = totalM20 = totalPessoas = 0

while True:
    nome = str(input('Digite o nome da pessoa a ser cadastrada: ')).upper()
    sexo = str(input('Digite o SEXO da pessoa a ser cadastrada [F/M]: ')).strip().upper()[0]
    idade = int(input('Digite a IDADE da pessoa a ser cadastrada: '))
    totalPessoas += 1
    if idade >= 18:
        totalMaioresIdade += 1
    if sexo == 'M':
        totalH += 1
    elif sexo == 'F' and idade < 20:
        totalM20 += 1
    try:
        opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    finally:
        if opcao == 'S':
            continue
        else:
            print(f'O total de PESSOAS CADASTRADAS foi: {totalPessoas}')
            print(f'O total de pessoas MAIORES DE IDADE, cadastradas foi: {totalMaioresIdade}')
            print(f'O total de pessoas do SEXO MASCULINO, cadastradas foi: {totalH}')
            print(f'O total de pessoas do SEXO FEMININO MENORES DE 20 ANOS, cadastradas foi: {totalM20}')
            break
        