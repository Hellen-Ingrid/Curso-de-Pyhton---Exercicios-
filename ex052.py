num = int(input('Digite um número: '))
p = 'É PRIMO'
for c in range(1, num+1):
    if num % c == 0 and c != 1 and c != num:
        p = 'NÃO É PRIMO'
print(f'O número {num} {p}')

