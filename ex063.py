# Minha solução

n = int(input('Digite  um número: '))
f1 = 0
cont = 1
f2 = f3 = 1
print(f'{f1} -> ', end='')
while cont <= n:
    cont += 2
    print(f'{f2} -> {f3}', end=' -> ')
    f2 = f2 + f3
    f3 = f2 + f3
print('FIM')



# Solução melhor

'''n = int(input('Quantos termos quer mostrar: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')'''

