# Exercicio 084

lista = []
mat = str(input('Digite uma expressão matemática: '))

for simb in mat:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Valida')
else:
    print('Invalida')
