resp = ''
cont = soma = 0
while resp != 'N':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'Você digitou {cont} valores')
print(f'A média entre os valores digitados é de {soma/cont}')
print(f'O MAIOR valor digitado foi {maior} e o MENOR foi {menor}')
