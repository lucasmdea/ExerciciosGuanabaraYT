preço = float(input('Qual é o valor do produto? R$: '))
desconto = float(input('Qual é a porcentagem desconto? %:'))
novo = preço - (preço * desconto/100)
print('O preço inicial do produto R${:.2f}, com o desconto de {:.2f}%, sairá por R${:.2f}'.format(preço, desconto, novo))
