cidade = str(input('Digite o nome de uma cidade: ')).strip()
city0 = cidade.capitalize()
city = city0.split()
print('A cidade começa com "Santo"? {}'.format('Santo' in (city[0])))
