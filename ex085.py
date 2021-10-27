lista = []
par = []
ímpar = []
lista.append(par)
lista.append(ímpar)
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 != 0:
        ímpar.append(valor)
par.sort()
print(f'Os valores pares digitados foram: {lista[0]}')
ímpar.sort()
print(f'Os valores ímpares digitados foram: {lista[1]}')



#Solução do Guanabara
'''núm = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    elif valor % 2 != 0:
        núm[1].append(valor)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')'''      





