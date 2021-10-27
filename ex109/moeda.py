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
