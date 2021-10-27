n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('-'*30)
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior   
    [4] Novos números
    [5] Sair do Programa
    ''')
    print('-'*30)
    opção = int(input('Digite a opção: '))
    if opção == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
    if opção == 2:
        print(f'O produto entre {n1} e {n2} é {n1*n2}')
    if opção == 3:
        if n1 > n2:
            print(f'O maior valor entre os dois é o {n1}')
        else:
            print(f'O maior valor entre os dois é o {n2}')
    if opção == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
print('FIM DO PROGRAMA')
