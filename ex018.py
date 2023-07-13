from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo qualquer: '))

seno = sin(radians(angulo))
print(f'O angulo {angulo} tem o SENO de {seno:.2f}')

cosseno = cos(radians(angulo))
print(f'O angulo {angulo} tem o COSSENO de {cosseno:.2f}')

tangente = tan(radians(angulo))
print(f'O angulo {angulo} tem a TANGENTE de {tangente:.2f}')