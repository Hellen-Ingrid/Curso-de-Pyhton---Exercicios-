ini = int(input('Início da PA: '))
razão = int(input('Razão da PA: '))
cont = 0
resp = 1
while cont < 10:
    cont += 1
    print(f'{ini}', end=' -> ')
    ini += razão
    if cont >= 10:
        while resp != 0:
            print('FIM')
            resp = int(input('\nQuantos termos você quer ver a mais? [0 para nenhum]: '))
            for c in range(1, resp+1):
                print(f'{ini}', end=' -> ')
                ini += razão

