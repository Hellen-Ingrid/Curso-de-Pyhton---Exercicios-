carro = float(input('Qual a velocidade do carro? '))
if carro > 80:
    print('MULTADO! Você ultrapassou o limite de 80 km/h')
    multa = (carro - 80) * 7
    print('A multa é de R$ {:.2f}'. format(multa))
print('Tenha um bom dia! Dirija com segurança!')
