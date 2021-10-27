from random import randint
from time import sleep
vitórias = 0
print(30*'-')
print(f'{"JOGO DO PAR OU ÍMPAR":^30}')
while True:
    print(30*'-')
    num = int(input('Digite um valor de 1 à 9: '))
    jogador = str(input('Par ou Ímpar [P/I]: ')).upper()[0]
    print(30 * '-')
    comp = randint(1, 9)
    soma = comp + num
    sleep(1)
    if jogador == 'P':
        if soma % 2 == 0:
            print('\033[33mDeu PAR. Você acertou\033[m')
            vitórias += 1
        else:
            print('\033[33mDeu ÍMPAR. Você errou\033[m')
            break
    elif jogador == 'I':
        if soma % 2 == 0:
            print('\033[33mDeu PAR. Você errou\033[m')
            break
        else:
            print('\033[33mDeu ÍMPAR. Você acertou\033[m')
            vitórias += 1
print(30*'-')
print('FIM DE JOGO')
print(f'Você acertou {vitórias} vezes seguidas')
