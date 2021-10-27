def área(a, b):
	m = a * b
	print(f'A área de um terreno {a}x{b} é de {m}m2.')


# Programa Principal
print('    Controle de terrenos   ')
print(30*'-')
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
área(a, b)
