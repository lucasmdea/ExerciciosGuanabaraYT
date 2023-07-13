# Exercicio 095


listaJogadores = []
gols = []
totalGols = 0
while True:
    jogador.clear(0)
    nomeJogador = input('Digite o Nome do Jogador: ').capitalize()
    qtdPartidas = int(input('Digite a Quantidade de Partidas que ele jogou: '))
    jogador = {
        'nome': nomeJogador,
        'partidas': qtdPartidas
    }
    for c in range(qtdPartidas):
        qtdGolsPartida = int(input(f'Quantos Gols foram feitos pelo jogador na {c+1}° partida?: '))
        gols.append(qtdGolsPartida)
        totalGols += qtdGolsPartida
    jogador.update({'golspartida': gols})
    jogador.update({'saldogols': totalGols})
    
    listaJogadores.append(jogador.copy())
    
    opcao = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if opcao == 'S': 
        continue
    
    else:

        print(jogador["nome"])
        print(jogador["golspartida"])

        for k, v in enumerate(listaJogadores):
            print(f'Na partida {k+1} o Jogador fez {v} gols.')
        print(jogador["saldogols"])
        
        break