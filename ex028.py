from random import randint
from time import sleep
num = randint(0, 5)
print('-*-'  * 10)
print('\033[33mEu pensei em um número de 0 a 5\033[m')
print('-*-' * 10)
n = int(input('Duvido você acertar qual foi: '))
print('-*-' * 10)
print('\033[31mPROCESSANDO...\033[m')
sleep(2)
if n == num:
    print('Nossa. Você acertou. Parabéns!')
else:
    print('Que pena. Você errou, era {} e não {}'.format(num, n))
