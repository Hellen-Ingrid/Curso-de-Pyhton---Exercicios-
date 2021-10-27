maior = menor = 0
for c in range(1, 6):
    peso = int(input(f'{c}º peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg. e o menor de {menor}kg')
