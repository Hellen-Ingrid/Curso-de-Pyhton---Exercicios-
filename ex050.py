soma = 0
for c in range(1, 7):
    num = int(input(f'Número {c}: '))
    if num % 2 == 0:
        soma += num
print(f'O somátorio dos números PARES digitados é de {soma}')
