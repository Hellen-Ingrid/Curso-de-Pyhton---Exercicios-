números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quartorze',
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um número de 0 a 20 para vê-lo por extenso: '))
        if 0 <= num <= 20:
            break
        print('\033[31mERRO! Digite apenas números entre 0 e 20.\033[m')
    print(f'Você digitou o número: {números[num]}')
    per = ' '
    while per not in 'SN':
        per = str(input('Que continuar [S/N]: ')).upper()[0]
    if per == 'N':
        break
print('-- FIM --')
