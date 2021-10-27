stop = 0
while stop != 1:
    sexo = str(input('Qual o seu sexo [M/F]: ')).upper()[0]
    if sexo == 'M' or sexo == 'F':
        stop = 1
    else:
        print('\033[31mERRO! Digite apenas [M/F]\033[m')
print('FIM')
