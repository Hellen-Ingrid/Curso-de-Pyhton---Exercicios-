while True:
    n = float(input('Digite uma nota entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    print('Valor Inválido. ', end='')
print('FIM')