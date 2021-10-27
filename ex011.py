h = float(input('Digite a altura em metros da parede: '))
l = float(input('Digite a largura em metros da parede: '))
a = l * h
print('Essa parede tem uma àrea de {:.1f} m2'.format(a))
t = a / 2 
print('Precisa-se de {:.1f} L de tinta para pinta-la'.format(t))