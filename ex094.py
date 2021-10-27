dados = []
pessoa = {}
acmédia = []
s = 0
while True:
	pessoa.clear()
	pessoa['nome'] = str(input('Nome: '))
	while True:
		pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
		if pessoa['sexo'] in 'MF':
			break
		print('ERRO! Digite apenas M ou F.')
	pessoa['idade'] = int(input('idade: '))
	s += pessoa['idade']
	dados.append(pessoa.copy())
	while True:
		p = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
		if p in 'SNsn':
			break
		print('ERRO! Digite apenas S ou N.')
	if p in 'Nn':
		break
print(40*'>')
print(f'-  Foram cadastradas {len(dados)} pessoas.')
print(f'-  A média de idade é de {s / len(dados):.1f} anos')
print('-  As mulheres cadastradas foram', end=' ')
for p in dados:
	if p['sexo'] in 'Ff':
		print(p['nome'], end=' ')
print('\n-  Lista de pessoas com idade acima da média:')
for i, v in enumerate(dados):
	if v['idade'] > s / len(dados):
		acmédia.append(v)
for v in acmédia:
	print(f'    Nome - {v["nome"]}; Sexo - {v["sexo"]}; Idade - {v["idade"]}')	
