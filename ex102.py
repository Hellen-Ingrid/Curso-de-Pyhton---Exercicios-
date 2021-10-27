def fatorial(n, show=False):
	"""
	-> Calcula o fatorial de um número.
	:param n: O número a ser calculado.
	:param show: (opcional) Mostrar ou não a conta.
	:return: O valor do Fatorial de um número n.	
	"""
	from math import factorial
	f = factorial(n)
	print(20*'<>')
	if show:
		print(f'{n} ', end='')
		for c in range(n-1, 0, -1):
			print(f'x {c} ', end='')
		print('=', end=' ')
	return f	


#Programa Principal		
print(fatorial(5, show=True))
help(fatorial)
