maior18 = homens = mulher18 = 0
while True:
    print(30*'-x')
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 +=1
    sexo = stop = ''
    while True:
        sexo = str(input('Sexo: [F/M] ')).upper()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 18:
            mulher18 += 1
        if sexo in 'FM':
            break
        print('\033[31mERRO! Digite apenas valores válidos.\033[m')
    while True:
        stop = str(input('Deseja continuar: [S/N] ')).upper()[0]
        if stop in 'SN':
            break
        print('\033[31mERRO! Digite apenas valores válidos.\033[m')
    if stop == 'N':
        break
print(30*'-x')
print(f'Das pessoas cadastradas {maior18} tem mais de 18 anos.')
print(f'{homens} homems foram cadastrados')
print(f'{mulher18} mulheres tem menos de 18 anos')