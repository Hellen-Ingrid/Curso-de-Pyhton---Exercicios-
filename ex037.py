print(20 * '×-')
print('\033[33mConversor de bases númericas\033[m')
print(20 * '×-')
print('')
num = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('\033[31m[1]\033[m para BINÁRIO')
print('\033[31m[2]\033[m para OCTAL')
print('\033[31m[3]\033[m para HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido em BINÁRIO é {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)))
else:
    print('\033[31mOpção inválida. Tente novamente.\033[m')