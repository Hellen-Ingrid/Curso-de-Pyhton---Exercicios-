total = maismil = quant = barato = 0
while True:
    print(40*'-')
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do Produto: R$'))
    total += preço
    if quant == 0:
        maisbarato = nome
        barato = preço
    elif preço < barato:
        maisbarato = nome
        barato = preço
    quant += 1
    if preço > 1000:
        maismil += 1
    while True:
        stop = str(input('Deseja continuar: [S/N] ')).upper()[0]
        if stop in 'SN':
            break
        print('\033[33mERRO! Digite apenas valores válidos\033[m')
    if stop == 'N':
        break
print(40*'-')
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'Dos produtos cadastrados, {maismil} custam mais de R$1000,00')
print(f'O produto mais barato foi: {maisbarato} de R${barato:.2f}')
