matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        if c <= 2 and l == 0:
            matriz[0].append(valor)      
        if c <= 2 and l == 1:
            matriz[1].append(valor)
        if c <= 2 and l == 2:
            matriz[2].append(valor)
print(40*'*')
for l in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[l][c]), end='')
    print()




#Solução do Guanabara
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print(40*'*')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()'''