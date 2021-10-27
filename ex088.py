from random import randint
from time import sleep
lista = []
jogos = []
tot = 0
print(40*'=')
print('{:^40}'.format('JOGO NA MEGA SENA'))
print(40*'=')
quant = int(input('Quantos jogos você quer que eu sortei? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'>>>>>>> SORTEANDO {quant} JOGOS <<<<<<<')
for cont, jogo in enumerate(jogos):
    sleep(1)
    jogo.sort()
    print(f'Jogo {cont+1}: {jogo}')
print('>>>>>>> BOA SORTE! <<<<<<<')

 
    
     

    































#Minha Solução
'''from random import randint
from time import sleep
lista = []
valores = []
print(40*'×')
print('{:^40}'.format('JOGO NA MEGA SENA'))
print(40*'×')
jogos = int(input('Quantos jogos você quer que eu sortei? '))
for c in range(0, jogos):
    for c in range(0, 6):
        valor = randint(0, 60)
        if valor in valores:
            while valor in valores:
                valor = randint(0, 60)       
            valores.append(valor)
        else:
            valores.append(valor)    
    lista.append(valores[:])
    valores.clear()
print(f'>>>>>>> SORTEANDO {jogos} JOGOS <<<<<<<')
for cont, j in enumerate(lista):
    lista[cont].sort()
    sleep(1)
    print(f'jogo {cont+1}: {j}')
print('{:>^40}'.format(' BOA SORTE! '))'''
    