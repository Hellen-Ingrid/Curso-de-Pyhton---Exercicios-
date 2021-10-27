def menu():
    print(40*'-')
    print(f'{"MENU PRINCIPAL":^40}')
    print(40*'-')
    print("""\033[33m1 -\033[m \033[34mVer Pessoas Cadastradas\033[m
\033[33m2 -\033[m \033[34mCadastrar Uma Nova Pessoa\033[m   
\033[33m3 -\033[m \033[34mSair do Sistema\033[m""")
    print(40 * '-')


def opcao():
    lista_op = [1, 2, 3]
    while True:
        try:
            op = int(input('Sua Opção: '))
            print('-' * 40)
            print(f'{"OPÇÃO":>20} {lista_op[op] - 1}')
            print('-' * 40)
        except ValueError:
            print('\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
        except IndexError:
            if op != 3:
                print('\033[31mERRO: Digite Uma Opção Válida \033[m')
        if op != 3:
            menu()
        if op == 3:
            print('-'*40)
            print(f'{"SAINDO DO SISTEMA... ATÉ LOGO":^40}')
            print('-'*40)
            break

#