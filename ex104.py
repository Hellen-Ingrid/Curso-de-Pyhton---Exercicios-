# Minha Solução
def leiaint(txt):
	while True:
		n = input(txt).strip()
		if n.isnumeric():
			break
		print('\033[31mERRO! Digite apenas um valor inteiro válido.\033[m')
	return n

	
	
# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')





#Solução do Guanabara

'''def leiaInt(msg):
	ok = False
	valor = 0
	while True:
		n = str(input(msg))
		if n.isnumeric():
			valor = n
			ok = True
		else:
			print('\033[0;31mERRO! Digite apenas um número inteiro válido.\033[m')
		if ok:
			break
	return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')'''