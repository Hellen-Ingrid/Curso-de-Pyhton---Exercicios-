resp = n = 0
cont = -1
soma = -999
while n != 999:
    n = int(input('Digite um número [999 para nenhum]: '))
    soma += n
    cont += 1
print(f'Você digitou {cont} valores e a soma entre eles é de {soma}')