n1 = int(input('Digite um número: '))
print('Analizando o número {}'.format(n1))
print('Unidade: {}'.format(n1 // 1 % 10))
print('Dezena: {}'.format(n1 // 10 % 10))
print('Centena: {}'.format(n1 // 100 % 10))
print('Milhar: {}'.format(n1 // 1000 % 10))

