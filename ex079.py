números = []
while True:
    números.append(int(input('Digite um número: ')))
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Quer Continuar? ')).upper()[0]
    if perg == 'N':
        break
números.sort()
print(f'Você digitou os valores {números}')
