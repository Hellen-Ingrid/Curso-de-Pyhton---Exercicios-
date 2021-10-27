expr = str(input('Digite a expressão: '))
p1 = p2 = 0
for p in expr:
    if p == '(':
        p1 += 1
    elif p == ')':
        p2 += 1

if p1 == p2:
    print('Sua expressão está válida')
else:
    print('Sua expressão está inválida')
