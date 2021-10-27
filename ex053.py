frase = str(input('Digite um frase: ')).upper()
reverso = ''
for c in range(1, len(frase)+1):
    reverso += frase[-c]
if reverso == frase:
    print('Esta frase É UM PALÍNDRIMO.')
else:
    print('Esta frase NÃO É UM PALÍNDRIMO.')
