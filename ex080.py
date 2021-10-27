lista = []
cont = 0
while True:
    num = int(input(f'Digite o {cont+1}° valor: '))
    if cont == 0:
        lista.append(num)
    elif num >= max(lista):
        lista.insert(cont, num)
    elif num <= min(lista):
        lista.insert(0, num)
    cont += 1
    if cont == 5:
        break
print(lista)
