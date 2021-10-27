p = float(input('Qual o preço do produto? R$ '))
n1 = p * 5 / 100
n2 = p - n1
print('Com 5% de desconto, este produto custará R$ {:.2f}'.format(n2))