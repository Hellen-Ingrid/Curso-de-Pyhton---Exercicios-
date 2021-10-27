while True:
    cont = 0
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    while cont < 10:
        cont += 1
        print(f'{num} x {cont} = {num*cont}')
