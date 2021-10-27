def aumentar(núm=0, p=0, f=False):
	núm += núm * p / 100 
	return núm if not f else moeda(núm)

def diminuir(núm=0, p=0, f=False):
	núm -= núm * p / 100
	return núm if not f else moeda(núm)
	
	
def dobro(núm=0, f=False):
	núm *= 2
	return núm if not f else moeda(núm)
	

def metade(núm=0, f=False):
	núm /= 2
	return núm if not f else moeda(núm)


def moeda(núm=0, m='R$'):
	return f'{m}{núm:.2f}'.replace('.', ',')
	

def resumo(núm=0, a=10, d=5):
	print(35*'-')
	print('RESUMO DO VALOR'.center(35))
	print(35*'-')
	print(f'Preço analizado: \t{moeda(núm)}')
	print(f'Dobro do preço: \t{dobro(núm, True)}')
	print(f'Metade do preço: \t{metade(núm, True)}')
	print(f'{a}% de aumento: \t{aumentar(núm, a, True)}')
	print(f'{d}% de redução: \t{diminuir(núm, d, True)}')
	print(35*'-')
	