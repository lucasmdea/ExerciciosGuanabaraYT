ano = int(input('Digite uma ANO, para saber se ele é um ano BISSEXTO: '))
if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano informado é um ano BISSEXTO.')
else:
    print(f'O ano informado não é um ano BISSEXTO.')