num = int(input('Digite um número qualquer: '))
r = num % 2
if r == 0:
    print('{} é um número PAR'.format(num))
else:
    print('{} é um número ÍMPAR'.format(num))