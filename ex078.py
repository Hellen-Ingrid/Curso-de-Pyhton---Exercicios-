lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}ª valor: ')))
print(f'O maior valor digitado foi {max(lista)} na posição {lista.index(max(lista)) + 1}')
print(f'O menor valor digitado foi {min(lista)} na posição {lista.index(min(lista)) + 1}')
