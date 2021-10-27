soma = 0
for c in range(1, 501):
    if not c % 2 == 0:
        if c % 3 == 0:
            soma += c
print(f'O somatório dos valores é de {soma}')
