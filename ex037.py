numb = int(input('Digite um número inteiro: '))
base = int(input('Digite a base de conversão:'
                 '\n1 para BINÁRIO'
                 '\n2 para OCTADECIMA'
                 '\n3 para HEXADECIMAL'
                 '\nEscolha uma das opções: '))
if base == 1:
    print(f'O valor BINÁRIO do número digitado é: {bin(numb)[2:]}.')
elif base == 2:
    print(f'O valor OCTADECIMAL do número digitado é: {oct(numb)[2:]}.')
elif base == 3:
    print(f'O valor HEXADECIMAL do número digitado é: {hex(numb)[2:]}.')
else:
    print('ERRO. Você não digitou as informações corretamente.')