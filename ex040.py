n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2) / 2

if media <= 5:
    print(f'Você está reprovado! A sua média é: {media:.1f}')
elif media > 5 and media <= 6.9:
    print(f'Você está de recuperação! A sua média é: {media:.1f}')
else:
    print(f'PARABÉNS você foi APROVADO! A sua média é: {media:.1f}')