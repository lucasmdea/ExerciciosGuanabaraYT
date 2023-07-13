n = int(input('Digite um número para ser fatorado: '))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f)