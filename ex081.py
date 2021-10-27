numeros = []
cont = 0
quant_valores = int(input('Quantos valores você deseja cadastrar? '))
while True:
    numeros.append(int(input(f'Digite o {cont+1}° valor: ')))
    cont += 1
    if cont == quant_valores:
        break
print(f'Foram digitados {len(numeros)} números')
numeros.sort(reverse=True)
print(f'Valores de forma decrescente {numeros}')
if 5 in numeros:
    print('O valor 5 ESTÁ na lista')
else:
    print('O valor 5 NÃO ESTÁ na lista')
