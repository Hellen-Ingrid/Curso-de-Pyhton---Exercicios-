alunos = []
aluno = []
while True: 
	aluno.append(str(input('Nome do aluno: ')))
	aluno.append(float(input('Primeira Nota: ')))
	aluno.append(float(input('Segunda Nota: ')))
	aluno.append((aluno[1] + aluno[2]) / 2)
	alunos.append(aluno[:])
	aluno.clear()
	while True:
		r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
		if r in 'SsNn':
			break
		print('ERRO! Digite apenas S ou N.')
	if r in 'Nn':
		break
print(40*'<')	
print(f'{"N°":<6}{"Nome":<12}{"Média":<12}')
print(30*'-')
for cont, a in enumerate(alunos):
	print(f'{cont:<6}{a[0]:<12}{a[3]:<12}', end='')
	print()
while True:
	print(40*'<')
	while True:
		p = int(input('Quer as notas de qual aluno? (999 interrompe) '))
		if p < len(alunos) or p == 999:
			break
		print(f'ERRO! Não existe aluno {p}')
	if p == 999:
		break
	print(f'>>>   Notas de {alunos[p][0]}')
	print(f'Nota 1: {alunos[p][1]}')
	print(f'Nota 2: {alunos[p][2]}')
print('---   VOLTE SEMPRE!  ---')
	