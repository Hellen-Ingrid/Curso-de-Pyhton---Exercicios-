def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


num1 = leiaint('Digite um inteiro: ')
num2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {num1} e o real {num2}')
