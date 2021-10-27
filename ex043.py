#IMC = PESO / ALTURA ** 2
peso = float(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
IMC = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif IMC >= 18 and IMC < 25: 
    print('Você tem o PESO IDEAL')
elif IMC >= 25 and IMC < 30:
    print('Você está na faixa de SOBREPESO')
elif IMC >= 30 and IMC < 40:
    print('Você está em OBESIDADE')
elif IMC >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')        
