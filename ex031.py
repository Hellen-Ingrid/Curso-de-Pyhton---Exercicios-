km = float(input('Qual a distancia da sua viagem? '))
if km <= 200:
    v = km * 0.50
    print('O valor da passagem é de R$ {:.2f}'.format(v))
else:
    v = km * 0.45
    print('O valor da passagem é de {:.2f}'.format(v))