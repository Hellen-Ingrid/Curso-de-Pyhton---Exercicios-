'''Cada um dos segmentos deve ser menor
do que a soma dos outros dois'''
print('\033[33m=*=*\033[m' * 10)
print('     \033[33mANALIZADOR DE TRIÂNGULOS\033[m')
print('\033[33m=*=*\033[m' * 10)
s1 = float(input('Primeiro Segmento: \033[33m'))
s2 = float(input('\033[mSegundo Segmento: \033[33m'))
s3 = float(input('\033[mTerceiro Segmento: \033[33m'))
if s1 == s2 and s2 == s3:
    Tipo = 'EQUILÁTERO'
elif s1 == s2 or s1 == s3 or s3 == s2:
    Tipo = 'ISÓSCELES'
elif s1 != s2 or s1 != s3 or s3 != s2:
    Tipo = 'ESCALENO'
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('\033[mOs segmentos acima PODEM FORMAR um triângulo')
    print('Tipo: \033[33m{}\033[m'.format(Tipo))
else:
    print('\033[mOs segmentos acima NÃO PODEM formar um triângulo')     
