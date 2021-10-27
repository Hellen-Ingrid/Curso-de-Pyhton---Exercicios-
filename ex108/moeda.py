def aumentar(núm=0, p=0):
	núm += núm * p / 100 
	return núm


def diminuir(núm=0, p=0):
	núm -= núm * p / 100
	return núm
	
	
def dobro(núm=0):
	núm *= 2
	return núm
	

def metade(núm=0):
	núm /= 2
	return núm


def moeda(núm=0, moeda='R$'):
	x = f'{moeda}{núm:.2f}'
	return x.replace('.', ',')