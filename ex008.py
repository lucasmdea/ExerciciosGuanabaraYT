metros = float(input('Digite um valor em metros: '))

cm = metros*100
mm = metros*1000

print(f'O valor digitado em Centímetros é: {cm}cm')
print(f'O valor digitado em Milímetros é: {mm}mm')

km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10

print(f'O valor informado em Decímetro é: {dm}dm')
print(f'O valor informado em Quilômetro é: {km}km')
print(f'O valor informado em Hectômetro é: {hm}hm')
print(f'O valor informado em Decâmetro é: {dam}dam')
