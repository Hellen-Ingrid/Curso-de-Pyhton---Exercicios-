from time import sleep


def maior(* núm):
	print(20*'<>')
	print('Analisando os valores passados...')
	mai = 0
	for n in núm:
		print(n, end=' ', flush=True)
		sleep(0.5)
		if len(núm) == 0:
			mai = n
		elif n > mai:
			mai = n		
	print(f'Foram informados {len(núm)} valores ao todo.')
	print(f'O maior valor informado foi {mai}')
	
	
# Programa Principal
maior(1, 5, 9, 3)
maior(2, 0, 5, 7, 1)
maior(2, 8)
maior(4)
maior()
