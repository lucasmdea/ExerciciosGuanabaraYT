pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))

if pv > sv:
    print(f'O primeiro valor {pv} é maior do que o segundo valor {sv}.')
elif sv > pv:
    print(f'O segundo valor {sv} é maior do que o primeiro valor {pv}.')
elif pv == sv:
    print(f'Os valores digitados {pv} e {sv} são iguais.')
else:
    print('ERRO. Digite valores válidos.')