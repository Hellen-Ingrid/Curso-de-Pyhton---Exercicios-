jogador = {}
gols = []
time = []
while True:
	jogador.clear()
	jogador['nome'] = str(input('Nome do jogador: '))
	partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
	gols.clear()
	for p in range(0, partidas):
		gols.append(int(input(f'   Gols na partida {p+1}: ')))
	jogador['gols'] = gols.copy()
	jogador['total'] = sum(gols)
	time.append(jogador.copy())
	while True:
		r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
		if r in 'NnSs':
			break
		print('ERRO! Digite apenas S ou N.')
	if r in 'Nn':
		break
print(40 * '<')
print(' N° ', end='')
for k in jogador.keys():
	print(f'{k:<14}', end='')
print()
print('-'*35)
for i, v in enumerate(time):
	print(f'{i:>2} ', end='')
	for d in v.values():
		print(f'{str(d):<15}', end='')
	print()
print(40*'>')
while True:
	j = int(input('Quer estatísticas de qual jogador? (999 interrompe) '))
	if j == 999:
		break
	if j >= len(time):
		print(f'ERRO! Não existe jogador com codígo {j}!')
	else:
		print(f'--  LEVANTAMENTO DO JOGADOR {time[j]["nome"]}')
		for i, v in enumerate(time[j]["gols"]):
			print(f'Na partida {i+1} fez {v} gols.')

	print(40*'-')
print('--- FIM ---')
