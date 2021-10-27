from datetime import date
print(20 * '*~')
print('\033[32m         ALISTAMENTO MILITAR\033[m')
print(20 * '*~')
s = str(input('Qual é o seu sexo? ')).upper()
ano = date.today().year
if s == 'MASCULINO':
    idade = int(input('Em que ano você nasceu? '))
    print('Quem nasceu em {} tem {} anos em {}'.format(idade, ano - idade, ano))
    if (ano - idade) == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif (ano - idade) > 18:
        print('Você deveria ter se alistado há {} anos.'.format((ano - idade) - 18))
        print('Seu alistamento foi em {}'.format(idade + 18))
    elif (ano - idade) < 18:
        print('Faltam {} anos para você fazer 18'.format(18 - (ano - idade)))
        print('Você deve se alistar em {}'.format(idade + 18))
elif s == 'FEMININO':
    print('Não é necessário fazer o alistamento')    
  