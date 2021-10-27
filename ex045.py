from time import sleep
from random import choice
print('\033[33m{:×^40}\033[m'.format(' JOKENPÓ '))
print('Suas Opções: ')
print('''\033[33m[ 1 ]\033[m PEDRA
\033[33m[ 2 ]\033[m PAPEL
\033[33m[ 3 ]\033[m TESOURA''')
jogador = int(input('Qual é a sua jogada? \033[33m'))
lista = [1, 2, 3]
comp = choice(lista)
print('\033[mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print(20 * '\033[33m=-\033[m')
if comp == 1:
    print('Computador jogou PEDRA')
elif comp == 2:
    print('Computador jogou PAPEL')
elif comp == 3: 
    print('Computador jogou TESOURA')
if jogador == 1:
    print('Jogador jogou PEDRA')
elif jogador == 2:
    print('Jogador jogou PAPEL')
elif jogador == 3:
    print('Jogador jogou TESOURA')
print(20 * '\033[33m=-\033[m')
if jogador == 1 and comp == 2:
    print('\033[33mComputador Vence\033[m')
elif jogador == 2 and comp == 1:
    print('\033[33mJogador Vence\033[m')
elif jogador == 3 and comp == 1:
    print('\033[33mComputador Vence\033[m')
elif jogador == 1 and comp == 3:
    print('\033[33mJogador Vence\033[m')
elif jogador == 2 and comp == 3:
    print('\033[33mComputador Vence\033[m')
elif jogador == 3 and comp == 2:
    print('\033[33mJogador Vence\033[m')
elif jogador == comp:
    print('\033[33mEMPATE\033[m')
            
