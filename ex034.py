salario = float(input('Qual o salário do funcionário? R$ '))
a1 = salario + (salario * 10 / 100)
a2 = salario + (salario * 15 / 100)
if salario > 1250:
    print('Quem ganhava R$ {:.2f} agora ganha R$ {:.2f}'.format(salario, a1))
else:
    print('Quem ganhava R$ {:.2f}, passa a ganhar R$ {:.2f} agora'.format(salario, a2))