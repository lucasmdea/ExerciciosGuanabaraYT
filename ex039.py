from datetime import date
hoje = date.today().year
nasc = int(input('Digite em que ano você nasceu: '))
idade = hoje - nasc
print(f'Quem nasceu no ano de {nasc} tem {idade} em {hoje}.')
if idade == 18:
    print('Você está no ano do seu ALISTAMENTO.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já PASSOU do prazo, o seu ALISTAMENTO já ocorreu em {saldo}')
    alista = hoje + saldo
    print(f'O seu ALISTAMENTO foi em {alista}')
elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não está no tempo de realizar o ALISTAMENTO, ele ocorrerá em {saldo}.')
    alista = hoje + saldo
    print(f'O seu ALISTAMENTO será em {alista}')
