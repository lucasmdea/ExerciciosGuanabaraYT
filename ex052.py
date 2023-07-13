num = int(input('Digite um número: '))
for c in range(1, num+1):
    if c % num == 0:
        print(f'O número {num} é PRIMO.')
    else:
        print(f'O número {num} não é PRIMO')
print('Ele só é divisivel por 1 e por ele mesmo.')
