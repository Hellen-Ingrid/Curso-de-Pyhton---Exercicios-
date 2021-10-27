from random import randint
from time import sleep
números = list()


def sorteia(* núm):
	print('Sorteando 5 valores: ', end='')
	for c in range(0, 5):
		números.append(randint(0, 9))
		print(números[c], end=' ', flush=True)
		sleep(0.4)
	print('PRONTO!')


def somaPar():
	somap = 0
	for n in números:
		if n % 2 == 0:
			somap += n
	print(f'Somando os valores pares de {números}, temos {somap}.')
	

# Programa Principal
sorteia()
somaPar()
