# Exercicio 093


lista = []
totalGols = 0
nomeJogador = input('Digite o Nome do Jogador: ').capitalize()
qtdPartidas = int(input('Digite a Quantidade de Partidas que ele jogou: '))
jogador = {
    'nome': nomeJogador,
    'partidas': qtdPartidas
}
for c in range(qtdPartidas):
    qtdGolsPartida = int(input(f'Quantos Gols foram feitos pelo jogador na {c+1}° partida?: '))
    lista.append(qtdGolsPartida)
    totalGols += qtdGolsPartida
jogador.update({'golspartida': lista})
jogador.update({'saldogols': totalGols})

print(jogador["nome"])
print(jogador["golspartida"])
for i, v in enumerate(jogador["golspartida"]):
    print(f'Na partida {i+1} o Jogador fez {v} gols.')
print(jogador["saldogols"])