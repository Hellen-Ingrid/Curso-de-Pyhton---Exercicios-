n1 = int(input(f'Digite o 1º número: '))
n2 = int(input(f'Digite o 2º número: '))
n3 = int(input(f'Digite o 3º número: '))
n4 = int(input(f'Digite o 4º número: '))
tupla = (n1, n2, n3, n4)
print(f'O valor 9 aparece {tupla.count(9)} vezes')
print(f'O valor 3 aparece pela primeira vez na posição {tupla.index(3)}')
for c in tupla:
    if tupla[c] % 2 == 0:
        par = (tupla[c])
print(f'Os valores pare digitados foram {par}')
