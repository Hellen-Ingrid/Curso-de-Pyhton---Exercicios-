n1 = float(input('Quantos km o carro percorreu? '))
n2 = float(input('Por quantos dias ele foi alugado? '))
n3 = 60 * n2
n4 = 0.15 * n1
n5 = n3 + n4
print('O preço a pagar pelo aluguel é de R$ {:.2f}'.format(n5))