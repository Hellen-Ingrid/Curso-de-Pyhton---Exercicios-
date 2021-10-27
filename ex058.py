from random import randint
from time import sleep
comp = randint(0, 10)
cont = 1
jogador = int(input('Pensei em um número de 0 a 10. Tente adivinhar: '))
if jogador != comp:
    while jogador != comp:
        sleep(1)
        jogador = int(input(f'\033[31mVOCÊ ERROU. Tente de novo:\033[m '))
        cont += 1
sleep(1)
print('VOCÊ ACERTOU. PARABÉNS!')
print(f'Foram necessários {cont} palpites para acertar')

