mediaidade = maidade = maior20 = 0
homem = ''
for c in range(1, 5):
    nome = str(input('Nome: '))
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()[0]
    print('-'*40)
    mediaidade += idade
    if sexo == 'M':
        if idade > maidade:
            maidade = idade
            homem = nome
    if sexo == 'F' and idade < 20:
        maior20 += 1
print(f'A média de idade do grupo é de {mediaidade/4}.')
print(f'O homem mais velho é {homem} com {maidade} anos.')
print(f'Das mulheres, {maior20} tem menos de 20 anos.')




