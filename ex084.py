pessoas = []
cont = 0
perg = int(input('Quantas pessoas deseja cadastrar? '))
while True:
    nome = str(input(f'Nome da {cont+1}° pessoa: '))
    pessoas.append(nome)
    peso = float(input(f'Peso de {nome}: '))
    if cont == 0:
        maior_peso = peso
        mp_nome = nome
    elif peso > maior_peso:
        maior_peso = peso
        mp_nome = nome
    pessoas.append(peso)
    cont += 1
    if perg == cont:
        break

print(f'Foram cadastradas {len(pessoas)/2:.0f} pessoas')
print(f'O maior peso foi de {mp_nome}, com {maior_peso:.0f}kg')
