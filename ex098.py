# Minha Solução

'''from time import sleep


def contador(início, fim, passo):
	print(20*'<>')
	print(f'Contagem de {início} ', end='')
	if fim < 0:
		print(f'até {fim*-1} de ', end='')
	else:
		print(f'até {fim} de ', end='')
	if passo < 0:
		print(f'{passo*-1} em {passo*-1}')
	elif passo == 0:
		print(f'{passo+1} em {passo+1}')
	else:
		print(f'{passo} em {passo}')
	if início > fim and passo > 0:
		fim -= 2
		passo *= -1
	elif passo < 0:
		fim -= 1
	elif início > fim and passo == 0:
		fim -= 2
		passo -= 1
	elif início < fim and passo == 0:
		passo += 1
	for c in range(início, fim+1, passo):
		print(c, end=' ', flush=True)
		sleep(0.5)
	print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, -1, -2)
print(20*'<>')
print('Agora é sua vez de personalizar a contagem!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)'''





# Solução do Guanabara
from time import sleep


def contador(i, f, p):
	print(20*'<>')
	if p < 0:
		p *= -1
	if p == 0:
		p = 1
	print(f'Contagem de {i} até {f} de {p} em {p}')
	
	if i < f:
		cont = i
		while cont <= f:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont += p
		print('FIM!')
	else:
		cont = i
		while cont >= f:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont -= p
		print('FIM!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print(20*'<>')
print('Agora é sua vez de personalizar a contagem')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
