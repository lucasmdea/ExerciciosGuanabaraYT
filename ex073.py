# Exercício 073


tuplaTabela = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athetico-PR', 'Atlético-MG', 'América-MG',
'Goiás', 'Santos', 'Bragantino', 'Botagofo', 'São Paulo', 'Ceará SC', 'Fortaleza', 'Coritiba', 'Cuiabá', 'Avai',
'Juventude', 'Atlético-GO', 'Juventude')

print('---'*30)
print(' - TABELA CAMPEONATO BRASILEIRO DE FUTEBOL - ')
print('---'*30)
opcao = int(input('\
| 1 | Os 5 Primeiros colocados\n\
| 2 | Os 4 Últimos colocados\n\
| 3 | Listar todos os times em ordem alfabética\n\
| 4 | Em que posição está o seu time\n\
Selecione uma opcões: \
'))

if opcao == 1:
    print(f'Os Cinco Primeiros colocados são: {tuplaTabela[0:5]}')
elif opcao == 2:
    print(f'Os Quatro Últimos colocados são: {tuplaTabela[-4:]}')
elif opcao == 3:
    ordLista = sorted(tuplaTabela)
    print(f'A ordem alfabética dos times da Série A, é: {ordLista} ')
elif opcao == 4:
    time = str(input('Digite o nome do seu Clube: ')).capitalize()
    if time in tuplaTabela:
        times = tuplaTabela.index(time)+1
        print(f'O seu Time está, atualmente, na {times}° posição do Campeonato Brasileiro')
    else:
        print('Não foi possível encontrar o seu Time.')
