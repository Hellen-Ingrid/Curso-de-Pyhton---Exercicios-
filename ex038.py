num =  int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num > num2:
    print('O \033[33mPRIMEIRO\033[m valor é maior.')
elif num < num2:
    print('O \033[33mSEGUNDO\033[m valor é maior.')
else:
    print('Não existe valor maior, os dois são \033[33mIGUAIS\033[m.')