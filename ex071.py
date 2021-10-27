print(40 * '-')
print('{:^40}'.format('BANCO UP'))
print(40 * '-')
saque = int(input('Valor a ser sacado R$'))
total = saque
céd = 100
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'Total de {totalcéd} cédulas de R${céd}')
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totalcéd = 0
        if total == 0:
            break
print(40 * '-')
print('Volte sempre ao BANCO UP! Tenha um bom dia!')