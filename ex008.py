m = float(input('Digite um valor em metros: '))
c = m * 100
ml = m * 1000
k = m / 1000
d = m * 10
print('\033[31;43;1mEsse valor em metros equivale a:\033[m')
print('\033[36m{} dm'.format(d))
print('{} cm'.format(c))
print('{} ml'.format(ml))
print('{} km\033[m'.format(k))
