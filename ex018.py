from math import radians, sin, cos, tan
a = float(input('Digite um ângulo qualquer: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O SENO do ângulo é {:.2f}'.format(s))
print('O COSSENO é {:.2f}'.format(c))
print('E a TANGENTE é {:.2f}'.format(t))