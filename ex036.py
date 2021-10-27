from math import ceil
from time import sleep
print(20 * '×-')
print('\033[32mEMPRÉSTIMO BANCÁRIO\033[m')
print(20 * '×-')
print('')
casa = float(input('Valor da casa: \033[31mR$'))
salário = float(input('\033[mSalário do comprador: \033[31mR$'))
prazo = int(input('\033[mPrazo em anos:\033[31m '))
prestacao = casa / (12 * prazo) 
mínimo = ceil(prestacao * 100 / salário)
print('\033[mA prestação será de \033[31mR${:.2f}\033[m'.format(prestacao))
print('\033[31mCalculando...\033[m')
sleep(3)
print('A prestação equivale a \033[31m{}%\033[m do salário'.format(mínimo))
if mínimo > 30:
    print('O empréstimo foi \033[31mNEGADO!\033[m')
elif mínimo < 30:
    print('O empréstimo pode ser \033[31mCONCEDIDO!\033[m')
else:
    print('O empréstimo pode ser \033[31mCONCEDIDO!\033[m')
print('Tenha um bom dia!')   
