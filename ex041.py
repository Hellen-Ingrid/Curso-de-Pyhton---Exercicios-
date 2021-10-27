from datetime import date
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: \033[32mMIRIN\033[m')
elif idade > 9 and idade <= 14:
    print('Classificação: \033[32mINFANTIL\033[m')
elif idade > 14 and idade <= 19:
    print('Classificação: \033[32mJUNIOR\033[m')
elif idade > 19 and idade <= 20:
    print('Classificação: \033[32mSÊNIOR\033[m')
elif idade > 20:
    print('Classificação: \033[32mMASTER\033[m')