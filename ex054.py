from datetime import date
maior = menor = 0
ano = date.today().year
for c in range(1, 8):
    nasc = int(input(f'{c}º ano de nascimento: '))
    if ano - nasc < 18:
        menor += 1
    else:
        maior += 1
print(f'{maior} pessoas são maiores e {menor} são menores')

