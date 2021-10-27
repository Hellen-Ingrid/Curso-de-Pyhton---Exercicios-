def LeiaDinheiro(txt):
	válido = False
	while not válido:
		entrada = str(input(txt)).replace(',', '.').strip()
		if entrada.isalpha() or entrada == '':
			print(f'ERRO: \"{entrada}\" é um preço inválido!')
		else:
			válido = True
			return float(entrada)
			
			
def leiaint(msg):
	print(30 * '>')
	while True:
		núm = input(msg).strip()
		if núm.isnumeric():
			break
		print('\033[31mERRO! Digite apenas um valor númerico.\033[m')
	return núm