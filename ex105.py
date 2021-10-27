def notas(* n, sit=False):
	"""
	-> Função para analisar notas e situações de vários alunos
	:param n: Uma ou mais notas de vários alunos.
	:param sit: (Opcional) Situação geral da turma
	:return: Dicionário com vários informações sobre a situação da turma.
	"""
	dados = dict()
	dados['Total'] = len(n)
	dados['Maior'] = max(n)
	dados['Menor'] = min(n)
	dados['Média'] = sum(n) / len(n)
	if sit:
		if dados['Média'] < 5:
			dados['Situação'] = 'RUIM'
		elif 7 > dados['Média'] > 5:
			dados['Situação'] = 'RAZOÁVEL'
		elif dados['Média'] >= 7:
			dados['Situação'] = 'BOA'
	return dados

		
# Programa Principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
#help(notas)