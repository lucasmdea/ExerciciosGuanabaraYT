# Exercício 4

x = input('Digite algo: ')

print('O tipo de dado informado é: ', type(x))
print('Tem espaços vazios no dado informado?' , x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está com letas maiusculas?', x.isupper())
print('Está com letras minusculas?', x.islower())
print('Está capitalizada?', x.istitle())

