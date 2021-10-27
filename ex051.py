ini = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
final = ini + 10
cont = ini
for c in range(ini, final):
    print(cont, end=' -> ')
    cont += razao
print('FIM')
