palavras = ('APRENDER', 'PROGRAMAR', 'LUTAR', 'CONQUISTAR', 'DEFENDER', 'PYTHON', 'VITORIA')

vogais = 'AEIOU'
f = ''

for c in palavras:
    print(f'\nNa palavra {c}, temos as vogais: ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end='')