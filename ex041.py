nascimento = int(input('Digite o seu ano de nascimento: '))
ano = 2022 - nascimento
if ano <= 9:
    print(f'A sua idade é {ano} e a sua categoria é MIRIM.')
elif ano <= 14:
    print(f'A sua idade é {ano} e a sua categoria é INFANTIL')
elif ano <= 19:
    print(f'A sua idade é {ano} e a sua categoria é JUNIOR.')
elif ano <= 20:
    print(f'A sua idade é {ano} e a sua categoria é SENIOR.')
else:
    print(f'A sua idade é {ano} e a sua categoria é MASTER.')
