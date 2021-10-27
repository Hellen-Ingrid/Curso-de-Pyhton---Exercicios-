jogador = {}
lista = []
tot = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, partidas):
	lista.append(int(input(f'Quantos gols na partida {c+1}: ')))
	tot += lista[c]
jogador['gols'] = lista[:]
jogador['total'] = tot
print(40*'<')
print(jogador)
print(40*'<')
for k, v in jogador.items():
	print(f'O campo {k} tem valor {v}.')
print(40*'<')
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c, g in enumerate(lista):
	print(f'   => Na partida {c+1}, fez {g} gols.')
print(f'Foi um total de {tot} gols.')
