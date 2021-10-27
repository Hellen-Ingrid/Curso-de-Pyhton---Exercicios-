from math import factorial
num = int(input('Digite um número para ver o seu fatorial: '))
cont = num - 1
print(f'{num}! = {num}', end='')
while cont > 0:
    print(f' x {cont}', end='')
    cont -= 1
print(f' = {factorial(num)}')
print('FIM')
