ini = int(input('Início da PA: '))
razão = int(input('Razão da PA: '))
cont = 0
while cont < 10:
    cont += 1
    print(f'{ini}', end=' -> ')
    ini += razão
print('FIM')
