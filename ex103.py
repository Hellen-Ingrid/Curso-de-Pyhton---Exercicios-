# Solução do Guanabara


'''def ficha(nome='<desconhecido>', gols=0):
	print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
	

# Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
	g = int(g)
else:
	g = 0
if n.strip() == '':
	ficha(gols=g)
else:
	ficha(n, g)'''
	
	

# Minha Solução

def ficha(nome='', gols=True):
	if nome in '':
		nome = '<desconhecido>'
	if not gols or gols != '':
		gols = 0
	print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do jogador: '))
g = input('Número de gols: ')
ficha(n, g)