from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6)}
ranking = ()
print('Valores Sorteados:')
for k,v in jogadores.items():
	print(f'{k} tirou {v} no dado.')
	sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(20*'<>')
print('  <<< RANKING DOS JOGADORES >>>')
for c, j in enumerate(ranking):
	print(f'    {c+1}° lugar: {j[0]} com {j[1]}.')
	sleep(1)