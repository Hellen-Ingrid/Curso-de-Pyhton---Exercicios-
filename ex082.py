numeros = []
numeros_pares = []
numeros_impares = []
cont = 0
quant_numeros = int(input('Quantos valores você deseja cadastrar? '))
while True:
    num = int(input(f'Digite o {cont+1}° valor: '))
    numeros.append(num)
    if num % 2 == 0:
        numeros_pares.append(num)
    else:
        numeros_impares.append(num)
    cont += 1
    if cont == quant_numeros:
        break
print(f'Lista geral: {numeros}')
print(f'Numeros pares da lista: {numeros_pares}')
print(f'Numeros ímpares da lista: {numeros_impares}')
