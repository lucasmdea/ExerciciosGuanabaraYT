peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura ** 2

if imc <= 18.5:
    print(f'O seu IMC é {imc:.2f} e você está abaixo do peso ideal.')
elif imc > 18.5 and imc <= 24.9:
    print(f'O seu IMC é {imc:.2f} e você está no peso ideal.')
elif imc > 25 and imc <= 29.9:
    print(f'O seu IMC é {imc:.2f} e você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print(f'O seu IMC é {imc:.2f} e você está com obesidade.')
else:
    print(f'O seu IMC é {imc:.2f} e você está com Obesidade Morbida. Procure um Médico.')