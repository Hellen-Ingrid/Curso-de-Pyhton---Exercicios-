matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
somapar = somac = maiorl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        somac += matriz[l][2]
        maiorl = max(matriz[1])
print(40*'×')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(40*'×')
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maior valor da segunda linha é {maiorl}')
