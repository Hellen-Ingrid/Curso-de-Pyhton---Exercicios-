n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média do aluno é de {}'.format(m))
if m < 5.0:
    print('Está abaixo de 5.0')
    print('Situação final: \033[31mREPROVADO!\033[m')
elif m == 5.0 or m <= 6.9:
    print('Está entre 5.0 e 6.9')
    print('O aluno fará uma \033[31mRECUPERAÇÃO!\033[m')
else: 
    print('Situação final: \033[32mAPROVADO!\033[m')
           
    

