# Solução do Guanabara

from time import sleep

c = ('\033[m', '\033[30;41m', '\033[30;42m', '\033[7;40m', '\033[30;44m');


def ajuda(com):
	título(f'Acessando Manual do Comando \'{com}\'', 4)
	print(c[3])
	help(com)
	print(c[0])
	sleep(1)
	

def título(msg, cor=0):
	print(c[cor], end='')
	print((len(msg) + 4) * '~')
	print(f'  {msg}')
	print((len(msg) + 4) * '~')
	print(c[0], end='')
	sleep(1)


# Programa Principal
comando = ''
título('Sistema de Ajuda PyHELP', 2)
while True:
	comando = str(input('Função ou biblioteca > '))
	if comando.upper() == 'FIM':
		break
	else:	
		ajuda(comando)
título('ATÉ LOGO!', 1)























# Minha Solução

'''def l(msg):
	print((len(msg) + 4) * '~')
	print(f'  {msg}')
	print((len(msg) + 4) * '~')
def manual():
	from time import sleep
	print('\033[42m')
	l('SISTEMA DE AJUDA PyHELP')
	print('\033[m')
	while True:
		sleep(0.5)
		c = str(input('Função ou biblioteca > '))
		if c.upper() == 'FIM':
			print('\033[41m')
			l('ATÉ LOGO')
			print('\033[m')
			break
		print('\033[44m')
		l(f"Acessando o manual do comando '{c}'")
		print('\033[m')
		sleep(0.5)
		print('\033[40;7m')
		help(c)
		print('\033[m')

# Programa Principal
manual()'''